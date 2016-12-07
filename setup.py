#!/usr/bin/python3
""" The setup program for the application.abs

"""

# IMPORTS

import sys

from app.src.setup import Setup

def main():
    """ Application Installer/ Updater

    """

    # The package install/ upgrade list
    reqs = ["pip",
            "pygame",
            "pytest",
            "pylint",
            "Sphinx"]

    setup = Setup()

    if len(sys.argv) <= 1:
        setup.option("install", "Installs and upgrades all dependencies.")
        setup.option("save {message}", "Updates git repositories.")
        sys.exit(0)

    # Install packages
    if sys.argv[1] == "install":
        setup.install("Installing packages", reqs)
        sys.exit(0)

    # Install packages
    if sys.argv[1] == "test":
        setup.test()
        sys.exit(0)

    # Update git and documentation
    if sys.argv[1] == "save":
        if len(sys.argv) <= 2:
            setup.error("No Git message given.", 1)

        # Generate html documentation
        setup.generate()
        setup.git(sys.argv[2])
        sys.exit(0)

    setup.error("Invalid action given.", 2)

# start main function
if __name__ == "__main__":
    main()
