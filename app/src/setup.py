#!/usr/bin/python3
""" Application setup script

"""

# IMPORTS

import sys
import os

from string import Template
from pip import main as pip

# CLASS

class Setup(object):
    """ Installs and upgrades necessary packages.

    """
    def __init__(self):
        """ Package installer constructor.

        Args:
            packages: (list (str)): A list of packages to install.

        """
        self._form = "html"
        self._source = "docs/source/"
        self._target = "classes/"
        self._build = "docs/build/"

        # Init to inherit classes
        super().__init__()

    # Private methods
    def _install(self, package):
        """ Installs a package.

        Args:
            package: (str): The name of the package to be installed.

        """
        print("\n - pip install " + package)
        pip(['install', '--upgrade', package])

    def _sphinx(self):
        """ Initialize sphinx documentation.

        """
        print("\n - Initializing sphinx")
        os.system("./docs/sphinx-quickstart")

    def _ghpages(self):
        """ Update gh-pages branch.

        """
        print("\n - Uploading documentation to gh-pages branch")
        cmd_msg = Template("git subtree push --prefix $b$f origin gh-pages")
        os.system(cmd_msg.substitute(b=self._build,
                                     f=self._form))

    def _master(self, msg):
        """ Update master branch.

        """
        print("\n - Uploading to git master branch: " + sys.argv[1])
        os.system("git add -A")
        os.system('git commit -m "' + msg +'"')
        os.system("git pull origin master")
        os.system("git push origin master")

    # Public methods
    def option(self, key, msg):
        """ Displays a command option message.

        Args:
            msg: (str): The message to print
            key: (str): The install command.

        """
        print("  " + key)
        print("\t" + msg)

    def install(self, msg, packages):
        """ Driver for package installer.

        Args:
            msg: (str): The message to print
            packages: (list (str)): A list of packages to install.

        """
        print("\n" + msg)
        for package in packages:
            self._install(package)

    def error(self, msg, exit_code):
        """ Reports error and exits

        Args:
            msg: (str): The message to print
            exit_code: (int): The exit code to give
        """
        print("\n" + msg)
        sys.exit(exit_code)

    def generate(self):
        """ Generates Documentation

        """
        # Generate documentation
        print("\n - Building documentation")
        cmd_msg = Template("sphinx-apidoc -f -o $s $t")
        os.system(cmd_msg.substitute(s=self._source,
                                     t=self._target))

        # Generate documentation
        print("\n - Generating html documentation")
        cmd_msg = Template("sphinx-build -b $f $s $b$f")
        os.system(cmd_msg.substitute(f=self._form,
                                     s=self._source,
                                     b=self._build))

    def git(self, commit_msg):
        """ Update git branches.

        Args:
            commit_msg: (str): The commit message.

        """
        # Update to master branch
        self._master(commit_msg)
        # Update gh-pages
        self._ghpages()

    def test(self):
        """ Run unit tests

        """
        # python -m unittest discover -s app/test
        os.system("python -m unittest discover -s app/test")
