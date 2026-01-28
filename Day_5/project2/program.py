import pyautogui
import pyperclip
import time

# Small pause so you can switch to the target app
time.sleep(3)

# Click the icon
pyautogui.click(919, 1067)
time.sleep(0.3)

# Drag to select text
pyautogui.moveTo(323, 221)
pyautogui.dragTo(1096, 982, duration=0.5, button='left')
time.sleep(0.2)

# Copy (Cmd + C on macOS)
pyautogui.hotkey('command', 'c')
time.sleep(0.2)
pyautogui.click(1066, 1003)  # Click to defocus

# Get clipboard content
copied_text = pyperclip.paste()

# Now it's stored in a variable
print("Copied text:")
print(copied_text)
