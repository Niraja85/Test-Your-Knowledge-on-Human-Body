""" Import Python modules """

import colorama
from colorama import Fore, Back, Style
import pyfiglet

""" Initialise colorama"""
colorama.init()

"""
A welcome statement for starting the quiz and if the user
says no, the game quits, and if chooses yes to play the game, 
questions are displayed.
"""
welcome = pyfiglet.figlet_format("Welcome To The Quiz World !")
print(welcome)

ans = input("Are you ready to play?\n").lower()

if ans != "yes":
    quit()

score = 0