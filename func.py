import os, pyautogui, time


def countdown(arg):
    for i in range(0, arg):
        print("\r", end='')
        print("%i" % int(arg - i), end='', flush=True)
        time.sleep(1)


def picktime():
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


def filespam():
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
        f"\nYou opened: {y} with a timer of {timer} seconds!\nBe sure to focus on the window of your "
        f"choice.\nStarting in:")

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


def restart():
    print("\n\nPress enter to restart")
    z = input()
    print("Restarting in:")

    countdown(15)
    print("\n" * 100)