# ntz-py
* **Objective**
    * To familiarize with how to manipulate persistent data through command line.
* **Description** -
    * `ntz.py` is intended to be a note taker that can be interacted with through the command line.
    * `ntz.py` is a python command line note tool that allows users to read and write notes to and from `SQLite3`, `YAML`, or `JSON`


## Installation (Once you have it written)
1. Execute the command below to prepend the python environment to the `ntz.py`
    * `echo "#!/usr/bin/env python3" | cat - ntz.py`
2. Execute the command below to add execution permissions to `ntz.py`
    * `chmod +x ntz.py`
3. Execute the command below to move the `ntz.py` file to your `/usr/local/bin` directory.
    * `cp ./ntz.py /usr/local/bin/ntz.py`
4. Execute the command below to append `ntz` alias to your `.bashrc`
    * `echo "alias ntz='./ntz.py'" >> ~/.bashrc`
5. Execute the command below to reread the `.bashrc` file
    * `source ~/.bashrc`  



## Usage

### What's it look like?
* ntz has four commands.
    * [r]emember
    * [-c] creates or appends to a category
    * [f]orget a note
    * [e]dit a note
    * clear
    
### Showing notes.
Typing `ntz` with no arguments should display all your notes. (Can you figure out how to send them to `more` or 
`less` so you can see them one screen at a time?)



## Purpose of Project

Keeping track of a small list of things to remember or stuff that needs doing is a pain. 
Remembering its location, manually accessing it, formatting it and all of the clicking that entails, 
is something many find unpleasant.

Other command line note tools out there are...clunky. 
They require interacting with vim or nano, and manual formatting. 
Yuck

ntz takes command line arguments and builds tidy todo/remember lists using the inherent 
neatness of SQLite (or YAML) and a little python magic. 
The result is a notes system that is easily manipulated both in the command line 
using ntz' interface, or manually in the SQLite database (or YAML file).


