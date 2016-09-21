#!/usr/bin/python3

from pip import main as pip

def install(package):
    print("\n- pip install " + package)
    pip(['install', package])

reqs = ["pygame", "pydoc-markdown"]

print("--Install Script--")

for req in reqs:
    install(req)

print("\nDone...")