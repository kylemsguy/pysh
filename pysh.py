import os
import sys
import socket
import getpass
import subprocess

import re
import math
import traceback

path = None
rcfile = "~/.pyshrc"

def get_prompt():
    theprompt = []
    theprompt.append(getpass.getuser())
    theprompt.append("@")
    theprompt.append(socket.gethostname())
    theprompt.append(":")
    theprompt.append(os.getcwd())
    theprompt.append("$ ")
    return ''.join(theprompt)


def init():
    global path
    if os.path.isfile(os.path.expanduser(rcfile)):
        #import os.path.expanduser(rcfile)
        # TODO: figure out how to import a .rc file
        # either that or load into mem and eval
        pass
    path = os.environ.get("PATH")
    if path:
        path = path.split(":")[:]
    else:
        path = []

def parsecmd(cmd):
    if(cmd == "exit"):
        quit()
    for item in path:
        if(os.path.isfile(os.path.join(os.path.expanduser(item), cmd.split()[0]))):
            os.system(cmd)
            return # eventually do return codes
    try:
        eval(cmd)
    except:
        traceback.print_exc()


def mainloop():
    cmd = input(get_prompt())
    parsecmd(cmd)
    #return_code = subprocess.call(cmd, shell=True)
    #print(return_code)
    

if __name__ == "__main__":
    init()
    while(True):
        mainloop()