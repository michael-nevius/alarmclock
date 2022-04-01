class AlarmClock:
    def __init__(self, current, alarm_toggle, display):
        self.current = current
        self.alarmtoggle = alarm_toggle
        self.display = display
    
    def set_time(self):
        self.current = input(f'Please set your current time in this format, "HH:MM": ')
    
    def display_time(self):
        print(f"The current time is {self.current} ")
    
    def toggle_alarm(self):
        self.alarmtoggle = alarm_toggle
        alarm_toggle = input('Would you like to set an alarm? Please type "y" or "n": ')
        if alarm_toggle == "y":
            input('Please type the the time you want your alarm to go off. Use this format, "HH:MM": ')
            
        else:
            alarm_toggle == "n"
            print("No alarm has been set")

        
