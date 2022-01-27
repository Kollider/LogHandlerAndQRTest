# 2021-11-15 13:36:11,423 - INFO - > 'WOLF;88;7cbb94;UU;-7664;'
# 2021-11-15 13:36:11,423 - DEBUG - Detect ec54a8
# 2021-11-15 13:36:11,913 - DEBUG - > 'BIG;77;D5FA3F;1;66;42;6160;1;2;46;5;0;0;141;1;-3474;1;DD;'
# 2021-11-15 13:36:11,913 - WARNING - > 'BAD;75;ec803d;8450;1;02;'
import json

working_ids = []
notWorking_ids = []

data = []
order_1 = ["handler", 'numb1', "id", 'numb2', 'numb3', 'numb4', 'numb5', 'numb6', 'numb7', 'numb8', 'numb9', 'numb10',
           'numb11', 'numb12', 'numb13', 'numb14', 'numb15', 'state']

order_2 = ["handler", 'numb1', "id", 'numb5', 'numb16', 'state']

with open("app_2.log") as f:
    file_for_logs = open("demofile2.txt", "w")
    count = 0
    new_count = 0
    for line in f:
        marker_left = line.find("'")
        marker_right = line.rfind("'")

        if marker_right and marker_left != -1:
            line_without_date = line[marker_left + 1:marker_right - 1]

            content = line_without_date.split(";")
            if len(content) > 6:
                structure = {key: value for key, value in zip(order_1, content)}
                data.append(structure)


                new_line = 1
                print(marker_left, marker_right)


                content=[x.strip() for x in content]



                new_count += 1


                pass
        count += 1

    print(count)
    print(new_count)
    print(notWorking_ids)
    for entry in data:
        file_for_logs.write(json.dumps(entry, indent = 4) + '\n')


    file_for_logs.close()