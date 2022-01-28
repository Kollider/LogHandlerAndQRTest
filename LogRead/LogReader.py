# 2021-11-15 13:36:11,423 - INFO - > 'WOLF;88;7cbb94;UU;-7664;'
# 2021-11-15 13:36:11,423 - DEBUG - Detect ec54a8
# 2021-11-15 13:36:11,913 - DEBUG - > 'BIG;77;D5FA3F;1;66;42;6160;1;2;46;5;0;0;141;1;-3474;1;DD;'
# 2021-11-15 13:36:11,913 - WARNING - > 'BAD;75;ec803d;8450;1;02;'

#order of parameters in log line
order = ["handler", 'numb1', "id", 'numb2', 'numb3', 'numb4', 'numb5', 'numb6', 'numb7', 'numb8', 'numb9', 'numb10',
         'numb11', 'numb12', 'numb13', 'numb14', 'numb15', 'state']

#function to transform the log file into the dictionary
def log_to_dictionary(filename, data):
    #open file
    with open(filename) as f:
        for line in f:
            #we need only the body of the log to resolve the task which is between quotation marks
            marker_left = line.find("'")
            marker_right = line.rfind("'")
            #there are some lines without quotation marks, so we exclude them
            if marker_right != -1:
                #crop the log line
                line_without_date = line[marker_left + 1:marker_right - 1]
                content = line_without_date.split(";")
                content = [x.strip() for x in content]
                #only the lines with more than 6 elements are necessary
                if len(content) > 6:
                    #transformation
                    structure = {key: value for key, value in zip(order, content)}
                    data.append(structure)
    return data

#function to filter the dictionary
def dict_filter(dictionary, devices_f, not_working_devices_f):
    for item in dictionary:
        #to resolve the task we need only the id and state of the device
        dev_id = item['id']
        dev_state = item['state']
        #devices_f - list of the working devices. We check this for duplicates
        if dev_id in devices_f and dev_state != 'DD':
            #check the current number of duplicates
            dev_number = devices_f[dev_id]
            new_dev_number = dev_number + 1
            #add the 1 to current number of duplicates
            devices_f[dev_id] = new_dev_number

        else:
            if dev_state == 'DD':
                #if the device sends the "DD" message, delete it from the working devices
                devices_f.pop(dev_id, None)
                #check for duplicates
                if dev_id not in not_working_devices_f:
                    not_working_devices_f.append(dev_id)
            elif dev_state == '02':
                #add the device to not working
                if dev_id in not_working_devices_f:
                    pass
                else:
                #the device is working, but it has no duplicates, so create a new instance
                    devices_f[dev_id] = 1
    return devices_f, not_working_devices_f


list_devices = []
log_to_dictionary("LogRead/app_2.log", list_devices)

devices = {}
not_working_devices = []
dict_filter(list_devices, devices, not_working_devices)

work_devices = len(devices)
notwork_devices = len(not_working_devices)

print(f'______Failed test {notwork_devices} devices______')
for device in not_working_devices:
    print(f'Device: {device} was removed')

print(f'______Success test {work_devices} devices______')
for device in devices:
    print(f'Device {device} sent {devices[device]} statuses')
