import os
import sys
import git
from time import sleep
from pyfiglet import figlet_format as ff
from termcolor import colored as cl

def Credits():
    os.system('clear')
    print(cl(ff("Project Arkyide")))
    print(cl("Project Arkyide, made by: \n", "red"))
    print(cl("Director Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer", 'cyan'))
    cont = input('Press enter to continue')
    if cont == '':
        os.system('clear')

def arkmenu0():
    print(cl("List of available options: \n", 'red'))
    print("""
    1.E-Mail bomber
    2.NetScan
    3.Tools installer
    4.theEYE
    5.ARP Spoofer
    6.Credits
    7.Exit
    """)
    user_choice = input(cl('Please select one of the option numbers:', 'yellow'))
    if user_choice == '1':
        os.system('clear')
        os.system('python lib/email_bomber.py')
        os.system('python arkyide.py')
    elif user_choice == '2':
        print(cl('Requires nmap module installed to work', 'red'))
        sleep(2)
        os.system('clear')
        os.system('python lib/net_scan.py')
        os.system('python arkyide.py')
    elif user_choice == '3':
        os.system('clear')
        os.system('python lib/ARKTLinstaller.py')
        os.system('python arkyide.py')
    elif user_choice == '4':
        os.system('clear')
        os.system('python lib/theEYE/theEYE.py')
        os.system('python arkyide.py')
    elif user_choice == '5':
        os.system('clear')
        os.system('python lib/arp_spoofer.py')
        os.system('python arkyide.py')
    elif user_choice == '6':
        Credits()
    elif user_choice == '7':
        sys.exit()
    else:
        print(cl('Wrong choice!'))
        sleep(2)
        os.system('python arkyide.py')

def arkwelcomer0():
    os.system('clear')
    print(cl('-'*55, 'red'))
    print(cl(ff('A R K Y I D E')+'\n\t-An AYLIT Production\n\t-v1.0 beta', 'cyan'))
    print(cl("A complex Suite of tools and tool installer", 'cyan'))
    print(cl('-'*55, 'red'))
    print('\n')
    arkmenu0()

arkwelcomer0()
