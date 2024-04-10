def add_time(start, duration):
    
    start_fmt=start.split()[0]
    start_hours=start_fmt.split(':')[0]
    start_minutes=start_fmt.split(':')[-1]

    duration_hours=duration.split(':')[0]
    duration_minutes=duration.split(':')[-1]

    am_pm_original_flag=start.split()[-1]
    am_pm_final=''

    plus_hour_minutes_flag=0
    plus_hour_hours_flag=0
    am_pm_minutes=0
    am_pm_hours=0

    #Minutes
    if (int(start_minutes)+int(duration_minutes))-60 > 0: 
        plus_hour_minutes_flag = 1
        am_pm_minutes =((int(start_minutes)+int(duration_minutes))-60)
    else:
        plus_hour_minutes_flag = 0
        am_pm_minutes =(int(start_minutes)+int(duration_minutes))
    
    #Hours
    if (int(start_hours)+int(duration_hours))-12 > 0: 
        am_pm_hours =((int(start_hours)+int(duration_hours))-12)+plus_hour_minutes_flag
    else:
        am_pm_hours =(int(start_hours)+int(duration_hours))+plus_hour_minutes_flag
    
    #AM PM
    hours_trivial_sum=int(start_hours)+int(duration_hours)
    am_pm_flag=int(hours_trivial_sum/12)
    if am_pm_original_flag =='AM':
        if am_pm_flag == 0 or am_pm_flag%2 ==0:
            am_pm_final = am_pm_original_flag
        else:
            am_pm_final = 'PM'
    if am_pm_original_flag =='PM':
        if am_pm_flag == 0 or am_pm_flag%2 ==0:
            am_pm_final = am_pm_original_flag
        else:
            am_pm_final = 'AM'
        
    


    new_totalhour=int(start_hours)+int(duration_hours)
    new_totalminutes=int(start_minutes)+int(duration_minutes)    
    
    new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}"

    return new_time
    #return new_time,am_pm_original_flag,start_fmt,start_hours,start_minutes,duration_hours,duration_minutes,am_pm_minutes,am_pm_hours,am_pm_flag
print(add_time('12:30 PM', '9:32'))