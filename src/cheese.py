#/usr/bin/env python3
"""CLI tool for taking pictures through a c525 Logicool webcam from a raspberry pi 3."""

#stand lib
import argparse as ap
from pathlib import Path
import subprocess

cameracount = "cameracount.txt"
pic_cmd     = "./takepicture"

def cheese(count):
    """Take a picture. Returns None."""
    subprocess.run([pic_cmd, count])
    print("cheese command == ", pic_cmd, int(count))
    upcount(count)

def check():
    """Checks program's files are in place. Returns None."""
    pass

def getcount():
    """Reads the cameracount file. Returns String"""
    with open(cameracount, "r") as f:
        return f.readline()

def resetcount():
    """Resets the camera count. Returns None."""
    with open(cameracount, "w+") as f:
        f.write("0")
    print("Camera count was reset to '0'.")

def upcount(count):
    """Increments camera count by 1. Returns None."""
    with open(cameracount, "w+") as f:
        f.write(str(int(count) + 1))
    print("New camera count ==", getcount())

def downcount(count):
    """Decrement camera count by 1. Returns None."""
    with open(cameracount, "w+") as f:
        f.write(str(int(count) - 1))
    print("New camera count ==", getcount())

def shutdown():
    """Shuts down the pi. Returns None."""
    subprocess.run(["sudo", "shutdown", "-h", "now"])

def reboot():
    """Reboots the pi. Returns None."""
    subprocess.run(["sudo", "reboot"])

if __name__ == "__main__":
    parser = ap.ArgumentParser(description="Take pictures remotely with a raspberry pi 3.")
    parser.add_argument("-c", "--cheese", help="Take a picture.", 
        action="store_true")
    parser.add_argument("-C", "--check", help="Ensure program is ready.", 
        action="store_true") 
    parser.add_argument("-d", "--downcount", help="Decrement count.", 
        action="store_true")
    parser.add_argument("-g", "--getcount", help="Check the count.", 
        action="store_true")
    parser.add_argument("-r", "--resetcount", help="Reset camera count.", 
        action="store_true")
    parser.add_argument("-R", "--reboot", help="Reboot the pi.", 
        action="store_true")
    parser.add_argument("-S", "--shutdown", help="Shutdown the pi.", 
        action="store_true")
    parser.add_argument("-u", "--upcount", help="Increment count.", 
        action="store_true")

    args = parser.parse_args()

    #load the count
    with open(cameracount, "r") as f:
        count = f.readlines()
    count = count[0].strip()

    if args.cheese:
        cheese(count)
    elif args.check:
        print("make a check function")
    elif args.downcount:
        downcount(count)
    elif args.getcount:
        print("Camera count ==", getcount())
    elif args.resetcount:
        resetcount()
    elif args.reboot:
        reboot()
    elif args.shutdown:
        shutdown()
    elif args.upcount:
        upcount(count)
