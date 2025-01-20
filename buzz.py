import time
import winsound
import threading


alarm_stopped = threading.Event()

def play_sound():
    try:
        
        winsound.PlaySound('mixkit-morning-clock-alarm-1003', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sound: {e}")

def stop_sound():
    try:
        
        winsound.PlaySound(None, winsound.SND_PURGE)
    except Exception as e:
        print(f"Error stopping sound: {e}")

def handle_alarm():
    """
    Handles the alarm sound for 30 seconds, allowing the user to stop it.
    """
    print("Alarm is ringing! Type 'stop' to turn it off.")
   
    play_sound()

    
    def listen_for_stop():
        user_input = input("Enter 'stop' to turn off the alarm: ").strip().lower()
        if user_input == 'stop':
            stop_sound()
            alarm_stopped.set()  
            print("Alarm stopped manually!")

    
    input_thread = threading.Thread(target=listen_for_stop)
    input_thread.start()

   
    for _ in range(30):
        if alarm_stopped.is_set():
            break
        time.sleep(1)

    if not alarm_stopped.is_set():
        stop_sound()
        print("Alarm stopped automatically after 30 seconds.")
    input_thread.join()  
def countdown_timer(seconds, timer_number):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'Timer {timer_number}: {mins:02}:{secs:02}'
        print(timer, end='\r')  
        time.sleep(1)
        seconds -= 1
    
    print(f"\nTimer {timer_number}: Time's up! ⏰")
    handle_alarm()  
def multiple_countdowns():
    print("Welcome to the Beep or Buzz!! Countdown!")
    print("Enter countdown times in seconds (type 'd' to finish):")
    
    countdowns = []
    while True:
        user_input = input("Enter countdown time in seconds: ")
        if user_input.lower() == 'd':
            break
        try:
            countdowns.append(int(user_input))
        except ValueError:
            print("Please enter a valid number or type 'd' to finish.")
    
    print(f"\nYou have set {len(countdowns)} countdown(s): {countdowns}\n")
    
    for i, duration in enumerate(countdowns, start=1):
        print(f"Starting Timer {i} for {duration} seconds...")
        countdown_timer(duration, i)
        print(f"Timer {i} completed!\n")
        if i < len(countdowns):
            cont = input("Do you want to continue to the next timer? (y/n): ").lower()
            if cont != 'y':
                print("Exiting the countdown timers. Goodbye!")
                break

if __name__ == "__main__":
    multiple_countdowns()
