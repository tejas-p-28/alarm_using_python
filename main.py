from datetime import datetime
#from playsound import playsound
import winsound

alarm_date = input("Enter the date on which you want to set the alarm:").strip()
alarm_time = "".join(input("Enter the time on which you want to set alarm in HH:MM,AM/PM format: ").split())
music_or_beep = input("enter for a music or a beep: ")
if music_or_beep == "b":
    dur = int(input("Enter your duration in seconds: "))*1000 #coz seconds are count in miliseconds
    freq = int(input("Enter the frequency of the sound(optimum= 500)"))
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[6:8].upper()

print("the alarm is being set.....")


while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime("%M")
    current_period = current_time.strftime("%p")
    current_date = current_time.strftime("%d")
    if current_date == alarm_date and current_period == alarm_period and current_hour == alarm_hour and current_minute == alarm_minute:
        print("*"*10)
        print("| " + "Wake Up" + " |")
        print("*"*10)
        if music_or_beep == "m":
            #playsound("Applications_Alarm_audio.wav")
            print("alarm is set")
        else:
            winsound.Beep(freq, dur)
            break