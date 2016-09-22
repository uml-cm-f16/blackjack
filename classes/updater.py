#!/usr/bin/python3

from os import system as cmd
from os import name as name
from string import Template

class Updater(object):
    def __init__(self):
        # Init to inherit classes
        super(Updater, self).__init__()

    def generate(self):
        # Generate documentation
        form="html"
        source="docs/source/"
        target="classes/"
        build="docs/build/"

        cmd_doc = Template("sphinx-apidoc -f -o $source $target")
        cmd(cmd_doc.substitute(source=source, target=target))

        #cmd_build = Template("sphinx-build -b $form $source $build")
        #cmd(cmd_build.substitute(form=form, source=source, build=build))

    def sphinx(self):
        """Initialize sphinx documentation.

        """
        cmd("./docs/sphinx-quickstart")

    def ghpages(self):
        """push to github gh-pages branch

        """
        cmd("git subtree push --prefix docs/build/html origin gh-pages")

    def master(self, msg):
        cmd("git add -A")
        cmd("git commit -m " + msg)
        cmd("git pull origin master")
        cmd("git push origin master")