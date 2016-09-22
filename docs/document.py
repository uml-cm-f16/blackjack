#!/usr/bin/python3

from os import system as cmd
from os import name as name

# Generate documentation
forms = ["html"]
cmd("sphinx-apidoc -f -o source/ ../classes/")

for form in forms:
    if name == 'nt':
        print('Windows')
        cmd(".\make.bat " + form)
    else:
        print('Bash')
        cmd("./make " + form)

"""
build\html
"""