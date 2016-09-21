#!/usr/bin/python3

from pip import main as pip

class Installer(object):
    """Installs and upgrades necessary packages.

    """

    def __init__(self, packages):
        """Package installer constructor.

        Calls the driver and installs packages.

        Args:
            packages: [str...]: A list of packages to install.
        """
        self._driver(packages)

        # Init to inherit classes
        super(Installer, self).__init__()

    def _install(self, package):
        """Installs a package.

        Args:
            package: (str): The name of the package to be installed.

        """
        print("\n- pip install " + package)
        pip(['install', '--upgrade', package])

    def _driver(self, packages):
        """Driver for package installer.

        Args:
            packages: [str...]: A list of packages to install.

        """
        print("--Install Script--")
        for package in packages:
            self._install(package)
        print("\nDone...")