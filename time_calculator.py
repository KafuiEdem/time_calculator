def add_time(start, duration,days=""):

    #getting the starting and ending time
    start_time = start.replace("PM","").replace("AM","").strip().split(":")
    end_time = duration.replace("PM","").replace("AM","").strip().split(":")
    zones = ["AM","PM"]
    #adding the hours
    hour = int(start_time[0]) + int(end_time[0])

    #adding the minutes
    minute = int(start_time[1]) + int(end_time[1])

    #check if the minute is more than 60 or equals to 60
    if minute == 60:
        minute = f"{minute - 60}0"
    elif minute > 60:
        minute = minute - 60
        if minute <10:
            minute = f"0{minute}"
        hour += 1
   
    #checking for the time zone
    for zone in zones:
        if zone in start:
            if hour >=12:
                hour -=12
                if hour <10:
                    new_time = f"0{hour}:0{minute} AM"
                else:
                    new_time = f"{hour}:{minute} PM"
            elif hour <=12:
                new_time = f"{hour}:{minute} {zone}"

       

    return new_time


p = add_time("10:10 PM", "3:30")

print(p)