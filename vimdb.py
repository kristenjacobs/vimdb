import os
import gdb
from time import sleep

g_vimOpen = False

def getLine():
    try:
        info = gdb.execute("info line", to_string=True)
        return int(info.split(" ")[1])
    except:
        return None

def getFileName():
    try:
        info = gdb.execute("info source", to_string=True)
        return (info.split("\n")[2]).split(" ")[2]
    except:
        return None

def sendCommand(command):
    comStr = "gvim --servername SERVER --remote-send ':" + command + "<Esc>'"
    os.system(comStr)

def openVim():
    global g_vimOpen
    if not g_vimOpen:
        os.system("gvim -R --servername SERVER") 
        updateFile()
        updateLine()       
        g_vimOpen = True
 
def closeVim():
    global g_vimOpen
    if g_vimOpen:
        sendCommand("q!")
        g_vimOpen = False

def updateFile():
    fileName = getFileName()
    if fileName != None:
        sendCommand("e " + fileName)

def updateLine():
    lineNumber = getLine()
    if lineNumber != None:
        sendCommand(str(lineNumber))

def stopHandler(event):
    updateFile()
    updateLine()

class VimCommand (gdb.Command):
    "Vim related commands."

    def __init__ (self):
        super (VimCommand, self).__init__ ("vim",
               gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)

class VimOpenCommand (gdb.Command):
    "Opens vim at the current file and line."

    def __init__ (self):
        super (VimOpenCommand, self).__init__ ("vim open",
               gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)

    def invoke (self, arg, from_tty):
        openVim()
        gdb.events.stop.connect(stopHandler)

class VimCloseCommand (gdb.Command):
    "Closes vim."

    def __init__ (self):
        super (VimCloseCommand, self).__init__ ("vim close",
               gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)

    def invoke (self, arg, from_tty):
        closeVim()
        gdb.events.stop.disconnect(stopHandler)

VimCommand()
VimOpenCommand()
VimCloseCommand()
