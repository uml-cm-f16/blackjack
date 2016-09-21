#!/usr/bin/python3

from classes.installer import Installer

# The package list
reqs = ["pip", "pygame", "Sphinx"]

# Install packages
installer = Installer(reqs)