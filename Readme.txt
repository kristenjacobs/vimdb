Simple integration of GDB and the VIM editor.

Installation:

Clone this repository, set the VIMDB_ROOT environment variable
to point to the top level directory of this repository, then add
this directory to your PATH.

Usage:

vimdb/gvimdb <executable>

This will open an instance of vim/gvim, with 2 windows. Gdb will be 
running in a console in the bottom window whereas the top window is 
used to display the current file/line of the source file being debugged. 
This window gets updated whenever GDB stops.

Note: In terms of implementation, this relies on the user having the 
vim Conque plugin installed, as this provides the ability to run a console
application (GDB in this case), from within vim.


