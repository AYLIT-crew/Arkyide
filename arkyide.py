import os
import sys
from time import sleep
#import git
from pyfiglet import figlet_format as ff
from termcolor import colored as cl
import subprocess

class arkyide():
    def __init__(self):
        self.FG_BLACK = '\033[30m'
        self.FG_RED = '\033[31m'
        self.FG_GREEN = '\033[92m'
        self.FG_YELLOW = '\033[33m'
        self.FG_BLUE = '\033[34m'
        self.FG_MAGENTA = '\033[35m'
        self.FG_CYAN = '\033[36m'
        self.FG_WHITE = '\033[37m'
        self.RESET = '\033[0m'
        
    def Credits(self):
        os.system('clear')
        
        #y'all want cooler ascii art here too?
        print(cl(ff("Project Arkyide")))
        print(cl("Project Arkyide, made by: \n", "red"))
        print(cl("Director Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer\nKyyomaa - Developer", 'cyan'))
        cont = input('Press enter to continue')
        if cont == '':
            os.system('clear')

    def arkmenu0(self):
        print('\n')
        print(cl("List of available options:", 'red'))
        text = f"""
[1] {self.FG_RED}MAIL BOMBER{self.RESET}
[2] {self.FG_RED}NETSCAN (run as root){self.RESET}
[3] {self.FG_RED}TOOLS INSTALLER{self.RESET}
[4] {self.FG_RED}THE EYE{self.RESET}
[5] {self.FG_RED}ARP SPOOFER{self.RESET}
[6] {self.FG_RED}CHANGE MAC (run as root){self.RESET}
[7] {self.FG_RED}ANON (anonymous surfing){self.RESET}
[8] {self.FG_RED}CREDITS{self.RESET}
[9] {self.FG_RED}EXIT{self.RESET}
    """
        print(text)

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
            self.Credits()
        elif user_choice == '9':
            sys.exit()
        else:
            print(cl('Wrong choice!'))
            sleep(2)
            os.system('python arkyide.py')

    os.system('clear')
    def disclamer(self):
        result = subprocess.run("pwd", capture_output=True, text=True)
        root = result.stdout.strip()  
        usr_txt_path = os.path.join(root, 'playground')

        usr_found = False

        for dirpath, dirnames, filenames in os.walk(root):
            if '.user.txt' in filenames:
                file = open('.user.txt', mode='r')
                file = open('3pgithub_tools_in_arkyide.txt', mode='r')
                print(cl("""Arkyide is a program which acts as an aide during penetration testing. 
                         \nThough some of the tools can be used for nefarious purposes, the creators 
                         \nare not responsible for any misuse of programs.\n\n """+file.read(), 'yellow'))
                file.close()
                flag = True
                while flag:
                    agreement = input(cl("Type 'Yes' to to continue:", 'yellow')).lower().strip()
                    if agreement == 'yes':
                        flag = False
                        os.remove('.user.txt')
                    else:
                        print(cl('Wrong choice', 'red'))
                        #sys.exit()
            else:
                pass



    #i dont really fw this banner. do y'all like it more like this?
    '''
        def arkwelcomer0(self):
            os.system('clear')
            letter = ff('Arkyide')
            letter = letter.split('\n')
            for i in range(len(letter)):
                if i != len(letter)-1:
                    letter[i] = '| '+letter[i]+'\t|'
            print(cl('-'*49+'\n'+'\n'.join(letter)+'|\t\t\t\t-v1.0\t\t|'+'\n'+'-'*49, 'cyan'))
            self.arkmenu0()
    '''
    def arkwelcomer0(self):
        os.system('clear')
        print(
"""
   █████████             █████                  ███      █████         
  ███░░░░░███           ░░███                  ░░░      ░░███          
 ░███    ░███  ████████  ░███ █████ █████ ████ ████   ███████   ██████ 
 ░███████████ ░░███░░███ ░███░░███ ░░███ ░███ ░░███  ███░░███  ███░░███
 ░███░░░░░███  ░███ ░░░  ░██████░   ░███ ░███  ░███ ░███ ░███ ░███████ 
 ░███    ░███  ░███      ░███░░███  ░███ ░███  ░███ ░███ ░███ ░███░░░  
 █████   █████ █████     ████ █████ ░░███████  █████░░████████░░██████ 
░░░░░   ░░░░░ ░░░░░     ░░░░ ░░░░░   ░░░░░███ ░░░░░  ░░░░░░░░  ░░░░░░  
                                     ███ ░███                          
                                    ░░██████                           
                                     ░░░░░░                            
"""            
        )

        

def main():
    a= arkyide()
    a.disclamer()
    a.Credits()
    a.arkwelcomer0()
    a.arkmenu0()


    
if __name__ == '__main__':
    main()
