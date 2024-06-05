import os
from time import sleep
import pyfiglet
import termcolor
from termcolor import colored as cl 
from pyfiglet import figlet_format as ff 
import git

def tllist():
    os.system('clear')
    print(cl('List of available tools:\n'))
    os.system('cat lib/tools_names.txt')
    usrchoice2 = input(cl('\nEnter the number of tool you want to install:\n', 'cyan'))
    if usrchoice2 == '1':
        os.system('clear')
        print(cl('Tool is being installed, please hold on...\n', 'red'))
        os.system('git clone https://github.com/aircrack-ng/aircrack-ng')
        print(cl('Tool installed, enjoy.', 'red'))
        sleep(1)
        aintwel()
    elif usrchoice2 == '2':
        os.system('clear')
        print(cl('Tool is being installed, please hold on...\n', 'red'))
        os.system('git clone https://github.com/beefproject/beef')
        print(cl('Tool installed, enjoy.', 'red'))
        sleep(1)
        aintwel()
    elif usrchoice2 == '3':
        # Needs implementation I guess
        pass

def aintmenu():
    print(cl("1.List of tools \n2.Exit", 'red'))
    usrchoice1 =input(cl("\nSelect one of available options: ", 'red'))
    if usrchoice1 == "1":
        tllist()
    elif usrchoice1 == "2":
        os.system('clear')
        print(cl('Exiting!=', 'red'))
        exit()
    else:
        print(cl("Wrong Choice!!!", 'red'))
        sleep(2)
        aintwel()


def aintwel(): 
    os.system('clear')
    print(cl('-'*58, 'red'))
    print(cl(ff('G U A R D I A')+'\n\t-An AYLIT Production\n\t-v1.0 beta', 'cyan'))
    print(cl('-'*58, 'red'))
    aintmenu()
aintwel()
