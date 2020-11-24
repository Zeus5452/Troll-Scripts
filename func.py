import os, pyautogui, time, random, string


def countdown(arg):
    for i in range(0, arg):
        print("\r", end='')
        print("%i" % int(arg - i), end='', flush=True)
        time.sleep(1)


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
        f"\nYou opened: {y} with a timer of {timer} seconds!\nBe sure to focus the window of your "
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


def randomstring():
    while True:
        try:
            amount = int(input("\nHow many times does a random string have to get spammed?\nChoose a number: "))
        except ValueError:
            print("This is not a valid number!")
            continue
        break

    while True:
        try:
            length = int(input("\nHow long does the string need to be?\nChoose a number: "))
        except ValueError:
            print("This is not a valid number!")
            continue
        break

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

    print(f"\nYou are going to spam a random string with the length of {length} characters {amount} times with a {timer} second cooldown!\nBe sure to focus the window of your choice")

    countdown(5)
    print("\r", end='')
    print("Started!", end='', flush=True)

    for i in range(0,amount):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        pyautogui.typewrite(result_str)
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