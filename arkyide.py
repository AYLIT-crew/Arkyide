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
    print(cl("Director Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer\nKyyomaa - Developer", 'cyan'))
    cont = input('Press enter to continue')
    if cont == '':
        os.system('clear')

def arkmenu0():
    print('\n')
    print(cl("List of available options:", 'red'))
    print(cl("""
    1.E-Mail bomber
    2.NetScan(run as root)
    3.Tools installer
    4.theEYE
    5.ARP Spoofer
    6.Change MAC(run as root)
    7.Anon(anonymous surfing)
    8.Credits
    9.Exit
    """, 'red'))
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
        os.system('clear')
        os.system('python lib/change_mac.py')
        os.system('python arkyide.py')
    elif user_choice == '7':
        os.system('clear')
        os.system('python lib/anon.py')
        os.system('python arkyide.py')
    elif user_choice == '8':
        Credits()
    elif user_choice == '9':
        sys.exit()
    else:
        print(cl('Wrong choice!'))
        sleep(2)
        os.system('python arkyide.py')

os.system('clear')

file = open('user.txt', mode='r')
if bool(int(file.read())):
    file.close()
    file = open('3pgithub_tools_in_arkyide.txt', mode='r')
    print(cl("""Arkyide is a program which acts as an aide during penetration testing. Though some of the tools can be used for nefarious purposes, the creators are not responsible for any misuse of programs.\n """+file.read(), 'yellow'))
    file.close()
    agreement = input(cl("Type 'Yes' to to continue:", 'yellow')).lower().strip()
    if agreement == 'yes':
        file = open('user.txt', mode='w')
        file.write('0')
        file.close()
    else:
        print(cl('Wrong choice', 'red'))
        sys.exit()

def arkwelcomer0():
    os.system('clear')
    letter = ff('Arkyide')
    letter = letter.split('\n')
    for i in range(len(letter)):
        if i != len(letter)-1:
            letter[i] = '| '+letter[i]+'\t|'
    print(cl('-'*49+'\n'+'\n'.join(letter)+'|\t\t\t\t-v1.0\t\t|'+'\n'+'-'*49, 'cyan'))
    arkmenu0()

arkwelcomer0()
