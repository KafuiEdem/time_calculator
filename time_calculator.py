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

    #constants
    MINUTE_DAY = 24*60

    #checking for time provided and convert it into 24 hours
    if am_or_pm=="PM":
        start_time_hour +=12

    #converting start time into minutes
    start_hour_in_minute = start_time_hour * 60 + start_time_minute 

    #converting duraation time into  minutes
    start_duration_in_minute = duration_hour * 60 + duration_minute

    #geting the total time in minute
    total_time_in_minute = start_hour_in_minute + start_duration_in_minute
    
    #getting the number of days
    number_of_days = total_time_in_minute//MINUTE_DAY

    #getting the actual hours and minute
    minute_left = total_time_in_minute % MINUTE_DAY
    hour = minute_left // 60
    minute = minute_left % 60
    period = am_or_pm

    #getting the Am/Pm, number of days and the actual hour 

    if hour < 12:
         if hour ==0:
             hour +=12
         period = "AM" 
        
    elif hour ==12:
        period = "PM" 

    elif hour >=13:
        hour -=12
        period = "PM" 
    
    new_time = f"{hour}:{minute:02d} {period}"

    #checking the days and updating the final touch of my code.
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
   