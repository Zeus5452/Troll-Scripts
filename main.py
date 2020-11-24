import os, pyautogui, time
from functions import *
from filespam import *


while True:
    print("Pick your spam tool here!\npick from:")
    print("1. Filespam - Spams everything word for word in a certain txt file")

    f = input("\nType the corresponding number to the option you want to pick\n> ")

    if f == str(1):
        print("\nYou picked: Filespam!\n\n")
        filespam()
        restart()





