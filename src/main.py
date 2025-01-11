import ctypes
import pyautogui
import keyboard

# Set the custom window name for Task Manager
def set_process_name(name):
    ctypes.windll.kernel32.SetConsoleTitleW(name)

# Custom names
set_process_name("KeyboardRebind")

def on_f6_pressed():
    pyautogui.press("w")

def on_f12_pressed():
    pyautogui.press("right")

# Register hotkeys
keyboard.add_hotkey('F6', on_f6_pressed, args=(), suppress=True)
keyboard.add_hotkey('F12', on_f12_pressed, args=(), suppress=True)

print("Press F6 to send 'W' and F12 to send 'Left Arrow'. Press Ctrl+C to exit.")

# Keep the program running to listen for key presses
keyboard.wait()
