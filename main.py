import pyautogui
import random
import time

while True:
    x = random.randint(300, 500)
    y = random.randint(90, 600)
    pyautogui.moveTo(x, y, 0.5)
    time.sleep(random.random() * 2)
