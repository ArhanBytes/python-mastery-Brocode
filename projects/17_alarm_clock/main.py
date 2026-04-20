# Alarm Clock
import time
import datetime
import pygame # working with sound effect

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "projects/17_alarm_clock/chicken-on-tree-screaming.mp3"

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UPPPPPP!")
            
            pygame.mixer.init() # library-> module -> function
            pygame.mixer.music.load(sound_file) # library->module->class->method
            pygame.mixer.music.play() #library->module->class->method
            
            # jab tak song khatam na ho tab tk chalao
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)