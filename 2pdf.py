# -*- coding: utf-8 -*-
from pdfclass import Option
from textwrap import dedent
import os
import time
import random

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = (
    '\33[94m', '\033[91m',
    '\33[97m', '\33[93m',
    '\033[1;35m', '\033[1;32m',
    '\033[0m')

colors = [BLUE, RED, YELLOW, MAGENTA, GREEN]


def choose(index):
    lists = ["url", "file", "string", "multi"]
    entry = input(f"Enter {lists[index - 1]} to \
convert[www.xxxx.com/https://xxxx.org]:>>> ")

    save = input("Save as:>>> ")
    test = Option(entry, save)
    # animation line
    symbol = "."
    print(colors[random.randint(0, len(colors)) - 1])
    while len(symbol) < 10:
        os.system("clear")
        # loading admin input form/session
        print(
            colors[random.randint(0, len(colors)) - 1]
            + "[!]" + END
            + f" A moment, converting {lists[index - 1]} ", end="")
        print(symbol)
        time.sleep(1)
        symbol = symbol + "."

    # testing condition on objects
    try:
        if lists[index - 1] == "url":
            test.url()
        elif lists[index - 1] == "file":
            test.files()
        elif lists[index - 1] == "multi":
            pass
        else:
            pass
    except OSError:
        print('\033[91m' + "Wrong url, retry!!..." + '\033[0m')

    main()


def clear():
    os.system("clear")


def stop():
    try:
        choose = input(
            f"\nDo you want to abort? Type {RED}[y]{END} to quit or \
{YELLOW}[n]{END} to cancel >> ")

        if choose == "y":
            print(colors[random.randint(0, len(colors)-1)])
            print("\nThanks alot for using this app" + END)
            print(random.choice(colors) + dedent("""
             ██████╗           ██████╗  ██████╗  ███████╗
             ╚════██╗          ██╔══██╗ ██╔══██╗ ██╔════╝
              █████╔╝   █████╗ ██████╔╝ ██║  ██║ █████╗
             ██╔═══╝    ╚════╝ ██╔═══╝  ██║  ██║ ██╔══╝
             ███████╗          ██║      ██████╔╝ ██║
             ╚══════╝          ╚═╝      ╚═════╝  ╚═╝
            """ + END))
            exit(1)

        elif choose == "n":
            clear()
            main()

        elif choose == "":
            print("Enter something!")
            stop()

        else:
            print(
                colors[random.randint(0, len(colors)-1)]
                + "Entered wrong input!!" + END)
            stop()

    # suppressing internal interruption
    except KeyboardInterrupt:
        stop()

    # quietly dealing with internal "Exit On File Error"
    # alias Ctrl^D :) by calling the stop() function
    except EOFError:
        stop()


def retry():
    os.system("clear")
    print(RED + "Wrong Entry!! retry..." + END)
    main()


def main():

    print(dedent("""
            SELECT OPTION TO CONVERT
            [1] URL
            [2] FILE
            [3] STRINGS
            [4] MULTIPLE CHOICE
            [5] Quit"""))

    try:
        enter = int(input("\nEnter Option:>>> "))

        time.sleep(1)
        if enter in (1, 2, 4):
            choose(enter)

        elif enter == 3:
            print("Enter as many lines of text as you want.")
            print("When you're done, enter a single period on a line to quit.")

            buffer = []
            while True:
                print("> ", end="")
                line = input()
                if line == ".":
                    break
                buffer.append(line)
            entry = "\n".join(buffer)
            save = input("Save text as:>>> ")
            test = Option(entry, save)
            test.string()

        elif str(enter) == "5":
            stop()

        else:
            retry()

    except ValueError:
        retry()


if __name__ == "__main__":
    if os.getuid() == 0:
        print("Do not run this as ROOT!!")

    else:
        clear()
        try:
            time.sleep(1)
            main()

        except KeyboardInterrupt:
            stop()

        except EOFError:
            stop()
