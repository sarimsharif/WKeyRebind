import pyautogui
import keyboard

# Define the rebind functionality
def rebind_f6_to_w():
    while True:
        # Check if F6 is pressed
        if keyboard.is_pressed("F6"):
            # Simulate pressing 'W'
            pyautogui.press("w")

            # Prevent holding the key too long
            while keyboard.is_pressed("F6"):
                pass  # Wait for the key to be released


# Run the rebind function
if __name__ == "__main__":
    print("Press F6 to send 'W'. Press Ctrl+C to exit.")
    try:
        rebind_f6_to_w()
    except KeyboardInterrupt:
        print("Rebind program stopped.")
