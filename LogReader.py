# 2021-11-15 13:36:11,423 - INFO - > 'WOLF;88;7cbb94;UU;-7664;'
# 2021-11-15 13:36:11,423 - DEBUG - Detect ec54a8
# 2021-11-15 13:36:11,913 - DEBUG - > 'BIG;77;D5FA3F;1;66;42;6160;1;2;46;5;0;0;141;1;-3474;1;DD;'
# 2021-11-15 13:36:11,913 - WARNING - > 'BAD;75;ec803d;8450;1;02;'


working_ids = []
notWorking_ids = []

with open("app_2.log") as f:
    count = 0
    for line in f:
        marker = line.find("'")
        line_without_date = line[marker:]








        new_line =1
        print(marker)

        print(line_without_date)
        pass




    print(count)
    print(notWorking_ids)
