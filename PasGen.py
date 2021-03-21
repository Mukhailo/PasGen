# imports
import random
import subprocess, platform
import colorama
from colorama import Fore, Back, Style


colorama.init()

def logo_add():
    print(f"""{Fore.GREEN}
            ██████╗░░█████╗░░██████╗░██████╗░██████╗░███████╗███╗░░██╗
            ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝░██╔════╝████╗░██║
            ██████╔╝███████║╚█████╗░╚█████╗░██║░░██╗░█████╗░░██╔██╗██║
            ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██║░░╚██╗██╔══╝░░██║╚████║
            ██║░░░░░██║░░██║██████╔╝██████╔╝╚██████╔╝███████╗██║░╚███║
            ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
    """)

def logo():
    logo_add()
# Choosing how will affect the generation of password or passwords
    print("""
        1.Symbols
        2.Words
        3.Namber
        4.Mixed
        """)

logo()
def logo2():
    print(logo_add(),
        """
        1.Words + Nambers
        2.Symbols + Words + Nambers
        """)


what = int(input('Enter namber: '))

# A function that generates a password from characters
def symbols(what1, what2):
    char1 = '+-/*!&$#?=@<>'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print('\n',passwords)
        
#A function that generates a password from words
def words(what1, what2):
    char1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print('\n',passwords)

# A function that generates a password from nambers
def nambers(what1, what2):
    char1 = '1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print('\n',passwords)

# A function that generates a password from words + nambers
def mixed1(what1, what2):
    char1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print('\n',passwords)

# A function that generates a password from words + nambers + symbols
def mixed2(what1, what2):
    char1 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print('\n',passwords)

def whot_namber():
    global what1,what2
    what1 = int(input(f'{Fore.RED}How many passwords do you want?: '))
    what2 = int(input(f'{Fore.RED}What password length do you want?: '))

if what == 1:
    whot_namber()
    symbols(what1,what2)

elif what == 2:
    whot_namber()
    words(what1,what2)

elif what == 3:
    whot_namber()
    nambers(what1,what2)

elif what == 4:
    # Delete text
    # Windows
    if platform.system() == "Windows":
        subprocess.Popen("cls",shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")
    logo2()
    what4 = int(input('Enter namber: '))
    whot_namber()
    
    if what4 == 1:
        mixed1(what1, what2)

    elif what4 == 2:
        mixed2(what1,what2)

if what > 4 or what < 1:
    print('You have entered an incorrect number')












    
    
    
    
