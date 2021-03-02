import random
from colorama import *
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def logo():
    print("""
            ██████╗░░█████╗░░██████╗░██████╗░███████╗███╗░░██╗
            ██╔══██╗██╔══██╗██╔════╝██╔════╝░██╔════╝████╗░██║
            ██████╔╝███████║╚█████╗░██║░░██╗░█████╗░░██╔██╗██║
            ██╔═══╝░██╔══██║░╚═══██╗██║░░╚██╗██╔══╝░░██║╚████║
            ██║░░░░░██║░░██║██████╔╝╚██████╔╝███████╗██║░╚███║
            ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
            """)
# Choosing how will affect the generation of password or passwords
    print('Choice a namber')
    print("""
        1.Symbols
        2.Words
        3.Namber
        4.Mixed
        """)

logo()
what = int(input('Enter namber'))


def symbols(what1, what2):
    char1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(what1):
        passwords = ''
        for x in range(what2):
            passwords += random.choice(char1)
        print(passwords)


if what == 1:
    what1 = int(input('How many passwords do you want?: '))
    what2 = int(input('What password length do you want?: '))
    symbols(what1,what2)









    
    
    
    