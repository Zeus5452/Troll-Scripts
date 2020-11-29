import os, pyautogui, time
from func import *



while True:
    print("Pick your spam tool here!\npick from:")
    print("1. Filespam - Spams everything word for word in a certain txt file")
    print("2. Random string spam - Spams a random string")
    print("3. Wikispam - Spams a random wikipedia article")
    print("4. Stringspam - Spams a inputted string")

    f = input("\nType the corresponding number to the option you want to pick\n> ")

    if f == str(1):
        print("\nYou picked: Filespam!\n\n")
        filespam()
        restart()

    if f == str(2):
        print("\nYou picked: Random string!\n\n")
        randomstring()
        restart()

    if f == str(3):
        print("\nYou picked: Wikispam!\n\n")
        wikispam()
        restart()

    if f == str(4):
        print("\nYou picked: String Spammer!\n\n")
        stringspammer()
        restart()



