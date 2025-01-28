import time
from datetime import datetime

def alarm(alarm_time, message="Time's up!"):
    print(f"Alarm set for {alarm_time}...")
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("\n⏰ Alarm! " + message)
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    message = input("Enter a custom alarm message (optional): ") or "Wake up!"
    alarm(alarm_time, message)
