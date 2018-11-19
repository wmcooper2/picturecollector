#!/usr/bin/env python3
"""Take a picture with the attached usb webcam.

    - increments the file name by one each time
    - saves as grayscale png
    - remembers the state of the counter between sessions

"""

#stand lib
import json
from pathlib import Path
import subprocess

answer = None
counter = None
file_ = "cameracounter.json"
PIC_DIR = "./webcam/"

def load_counter():
    """Loads the counter value. Returns Integer."""
    with open(file_, "r") as file_obj:
        #counter = int(json.load(file_obj))
        return int(json.load(file_obj))

def save_counter(file_, counter):
    """Saves the counter value. Returns None."""
    with open(file_, "w+") as file_obj:
        json.dump(counter, file_obj)

def resetcounter():
    """Resets the counter. Returns None."""
    global counter
    global file_
    counter = 0
    save_counter(file_, "0")

def pi_reboot():
    """Reboots the pi. Returns None."""
    subprocess.Popen("sudo reboot", shell=True)

def pi_shutdown():
    """Shutsdown the pi. Returns None."""
    subprocess.Popen("sudo shutdown -h now", shell=True)

def takepic():
    """Takes a picture. Returns None."""
    global counter
    subprocess.run(["./takepicture", str(counter)])
    counter += 1

def deleteall():
    """Deletes all pictures from PIC_DIR. Returns None.'"""
    pass

def picdir():
    """Shows the save directory for the pictures. Returns None."""
    print(PIC_DIR)

def countpics():
    """Counts the pictures in the save directory. Returns Integer."""
    global PIC_DIR
    print("Picture count:: ", str(sum(1 for pic in Path(PIC_DIR).iterdir())))

def newline():
    print("\n")

def _help():
    """Shows commands available. Returns None."""
    newline()
    print("HELP COMMANDS")
    print("(enter): takes a picture.")
    print("help: prints this list.")
    print("reboot: duh...")
    print("shutdown: duh...")
    print("picdir: shows the save directory.")
    print("deleteall: deletes all the pictures in the save directory.")
    print("resetcounter: resets the counter used for the save file name.")
    print("countpics: counts the pictures in the save directory.")
    newline()

commands = {
        "reboot":pi_reboot,
        "\n":takepic,
        "picdir":picdir,
        "deleteall":deleteall,
        "help":_help,
        "resetcounter":resetcounter,
        "countpics":countpics,
        "shutdown":pi_shutdown,
        }

if __name__ == "__main__":
    counter = load_counter()
    while answer != "q":
        answer = input("Press any key to take a picture. \nExcept 'q'. 'q' is for quit.")
        if answer == "q":
            print("Quitting program.")
            newline()
            break
        elif answer == "":
            takepic()
        else:
            commands.get(answer)()
    save_counter(file_, counter)

