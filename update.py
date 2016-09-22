#!/usr/bin/python3

import sys

from classes.updater import Updater

if len(sys.argv) <= 1:
    print("Error: No Git message given.")
    sys.exit(1)


updater = Updater()

updater.generate()
#updater.ghpages()
#updater.master(sys.argv[2])

print("Done...")
sys.exit()
