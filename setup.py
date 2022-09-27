from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'a game engine I made for fun'

setup(
    name="bad-game-engine",
    version=VERSION,
    author="PotatMuffin",
    description=DESCRIPTION,
    install_requires=["tkinter"]
)
