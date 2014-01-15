Simple integration of GDB and the VIM editor.

2 Implmentations:

Internal
--------

Run GDB as normal from the command line. This implemention
contains a GDB script that adds the 'vim open' and vim close'
commands, which open/close a instance of the external gvim editor.
If open, this editor will then get updated with the current file/line
when GDB stops.

External 
--------

In this implemention we open vim/gvim, which using the Conque plugin,
opens a GDB console in a bottom window, and creates a top window for the 
current file/line to be shown. This then gets updated when GDB stops.


