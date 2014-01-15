import os
import gdb

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
    os.system("vim --servername VIMDB --remote-send " +
              "'<Esc>:windo if winnr() == 1 | " + command + 
              " | endif | startinsert<Enter>'")

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

gdb.events.stop.connect(stopHandler)

# Overrides the gdb quit command to ensure that 
# vim exits when the command is invoked.
class QuitCommand (gdb.Command):
    "Quit command."

    def __init__ (self):
        super (QuitCommand, self).__init__ ("quit",
               gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)

    def invoke (self, arg, from_tty):
        sendCommand("x")

QuitCommand()

