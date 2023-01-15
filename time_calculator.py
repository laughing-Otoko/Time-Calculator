def add_time(start, duration, days = False):
  
    start_time = start.split()
    current_time = start_time[0].split(":")
    day_time = start_time[1]

    if day_time == "PM":
        if current_time[0] != "12": 
            int_current_time_hour = int(current_time[0])
            int_current_time_hour += 12
            current_time[0] = str(int_current_time_hour)

    if day_time == "AM" and current_time[0] == "12": 
        current_time[0] = "00"
    time_to_add = duration.split(":")

    sum_of_mins = int(time_to_add[1]) + int(current_time[1])

    if sum_of_mins >= 60:
        diff_of_min = sum_of_mins - 60
        minutes = diff_of_min
        hrs = 1
    else:
        minutes = sum_of_mins
        hrs = 0

    sum_of_hrs = int(time_to_add[0]) + int(current_time[0]) + hrs
    if sum_of_hrs >= 24:
        int_xdays = sum_of_hrs // 24
        hour = sum_of_hrs - 24 * int_xdays
    else:
        hour = sum_of_hrs
        int_xdays = 0

    if days != False:
        days = days.lower()
        if days == "monday":
            fweekday = 1
        elif days == "tuesday":
            fweekday = 2
        elif days == "wednesday":
            fweekday = 3
        elif days == "thursday":
            fweekday = 4
        elif days == "friday":
            fweekday = 5
        elif days == "saturday":
            fweekday = 6
        elif days == "sunday":
            fweekday = 7

        no_of_weekday = (fweekday + int_xdays) % 7

        if no_of_weekday == 1:
            weekday = "Monday"
        elif no_of_weekday == 2:
            weekday = "Tuesday"
        elif no_of_weekday == 3:
            weekday = "Wednesday"
        elif no_of_weekday == 4:
            weekday = "Thursday"
        elif no_of_weekday == 5:
            weekday = "Friday"
        elif no_of_weekday == 6:
            weekday = "Saturday"
        elif no_of_weekday == 0:
            weekday = "Sunday"

    if hour >= 12:
        rest = 24 - hour
        hour = 12 - rest
        time_of_day = "PM"

        if hour == 12: 
            time_of_day = "AM"
        if hour == 0:  
            hour = 12

    else:
        time_of_day= "AM"
        if hour == 0: 
            hour = 12

   
    def timeNumberFormat(n) :
        if n < 10:
            return "0{}".format(n)
        else:
            return "{}".format(n)
    final_hour = str(hour)

    if minutes < 10:
      final_minutes = "0{}".format(minutes)
    else:
      final_minutes = "{}".format(minutes)
      
    final_xdays = str(int_xdays)

    #print

    if int_xdays == 0:
        if days == False:
            new_time = final_hour+":"+final_minutes+" "+time_of_day
        else:
            new_time = final_hour + ":" + final_minutes + " " + time_of_day+", "+weekday
    else:
        if days == False:
          if int_xdays == 1:
            new_time = final_hour+":"+final_minutes+" "+time_of_day+" (next day)"
          else:
            new_time = final_hour+":"+final_minutes+" "+time_of_day+" ("+final_xdays+" days later)"
        else:
          if int_xdays == 1:
             new_time = final_hour + ":" + final_minutes + " " + time_of_day + ", " + weekday+ " (next day)"
          else:
             new_time = final_hour + ":" + final_minutes + " " + time_of_day + ", " + weekday+ " (" +final_xdays + " days later)"

    return new_time
