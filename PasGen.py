import random
import subprocess, platform
import colorama
from colorama import Fore, Back, Style
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

colorama.init()

def logo():
    print(f"""{Fore.GREEN}
            ██████╗░░█████╗░░██████╗░██████╗░███████╗███╗░░██╗
            ██╔══██╗██╔══██╗██╔════╝██╔════╝░██╔════╝████╗░██║
            ██████╔╝███████║╚█████╗░██║░░██╗░█████╗░░██╔██╗██║
            ██╔═══╝░██╔══██║░╚═══██╗██║░░╚██╗██╔══╝░░██║╚████║
            ██║░░░░░██║░░██║██████╔╝╚██████╔╝███████╗██║░╚███║
            ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
            """)
# Choosing how will affect the generation of password or passwords
    print("""
        1.Symbols
        2.Words
        3.Namber
        4.Mixed
        """)

logo()
def logo2():
    print("""
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
        print(passwords)

def words(what1, what2):
    char1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print(passwords)

def nambers(what1, what2):
    char1 = '1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print(passwords)

def mixed1(what1, what2):
    char1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print(passwords)

def mixed2(what1, what2):
    char1 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print(passwords)

if what == 1:
    what1 = int(input('How many passwords do you want?: '))
    what2 = int(input('What password length do you want?: '))
    symbols(what1,what2)
elif what == 2:
    what1 = int(input('How many passwords do you want?: '))
    what2 = int(input('What password length do you want?: '))
    words(what1,what2)
elif what == 3:
    what1 = int(input('How many passwords do you want?: '))
    what2 = int(input('What password length do you want?: '))
    nambers(what1,what2)
elif what == 4:
    # Windows
    if platform.system() == "Windows":
        subprocess.Popen("cls",shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")
    logo2()
    what4 = int(input('Enter namber: '))
    what1 = int(input('How many passwords do you want?: '))
    what2 = int(input('What password length do you want?: '))
    if what4 == 1:
        mixed1(what1, what2)
    elif what4 == 2:
        mixed2(what1,what2)










    
    
    
    