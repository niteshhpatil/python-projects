import pyautogui
import time

i = 0
while i < 10:
    img = pyautogui.screenshot()
    img.save("D:\Screenshot\img" + str(i) + ".png")
    i = i + 1
    time.sleep(2)
