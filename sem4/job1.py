import time

# Initialize variables
seconds = 0
paused = False

def reset():
    global seconds
    seconds = int(input("Enter the number of seconds for the countdown: "))

def start():
    global seconds, paused
    while seconds > 0:
        if not paused:
            print(seconds)
            seconds -= 1
            time.sleep(1)
        else:
            time.sleep(0.1)
    print("Countdown finished!")

def pause():
    global paused
    paused = True
    print("Countdown paused.")

def resume():
    global paused
    paused = False
    print("Countdown resumed.")

def stop():
    global seconds
    seconds = 0
    print("Countdown stopped.")

# Main loop
while True:
    choice = input("Enter 'start', 'reset', 'pause', 'resume' or 'stop': ")
    if choice == 'start':
        if seconds == 0:
            reset()
        start()
    elif choice == 'reset':
        reset()
    elif choice == 'pause':
        pause()
    elif choice == 'resume':
        resume()
    elif choice == 'stop':
        stop()
        break
    else:
        print("Invalid input. Please enter 'start', 'reset', 'pause', 'resume' or 'stop'.")