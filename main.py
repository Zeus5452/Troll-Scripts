import os, pyautogui, time

arr = os.listdir('spamFiles')
print(arr)

y = input('Choose File: \n')
f = open(f"spamFiles\\{y}", 'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)