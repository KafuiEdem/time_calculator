def add_time(start, duration,days=""):

    #getting the starting and ending time
    start_time = start.replace("PM","").replace("AM","").strip().split(":")
    end_time = duration.split(":")
    zones = ["AM","PM"]
    new_time =''
    #check the number of days
    
    #adding the hours
    hour = int(start_time[0]) + int(end_time[0])

    #adding the minutes
    minute = int(start_time[1]) + int(end_time[1])
    for zone in zones:
        num_days = ""
        num = ""
        if num_days:
            if num_days ==1:
                num = f"(next day)"
            elif num_days >1:
                num = f"({num_days} days later)"
        if zone in start:
            #building the 12 hour clock
            if hour ==0 and minute <=59:
                if days =="":
                    new_time += f"{hour + 12}:{minute} {zones[0]}"
                else:
                    new_time += f"{hour + 12}:{minute} {zones[0]}, {days.capitalize()}"

            elif hour >= 1 and hour <=11 and minute <=59:
                if days == "":
                    if minute <10:
                        new_time += f"{hour}:{minute:02d} {zone}"
                    else:
                        new_time += f"{hour}:{minute} {zones[1]}"
                else:
                    if minute <10:
                        new_time += f"{hour}:{minute:02d} {zone}"
                    else:
                        new_time += f"{hour}:{minute} {zones[1]}, {days.capitalize()}"
                    
            elif hour <=1 or hour >= 11 and minute ==0:
                if days =="":
                    new_time += f"{hour}:{minute} {zones[0]}"
                else:
                    new_time += f"{hour}:{minute} {zones[0]}, {days.capitalize()}"
        
            elif hour ==1 or (hour <=11 and minute > 59):
                minute_to_hour = minute/60 #getting hour from minutes
                new_minute = round(minute_to_hour -1,2) #getting new minute in two decimal
                add_hr = str(float(hour)+minute_to_hour).split(".") #adding the hours to get complete hours
                new_minute = round(float(new_minute)*60)
                if days == "":
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[1]}"
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[0]}"
                else:
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[1]}, {days.capitalize()}"
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[0]}, {days.capitalize()}"


            elif hour ==12 and 0 <= minute <= 59:
                if days =="":
                    new_time += f"{hour}:{minute} {zones[1]}"
                else:
                    new_time += f"{hour}:{minute} {zones[1]}, {days.capitalize()}"
                
            elif hour ==13 and (hour <=23 and minute <= 59):
                num_days = round(int(hour)/24)
                if days == "" and num_days>0 or num_days==1:
                    new_time += f"{hour -12}:{minute} {zones[1]} {num}"
                else:
                    new_time += f"{hour -12}:{minute} {zones[1]}, {days.capitalize()} {num}"

            elif hour ==13 or (hour <=23 and minute >59):
                minute_to_hour = minute/60 #getting hour from minutes
                new_minute = round(minute_to_hour -1,2) #getting new minute in two decimal
                new_hour = hour + new_minute
                add_hr = str(float(new_hour-12)+minute_to_hour).split(".") #adding the hours to get complete hours
                new_minute = round(float(new_minute)*60)
                if days == "":
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[1]} {num} "
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[0]} {num}"
                else:
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[1]}, {days.capitalize()} {num}"
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[0]}, {days.capitalize()} {num}"

            elif hour >= 24 and minute > 59:
                minute_to_hour = minute/60 #getting hour from minutes
                new_minute = round(minute_to_hour -1,2) #getting new minute in two decimal
                new_hour = hour -24 #getting my new hours
                add_hr = str(float(new_hour)+minute_to_hour).split(".") #adding the hours to get complete hours
                new_minute = round(float(new_minute)*60)

                #checking for the number of days
                num_days = round(int(hour+minute_to_hour)/24)

                if days == "" and num_days==1 or num_days>2:
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[0]} {num}"
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[1]} {num}"
                else:
                    if new_minute <10:
                        new_time +=f"{add_hr[0]}:{new_minute:02d} {zones[0]}, {days.capitalize()} {num}"
                    else:
                        new_time +=f"{add_hr[0]}:{new_minute} {zones[1]}, {days.capitalize()} {num}"

        
                print(num_days)

                print("Days ", num)
    return new_time


p = add_time("10:10 PM", "3:30")

print(p)