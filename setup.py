#!/usr/bin/python3

import sys

from classes.app.installer import Installer
from classes.app.updater import Updater

# The package install/ upgrade list
reqs = ["pip", "pygame", "Sphinx"]

if len(sys.argv) <= 1:
    print("\nError: No Action given.")
    sys.exit(1)

elif sys.argv[1] == 'install':
    # Install packages
    installer = Installer(reqs)
    sys.exit()

elif sys.argv[1] == 'save':
    if len(sys.argv) <= 2:
        print("\nError: No Git message given.")
        sys.exit(2)
    updater = Updater()
    # Generate html documentation
    updater.generate()
    # Update to master branch
    updater.master(sys.argv[2])
    # Update gh-pages
    updater.ghpages()
    print("Done...")
    sys.exit()

else:
    print("\nError: Invalid action given.")
    sys.exit(2)