import os
import string
import wikipedia, random, pyautogui, time
import re

alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


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

    print(
        f"\nYou are going to spam a random string with the length of {length} characters {amount} times with a {timer} second cooldown!\nBe sure to focus the window of your choice")

    countdown(5)
    print("\r", end='')
    print("Started!", end='', flush=True)

    for i in range(0, amount):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        pyautogui.typewrite(result_str)
        pyautogui.press('enter')
        time.sleep(float(timer))

    print("\r", end='')
    print("Done!", end='', flush=True)


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text: text = text.replace(".”", "”.")
    if "\"" in text: text = text.replace(".\"", "\".")
    if "!" in text: text = text.replace("!\"", "\"!")
    if "?" in text: text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


def wikispam():
    while True:
        selectedlang = input("Choose the language you want to spam using the UTF-8 Language Codes ex.English - en:\n")

        try:
            if selectedlang not in wikipedia.languages():
                if selectedlang != wikipedia.languages():
                    print(f"Your selected Language of {selectedlang} is not found. Try again!\n")
                continue
            break
        except:
            print("This is not a language code")
    print(f"You selected the language {selectedlang} for your Wikipedia page!")
    while True:
        timer = input("\nHow long do you want the time in between messages to be (sec)?\nChoose a number: ")

        try:
            float(timer)
            if float(timer) < -0.1:
                print("This is not a valid number!")
                continue
            break

        except ValueError:
            print("This is not a valid number!\n")

    print(
        f"\nYou opened a random wiki article with a timer of {timer} seconds!\nBe sure to focus the window of your "
        f"choice.\nStarting in:")

    try:
        wikipedia.set_lang(selectedlang)
        wikipage = wikipedia.random(1)
        wikiload = wikipedia.page(wikipage).content

        page = split_into_sentences(wikiload)

        countdown(5)

        print("\r", end='')
        print(f"Started!\nSpamming {wikipedia.page(wikipage).title}\n", end='', flush=True)
        float(timer)
        for word in page:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            time.sleep(float(timer))

        print("\r", end='')
        print("Done!", end='', flush=True)

    except wikipedia.DisambiguationError as e:
        s = random.choice(e.options)
        p = wikipedia.pages(s)


def restart():
    print("\n\nPress enter to restart")
    z = input()
    print("Restarting in:")

    countdown(5)
    print("\n" * 100)