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
        if len(str(am_pm_minutes)) == 1:
            am_pm_minutes= '0'+str(am_pm_minutes)
    else:
        plus_hour_minutes_flag = 0
        am_pm_minutes =(int(start_minutes)+int(duration_minutes))
        if len(str(am_pm_minutes)) ==1 :
            am_pm_minutes= '0'+str(am_pm_minutes)
    
    #Hours
    if (int(start_hours)+int(duration_hours))-12 > 0: 
        am_pm_hours =((int(start_hours)+int(duration_hours))-12)+plus_hour_minutes_flag
    else:
        am_pm_hours =(int(start_hours)+int(duration_hours))+plus_hour_minutes_flag
    
    #AM PM
    hours_trivial_sum=int(start_hours)+int(duration_hours)+plus_hour_minutes_flag
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
        
    #Next Day
    next_day_check = 0 
    next_day_trivial_sum=0
    if am_pm_original_flag == 'AM':
        next_day_trivial_sum = int(start_hours)+int(duration_hours)+plus_hour_minutes_flag
    else:
        next_day_trivial_sum = (int(start_hours)+12)+int(duration_hours)+plus_hour_minutes_flag
    next_day_flag=0
    if int(next_day_trivial_sum/24) <1:
        next_day_flag=0
        next_day_text=0
    if int(next_day_trivial_sum/24) ==1:
        next_day_flag=1
        next_day_text ='(next day)'
    if int(next_day_trivial_sum/24) >1:
        next_day_flag = int(next_day_trivial_sum/24)
        next_day_text = f'{next_day_flag} days later'
    

    if next_day_flag == 0:
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}"
    else:
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final} {next_day_text}"
    

    return new_time
    #return new_time,am_pm_original_flag,start_fmt,start_hours,start_minutes,duration_hours,duration_minutes,am_pm_minutes,am_pm_hours,am_pm_flag,next_day_trivial_sum,next_day_flag
print((add_time('2:59 AM', '24:00')))
