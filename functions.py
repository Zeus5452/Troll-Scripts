import os, pyautogui, time
from filespam import *


def countdown(arg):
    for i in range(0, arg):
        print("\r", end='')
        print("%i" % int(arg - i), end='', flush=True)
        time.sleep(1)


def timechooser():
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


def restart():
    print("\n\nPress enter to restart")
    z = input()
    print("Restarting in:")

    countdown(15)
    print("\n" * 100)