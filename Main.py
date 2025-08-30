import pyautogui
import keyboard
import time
import ctypes

running = True

last_position = None
still_time = 0

def stop_program(event):
    global running
    running = False

def move(event):
    global saved_position
    pyautogui.moveTo(saved_position)
    print("moved")

keyboard.on_press_key("esc", stop_program)
keyboard.on_press_key("F5", move)

while running:
    current_position = pyautogui.position()

    print(f"\rmouse: {current_position}", end='')

    if current_position == last_position:
        still_time += 0.1
        if still_time >= 1.0:
            saved_position = current_position
            print(" | ", saved_position)
            still_time = 0
    else:
        still_time = 0

    last_position = current_position
    time.sleep(0.1)
