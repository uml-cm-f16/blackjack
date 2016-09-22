#!/usr/bin/python3

from classes.installer import Installer

# The package install/ upgrade list
reqs = ["pip", "pygame", "Sphinx"]

# Install packages
installer = Installer(reqs)