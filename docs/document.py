#!/usr/bin/python3

from os import system as cmd
from os import name as name

# Generate documentation
cmd("sphinx-apidoc -f -o source/ ../classes/")
if name == 'nt':
    print('Windows')
    cmd(".\make.bat html")
else:
    print('Bash')
    cmd(".\make html")