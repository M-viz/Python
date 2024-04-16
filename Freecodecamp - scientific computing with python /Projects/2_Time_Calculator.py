# Function to add time to a given start time and return the final time
# Funzione per aggiungere del tempo a un'ora di inizio data e restituire l'orario finale
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

def add_time(start, duration, week_day=' '):    
    start_fmt=start.split()[0]
    start_hours=start_fmt.split(':')[0]
    start_minutes=start_fmt.split(':')[-1]

    duration_hours=duration.split(':')[0]
    duration_minutes=duration.split(':')[-1]

    am_pm_original_flag=start.split()[-1]
    am_pm_final=''

    # Flags for tracking additional hours and minutes
    # Bandiere per tenere traccia delle ore e dei minuti aggiuntivi
    plus_hour_minutes_flag=0
    am_pm_minutes=0
    am_pm_hours=0

    # Calculate additional minutes
    # Calcolo dei minuti aggiuntivi
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
        
    # Calculate AM/PM
    # Calcolo AM/PM
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
        
    # Calculate if the time crosses to the next day
    # Calcolo se l'ora passa al giorno successivo
    next_day_trivial_sum=0
    if am_pm_original_flag == 'AM':
        next_day_trivial_sum = int(start_hours)+int(duration_hours)+plus_hour_minutes_flag
    else:
        next_day_trivial_sum = (int(start_hours)+12)+int(duration_hours)+plus_hour_minutes_flag
    if int(next_day_trivial_sum/24) <1:
        next_day_flag=0
        next_day_text=0
    if int(next_day_trivial_sum/24) ==1:
        next_day_flag=1
        next_day_text ='(next day)'
    if int(next_day_trivial_sum/24) >1:
        next_day_flag = int(next_day_trivial_sum/24)
        next_day_text = f'({next_day_flag} days later)'
    

    # Calculate hours for the final time
    # Calcolo delle ore per l'orario finale

    if next_day_flag == 0:
        if (int(start_hours)+int(duration_hours))-12> 0: 
            am_pm_hours =((int(start_hours)+int(duration_hours))-12)+plus_hour_minutes_flag
        else:
            am_pm_hours =(int(start_hours)+int(duration_hours))+plus_hour_minutes_flag
    else:
        if (int(start_hours)+int(duration_hours))-12> 0: 
            half_day_num=(int(start_hours)+int(duration_hours)+plus_hour_minutes_flag)/12
            half_day_module = half_day_num % 1
            if half_day_module !=0:
                am_pm_hours= round(half_day_module*12)
            else:
                am_pm_hours=12 
        else:
            half_day_num=(int(start_hours)+int(duration_hours)+plus_hour_minutes_flag)/12
            half_day_module = half_day_num % 1
            am_pm_hours= round(half_day_module*12)
    
    # Calculate the week day
    # Calcolo del giorno della settimana
    week_day_flag=0
    if week_day!=' ':
        week_day_flag=1
    if week_day_flag == 1:
        week_day_normalized=week_day.lower()
        days_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        week_day_index= days_of_week.index(week_day_normalized)
        new_week_day_index=week_day_index+next_day_flag
        if new_week_day_index<=6:
            final_week_day=days_of_week[new_week_day_index].capitalize()
        else:
            new_week_day_index_num=new_week_day_index /7 
            if new_week_day_index_num== 0: 
                final_week_day=days_of_week[0].capitalize()
            else:
                new_week_day_index= round((new_week_day_index_num %1)*7)
                final_week_day=days_of_week[new_week_day_index].capitalize()

    # Finalize the time format to return
    # Formattazione finale dell'ora da restituire    
    if next_day_flag == 0 and week_day==' ':
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}"
    if next_day_flag == 0 and week_day!=' ':
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}, {week_day_normalized.capitalize()}"
    if next_day_flag != 0 and week_day==' ': 
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final} {next_day_text}"
    if next_day_flag != 0 and week_day!=' ':
        new_time=f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}, {final_week_day} {next_day_text}"

    # Coincise way provided by ChatGPT:
        # new_time = f"{am_pm_hours}:{am_pm_minutes} {am_pm_final}" + (f", {next_day_text}" if next_day_flag != 0 else "") + (f", {week_day_normalized.capitalize()}" if next_day_flag == 0 and week_day != ' ' else "")

    # Return the final time
    # Restituzione dell'orario finale       
    return new_time

# Example usage of the function
# Esempio di utilizzo della funzione
print((add_time('8:16 PM', '466:02', 'tuesday')))
