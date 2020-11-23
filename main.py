import pyautogui, time
f = open('beemovie', 'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)