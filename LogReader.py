# 2021-11-15 13:36:11,423 - INFO - > 'WOLF;88;7cbb94;UU;-7664;'
# 2021-11-15 13:36:11,423 - DEBUG - Detect ec54a8
# 2021-11-15 13:36:11,913 - DEBUG - > 'BIG;77;D5FA3F;1;66;42;6160;1;2;46;5;0;0;141;1;-3474;1;DD;'
# 2021-11-15 13:36:11,913 - WARNING - > 'BAD;75;ec803d;8450;1;02;'

#
data = []
order = ["handler", 'numb1', "id", 'numb2', 'numb3', 'numb4', 'numb5', 'numb6', 'numb7', 'numb8', 'numb9', 'numb10',
         'numb11', 'numb12', 'numb13', 'numb14', 'numb15', 'state']

devices = {}
not_working_devices = []


def log_to_dictionary(filename):
    with open(filename) as f:
        for line in f:
            marker_left = line.find("'")
            marker_right = line.rfind("'")
            if marker_right != -1:
                line_without_date = line[marker_left + 1:marker_right - 1]
                content = line_without_date.split(";")
                content = [x.strip() for x in content]
                if len(content) > 6:
                    structure = {key: value for key, value in zip(order, content)}
                    data.append(structure)


def dict_filter(dictionary):
    for item in dictionary:
        dev_id = item['id']
        dev_state = item['state']

        if dev_id in devices and dev_state != 'DD':
            dev_number = devices[dev_id]
            new_dev_number = dev_number + 1
            devices[dev_id] = new_dev_number

        else:
            if dev_state == 'DD':
                devices.pop(dev_id, None)
                if dev_id not in not_working_devices:
                    not_working_devices.append(dev_id)
            elif dev_state == '02':
                if dev_id in not_working_devices:
                    pass
                else:
                    devices[dev_id] = 1



log_to_dictionary("app_2.log")
dict_filter(data)

work_devices =len(devices)
notwork_devices = len(not_working_devices)

print(f'______Failed test {notwork_devices} devices______')
for device in not_working_devices:
    print(f'Device: {device} was removed')

print(f'______Success test {work_devices} devices______')
for device in devices:
    #print(device,devices[device])
    print(f'Device {device} sent {devices[device]} statuses')
