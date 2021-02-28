# Import relevant modules
import time
import pyautogui

time.sleep(5)  # Python file sleeps for 5 seconds
text = open("text.txt")  # Opening the text file
for each_line in text:
    pyautogui.typewrite(each_line)  # Typewriting the file!
