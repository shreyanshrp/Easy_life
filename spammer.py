import pyautogui as pg
import time
time.sleep(3)

for i in range(100):
    pg.write('I made a spammer in Python!')
    pg.press('Enter')