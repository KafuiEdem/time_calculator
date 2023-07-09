def add_time(start,duration, days=""):

    #geting the hours, minutes and AM/PM from start time
    general_start_time = start.split(":")
    start_time_hour = int(general_start_time[0])
    start_time_minute =int(general_start_time[1].split()[0])
    am_or_pm = (general_start_time[1].split()[1])

    #geting the minute, hours from the duration
    general_duration_time = duration.split(":")
    duration_hour = int(general_duration_time[0])
    duration_minute = int(general_duration_time[1])

    #converting start time into minutes
    start_hour = start_time_hour * 60 + start_time_minute

    #converting duraation time into  minutes
    star_duration = duration_hour * 60 + duration_minute

    #geting the total hour and minute
    hour = (start_hour + star_duration)//60
    minute = (star_duration + start_hour) % 60

    #getting the Am/Pm, number of days and the actual hour 
    period = am_or_pm
    number_of_days = round(hour/24)
    hour = hour % 24

    #coding the main logic of the project
    
    # if hour < 1 and minute < 59:
    #     period = "PM" if period == "AM" else "AM"

    if hour <12:
        period = "PM" if period == "PM" else "AM"

    elif hour ==12:
        period = "PM" if period == "AM" else "AM"
    
    elif hour >=13:
        hour -= 12
        period = "PM" if period == "AM" else "AM"
        print("NUMBER OF DAYS = ",number_of_days)



    new_time = f"{hour}:{minute:02d} {period}"

    #geting the days
    if number_of_days:
        days = days.lower().capitalize()
        if number_of_days ==1:
            new_time +=f", {days} (next day)"
        elif number_of_days > 1:
            new_time +=f", {days} ({number_of_days} days later)"

    
    return new_time

p = add_time("11:30 AM", "2:32", "Monday")

print(p)