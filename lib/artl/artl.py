import os
import subprocess
from time import sleep
from pyfiglet import figlet_format
from termcolor import colored
from simple_term_menu import TerminalMenu

class Installer:

    def __init__(self):
        pass
    
    def instalando(self):
        while True:
            os.system('clear')
           
    
    
    def menu(self):
        while True:
            os.system('clear')
            print("""

    _    ____  _  _____ _   _ ____ _____  _    _     _     _____ ____  
   / \  |  _ \| |/ /_ _| \ | / ___|_   _|/ \  | |   | |   | ____|  _ \ 
  / _ \ | |_) | ' / | ||  \| \___ \ | | / _ \ | |   | |   |  _| | |_) |
 / ___ \|  _ <| . \ | || |\  |___) || |/ ___ \| |___| |___| |___|  _ < 
/_/   \_\_| \_\_|\_\___|_| \_|____/ |_/_/   \_\_____|_____|_____|_| \_\

""")
            options = ( 
                          "[1] CATEGORIES",
                          "[2] EXIT")
            menu_highlight_style = ("standout", "fg_gray", "bold")
            terminal_menu = TerminalMenu(options, menu_highlight_style=menu_highlight_style)
            menu_entry_index = terminal_menu.show()
            actions = {
                0: self.main_menu,
                1: self.exit_program
            }
            selected_action = actions.get(menu_entry_index, self.invalid_selection)
            selected_action()
            
    def main_menu(self):
        print('not done yet')
        sleep(2)
            
    def exit_program(self):
        print("EXITING")
        sleep(1)
        exit()
        os.system('clear')
        exit()
        
    
  
            
            
       

if __name__ == "__main__":
    installer = Installer()
    installer.menu()
    
