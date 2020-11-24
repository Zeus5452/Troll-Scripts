import os, pyautogui, time

# OPEN FILE

arr = os.listdir('spamFiles')

print("Available files:\n")

for i in arr:
    print(f"- {i}")

while True:
    y = input('\nChoose File: ')

    if y not in arr:
        if y == "files":
            for i in arr:
                print(f"- {i}")

        if y != "files":
            print("Sorry, this file does not exist!\nType 'files' to see all available files.")
        continue
    break

# CHOOSE TIME

while True:
    timer = input("\nHow long do you want the time in between messages to be (sec)?\nChoose a number: ")

    try:
        float(timer)
        if float(timer) < -0.1:
            print("This is not a valid number!")
            continue
        break

    except ValueError:
        print("This is not a valid number!")

# OPENING

f = open(f"spamFiles\\{y}", 'r')

print(
    f"\nYou opened: {y} with a timer of {timer} seconds!\nBe sure to focus on the window of your choice.\nStarting in:")

x = 5
for i in range(0, x):
    time.sleep(1)
    print("\r", end='')
    print("%i" % int(x - i), end='', flush=True)

print("\r", end='')
print("Started!\n", end='', flush=True)


while True:
    continue
    break

countdown()
# SCRIPT

float(timer)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(float(timer))

print("\r", end='')
print("Done!\n", end='', flush=True)