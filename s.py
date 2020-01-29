import pyautogui
import time

x=1
while x>0:
 pyautogui.click()
 pyautogui.screenshot('/Users/laluheri/image'+str(x)+'.png')
 x+=1
 time.sleep(2)

