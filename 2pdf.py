# -*- coding: utf-8 -*-
from pdf.pdfclass import Option
from textwrap import dedent
import os
import sys
import time
import random
import subprocess

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = (
    '\33[94m', '\033[91m',
    '\33[97m', '\33[93m',
    '\033[1;35m', '\033[1;32m',
    '\033[0m')

colors = [BLUE, RED, YELLOW, MAGENTA, GREEN]

def duplicate(list1, list2, objects, dictionary):
    for e in range(1, 5):
        print(f"Enter {list1[e]} <{list2[e]}>: ", end="")
        inp = input()
    objects.others(dictionary)

def advanceOption(objects):
    default = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in'
        }
    empty = []
    for l in range(5):
        print(dedent("""
            Enter {} <{}>: """.format(list(default.keys())[l],
                list(default.values())[l])), end="")
        inp = input()
        empty.append(inp)

        if inp == "":
            duplicate(list(default.keys()), list(default.values()), objects, default)
            stop()

    print(empty)
    entry = {
        list(default.keys())[0]: empty[0],
        list(default.keys())[1]: empty[1],
        list(default.keys())[2]: empty[2],
        list(default.keys())[3]: empty[3],
        list(default.keys())[4]: empty[4]
        }
    objects.others(entry)


def choose(index):
    lists = ["url", "file", "strings", "multi-urls", "others",]
    entry = input(f"Enter {lists[index - 1]} \
to convert[www.xxxx.com/https://xxxx.org]:>>> ")

    save = input("Save as:>>> ")
    test = Option(entry, save)

    if lists[index - 1] == "others":
        advanceOption(test)

    # animation line
    symbol = "."
    print(colors[random.randint(0, len(colors)) - 1])
    while len(symbol) < 10:
        clear()
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
        elif lists[index - 1] ==  "multi":
            pass
        else:
            pass
    except OSError:
        print('\033[91m' + "Wrong url, retry!!..." + '\033[0m')

    main()



def clear():
    if sys.platform == "linux" or sys.platform == "linux2":
        subprocess.call("clear", shell=True)
    else:
        subprocess.call("cls", shell=True)


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
    clear()
    print(RED + "Wrong Entry!! retry..." + END)
    main()


def main():
    print("SELECT OPTION TO CONVERT")
    lists = ["URL", "FILE", "STRINGS", "MULTI-URLs", "OTHERS", "Quit"]
    for i, l in enumerate(lists, start=1):
        print(f"{i}: {l}")

    try:
        enter = int(input("\nEnter Option:>>> "))

        time.sleep(1)
        if enter in (1, 2, 4, 5):
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

        elif str(enter) == "6":
            stop()

        else:
            retry()

    except ValueError:
        retry()


if __name__ == "__main__":
    if os.name == "posix":
        if os.getuid() == 0:
            print("Do not run this as ROOT!!")

        else:
            clear()
            try:
                time.sleep(1)
                main()

            except:
                stop()
    else:
        clear()
        try:
            time.sleep(1)
            main()
        except:
            stop()