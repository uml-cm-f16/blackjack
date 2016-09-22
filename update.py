#!/usr/bin/python3

import sys

from classes.updater import Updater

if len(sys.argv) <= 1:
    print("Error: No Git message given.")
    sys.exit(1)

updater = Updater()

# Generate html documentation
updater.generate()

# Update to master branch
updater.master(sys.argv[1])

# Update gh-pages
updater.ghpages()

print("Done...")
sys.exit()
