def add_time(start,duration, days=None):

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
    check_day = hour//24
    
   
    #getting the clock logic for 24 hours
    if hour <12:
        period = "PM" if period == "PM" else "AM"

    elif hour ==12:
        period = "PM" if period == "AM" else "AM"
        
    elif hour >=13:
        hour -= 12
        period = "PM" if period == "AM" else "AM"

    new_time = f"{hour}:{minute:02d} {period}"

    if days==None:
        if number_of_days ==0:
            new_time
        elif number_of_days ==1:
           new_time +=f" (next day)"
        else:
            new_time +=f" ({number_of_days} days later)"
    else:
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        start_day_index = days_of_week.index(days.capitalize())
        new_day_index = (start_day_index + number_of_days) % 7
        new_day = days_of_week[new_day_index]

        if number_of_days ==0:
            new_time +=f", {new_day}"
        elif number_of_days ==1:
            new_time +=f", {new_day} (next day)"
        else:
            new_time +=f", {new_day} ({number_of_days} days later)"
    return new_time


p = add_time("11:59 PM", "24:05", "Wednesday")

print(p)