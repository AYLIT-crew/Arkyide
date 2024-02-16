import os
import git
import pyfiglet
from pyfiglet import figlet_format as ff
import termcolor
from termcolor import colored as cl
from time import sleep

def Credits():
    os.system('clear')
    print(cl(ff("Project Arkyide")))
    print(cl("Project Arkyide, made by: \n", "red"))
    print(cl("Director Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer", 'cyan'))
    
    

    
def arkmenu0():
    print(cl("List of available options: \n", 'red'))
    print("""
    1.E-Mail bomber(beta)
    2.Nmap-scanner(beta)
    3.Tool installer
    4.Credits
    5.Exit
    """)
    user_choice = input('Please select one of the options: \n')
    if user_choice == '1':
        os.system('clear')
        os.system('python lib/mail_bomber.py')
    elif user_choice == '2':
        print(cl('Requires nmap module installed to work', 'red'))
        sleep(1)
        os.system('clear')
        os.system('python lib/net_scan.py')
    elif user_choice == '3':
        os.system('clear')
        os.system('python lib/ARKTLinstaller.py')
        
    elif user_choice == '4':
        Credits()
    elif user_choice == '5':
        exit()
    else:
        print(cl('Wrong choice!'))
        sleep(2)
        os.system('clear')
        arkwelcomer0()

os.system('clear')
def arkwelcomer0():
    os.system('clear')
    print(cl('-'*55, 'red'))
    print(cl(ff('A R K Y I D E')+'\n\t-An AYLIT Production\n\t-v1.0 beta', 'cyan'))
    print(cl("A complex Suite of tools and tool installer", 'black'))
    print(cl('-'*55, 'red'))
    print('\n')
    arkmenu0()    

arkwelcomer0()