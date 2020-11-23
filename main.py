import os, pyautogui, time

arr = os.listdir('spamFiles')

print("Available files:\n")

for i in arr:
    print(f"- {i}")

while True:
    y = input('\nChoose File: \n')



    if y not in arr:
        if y == "files":
            for i in arr:
                print(f"- {i}")


        if y != "files":
            print("Sorry, this file does not exist!\nType 'files' to see all available files.")
        continue
    break

f = open(f"spamFiles\\{y}", 'r')

print(f"\nYou opened: {y}!\nBe sure to focus on the window of your choice.\nStarting in:")

x = 5
for i in range(0, x):
    time.sleep(1)
    print("\r", end='')
    print("%i" % int(x - i), end='', flush=True)

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)
