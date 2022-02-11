import pyautogui as pg
import time
time.sleep(3)

for i in range(100): #replace 100 with any number of times you want to send message
    pg.write("Sorry!, won't happen again!") #We can add any message inside "..."
    pg.press('Enter')
