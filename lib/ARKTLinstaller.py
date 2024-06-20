import os
import subprocess
from time import sleep
from pyfiglet import figlet_format
from termcolor import colored
from simple_term_menu import TerminalMenu

class Installer:

    def __init__(self):
        pass
    
    # Print the list of available tools
    def print_tool_list(self):
        with open('tools_names.txt', 'r') as file:
            tools = file.read()
        print(colored('List of available tools:\n', 'cyan'))
        print(tools)


    # Install a tool from a given Git repository URL
    def install_tool(self, repo_url):
        try:
            print(colored('Tool is being installed, please hold on...\n', 'red'))
            subprocess.run(['git', 'clone', repo_url], check=True)
            print(colored('Tool installed, enjoy.', 'red'))
        except subprocess.CalledProcessError as e:
            print(colored(f'Failed to install tool: {e}', 'red'))
        sleep(1)
        self.menu()

    # Handle user choice for tool installation
    def handle_tool_choice(self, choice):
        tool_repos = {
            '1': 'https://github.com/aircrack-ng/aircrack-ng',
            '2': 'https://github.com/beefproject/beef',
            # Add more tools here as needed
        }
        repo_url = tool_repos.get(choice)
        if repo_url:
            self.install_tool(repo_url)
        else:
            print(colored('Invalid choice or not implemented yet.', 'red'))
            sleep(1)
            self.menu()

    # Display the main menu and handle user input
    def main_menu(self):
            self.print_tool_list()
            usrchoice2 = input(colored('\nEnter the number of tool you want to install:\n', 'cyan'))
            self.handle_tool_choice(usrchoice2)
    

    # Display the welcome screen
#   def welcome(self):
#       os.system('clear')
#       print(colored('-'*58, 'red'))
#        print(colored(figlet_format('G U A R D I A') + '\n\t-An AYLIT Production\n\t-v1.0 beta', 'cyan'))
#        print(colored('-'*58, 'red'))
#        self.main_menu()


    def exit_program(self):
        print(colored('Exiting program', 'red'))
        exit()

    def invalid_selection(self):
        print(colored('Invalid selection', 'red'))
        sleep(2)
        self.menu()

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
            options = ["LIST OF TOOLS", "EXIT"]
            menu_highlight_style = ("standout", "fg_gray", "bold")
            terminal_menu = TerminalMenu(options, menu_highlight_style=menu_highlight_style)
            menu_entry_index = terminal_menu.show()
            actions = {
                0: self.main_menu,
                1: self.exit_program,
            }
            selected_action = actions.get(menu_entry_index, self.invalid_selection)
            selected_action()

if __name__ == "__main__":
    installer = Installer()
    installer.menu()
