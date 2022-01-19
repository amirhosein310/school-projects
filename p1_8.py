month_list=['فرودین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
month_duration=30
day = int(input('enter day number'))
if day <= month_duration:
    print(day,month_list[0])
if day > month_duration:
    month_num = day // month_duration
    day_num = day % month_duration
    if day_num == 0:
        day_num=30
        month_num=month_num-1
    print(month_list[month_num], day_num)
