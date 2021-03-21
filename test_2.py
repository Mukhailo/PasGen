# imports
import random
import subprocess, platform
import colorama
from colorama import Fore, Back, Style
from logo import logo_add

colorama.init()


# logo()
# def logo2():
#     print(logo_add(),
#         """
#         1.Words + Nambers
#         2.Symbols + Words + Nambers
#         """)

what = int(input('Enter namber: '))

class Main():
    
    def passw(self, char):
        self.char = char
        what1 = int(input(f'{Fore.RED}How many passwords do you want?: '))
        what2 = int(input(f'{Fore.RED}What password length do you want?: '))
        for i in range(what1):
                passwords = ''
                for x in range(what2):
                    passwords += random.choice(char)
                print('\n',passwords)

gs = Main()

if what == 1:
    char = '+-/*!&$#?=@<>'
    gs.passw(char)

     

if what > 4 or what < 1:
    print('You have entered an incorrect number')
