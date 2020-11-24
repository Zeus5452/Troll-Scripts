import os, pyautogui, time
from functions import *


def filespam():
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

    timechooser()

    # OPENING

    f = open(f"spamFiles\\{y}", 'r')

    print(
        f"\nYou opened: {y} with a timer of {timer} seconds!\nBe sure to focus on the window of your choice.\nStarting in:")

    countdown(5)
    print("\r", end='')
    print("Started!", end='', flush=True)

    # SCRIPT

    float(timer)
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(float(timer))

    print("\r", end='')
    print("Done!", end='', flush=True)