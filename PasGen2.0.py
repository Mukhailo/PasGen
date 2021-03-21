# imports
import random
import subprocess, platform
import colorama
from colorama import Fore, Back, Style
from logo import logo_add, logo2

colorama.init()

def wha():
    global what
    what = int(input('Enter namber: '))
wha()

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

elif what == 2:
    char = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    gs.passw(char)

elif what == 3:
    char = '1234567890'
    gs.passw(char)

elif what == 4:
    # Delete text
    # Windows
    if platform.system() == "Windows":
        subprocess.Popen("cls",shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")
    logo2()
    wha()

    if what == 1:
        char = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        gs.passw(char)

    elif what == 2:
        char = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        gs.passw(char)    
     
if what > 4 or what < 1:
    print('You have entered an incorrect number')
