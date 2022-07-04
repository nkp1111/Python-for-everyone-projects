
def add_time(start, duration, weekday=None):
    answer = []
    weeks = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    pos_s, pos_d = start.find(":"), duration.find(":")
    start = [start[:pos_s], start[pos_s + 1:]]
    duration = [duration[:pos_d], duration[pos_d + 1:]]
    start_value = start[1].split()
    start.pop()
    
    for i in range(2):
        start.append(start_value[i])
    hour = int(start[0]) + int(duration[0])
    minute = int(start[1]) + int(duration[1])
    am_pm = start[2]
    day = 0
    
    if minute >= 60:
        minute -= 60
        hour += 1
        
    while hour >= 12:
        if am_pm == "PM":
            am_pm = "AM"
            day += 1
        else:
            am_pm = "PM"

        if hour > 12:
            hour -= 12
        elif hour == 12:
            break

    for i in [hour, minute, am_pm]:
        answer.append(str(i))
        
    if weekday is not None:
        week_num = weeks.index(weekday.lower())
        week_num += day
        
        if week_num > 6:
            week_num = week_num % 7
            
        weekday = weeks[week_num]
        answer.append(weekday)

    if day == 1:
        answer.append("(next day)")
    else:
        answer.append(f"({day} days later)")

    new_time = answer[0] + ":" + answer[1].rjust(2, "0") + " " + answer[2]
    if weekday is None and day == 0:
        return new_time
    elif weekday and day == 0:
        new_time += ", " + answer[-2].capitalize()
        return new_time
    elif weekday is None and day > 0:
        new_time += " " + answer[-1]
        return new_time
    else:
        new_time += ", " + answer[-2].capitalize() + " " + answer[-1]
        return new_time 
      
print(add_time("11:06 AM", "52:02", "tuesday"))
