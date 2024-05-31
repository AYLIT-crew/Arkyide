from termcolor import colored as cl
from simple_term_menu import TerminalMenu
import os, time, textwrap, curses, subprocess 

class Aesthetic:
    def __init__(self):
        pass


    def Credits(self):
        os.system('clear')
        
        #y'all want cooler ascii art here too?
        print("Project Arkyide")
        print(("Project Arkyide, made by: \n", "red"))
        print(("Director Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer\nKyyomaa - Developer"))
        cont = input('Press enter to continue')
        if cont == '':
            os.system('clear')

    def show_curses_disclaimer(self, stdscr):
        # Initialize curses colors
        curses.start_color()
        curses.use_default_colors()

        # Clear the screen with default background color
        stdscr.bkgd(' ', curses.color_pair(0))
        stdscr.clear()

        # Define the disclaimer message
        disclaimer_message = (
            "###############################################################################\n"
            "#                                                                             #\n"  
            "#  Arkyide is a program which acts as an aide during penetration testing.      #\n"
            "#  Though some of the tools can be used for nefarious purposes, the creators  # \n"
            "#  are not responsible for any misuse of programs.                            #\n"
            "#                                                                             #\n"  
            "###############################################################################\n"

        )

        # Get the screen dimensions
        height, width = stdscr.getmaxyx()

        # Split the message by explicit newlines and then wrap each line
        lines = disclaimer_message.split('\n')
        wrapped_lines = [textwrap.fill(line, width - 4) for line in lines]

        # Flatten the list of wrapped lines
        final_lines = []
        for wrapped_line in wrapped_lines:
            final_lines.extend(wrapped_line.split('\n'))

        # Calculate the starting position to center the message
        y = height // 2 - len(final_lines) // 2
        x = 2

        curses.start_color()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        # Display the wrapped disclaimer message
        for i, line in enumerate(final_lines):
            stdscr.addstr(y + i, x, line, curses.color_pair(1))

        # Display the prompt to continue
        prompt_message = "Press any key to accept the disclaimer and continue..."
        stdscr.addstr(y + len(final_lines) + 2, x, prompt_message, curses.color_pair(1))

        # Refresh the screen to show the message
        stdscr.refresh()

        # Wait for the user to press a key
        stdscr.getch()

    def disclaimer_start(self):
        result = subprocess.run("pwd", capture_output=True, text=True)
        root = result.stdout.strip()  
        usr_txt_path = os.path.join(root, 'playground')

        usr_found = False

        for dirpath, dirnames, filenames in os.walk(root):
            if '.user.txt' in filenames:
                curses.wrapper(self.show_curses_disclaimer)
                os.remove('.user.txt')
            else:
                pass

    def menu(self):
        os.system('clear')
        print(cl(
"""
 █████╗ ██████╗ ██╗  ██╗██╗   ██╗██╗██████╗ ███████╗
██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝██║██╔══██╗██╔════╝
███████║██████╔╝█████╔╝  ╚████╔╝ ██║██║  ██║█████╗  
██╔══██║██╔══██╗██╔═██╗   ╚██╔╝  ██║██║  ██║██╔══╝  
██║  ██║██║  ██║██║  ██╗   ██║   ██║██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═════╝ ╚══════╝
""",'red'))
        options = ("[1] MAIL BOMBER",
                   "[2] NETSCAN (run as root)",
                   "[3] TOOLS INSTALLER",
                   "[4] THE EYE",
                   "[5] ARP SPOOFER",
                   "[6] CHANGE MAC (run as root)",
                   "[7] ANON (anonymous surfing)",
                   "[8] CREDITS",
                   "[9] EXIT")

        menu_highlight_style = ("standout", "fg_gray", "bold")
        terminal_menu = TerminalMenu(options, menu_highlight_style=menu_highlight_style)
        menu_entry_index = terminal_menu.show()

        actions = {
            0: self.mail_bomber,
            1: self.netscan,
            2: self.tools_installer,
            3: self.the_eye,
            4: self.arp_spoofer,
            5: self.change_mac,
            6: self.anon_surfing,
            7: self.credits,
            8: self.exit_program
        }

        selected_action = actions.get(menu_entry_index, self.invalid_selection)
        selected_action()

    def mail_bomber(self):
        print("Mail Bomber selected")
        os.system('clear')
        os.system('python lib/mail_bomber.py')
        os.system('python arkyide.py')

    def netscan(self):
        print("NetScan selected (run as root)")
        print(('Requires nmap module installed to work'))
        time.sleep(2)
        os.system('clear')
        os.system('python lib/net_scan.py')
        os.system('python arkyide.py')

    def tools_installer(self):
        print("Tools Installer selected")
        os.system('clear')
        os.system('python lib/ARKTLinstaller.py')
        os.system('python arkyide.py')
        
    def the_eye(self):
        print("The Eye selected")
        os.system('clear')
        os.system('python lib/theEYE/theEYE.py')
        os.system('python arkyide.py')

    def arp_spoofer(self):
        print("ARP Spoofer selected")
        os.system('clear')
        os.system('python lib/arp_spoofer.py')
        os.system('python arkyide.py')

    def change_mac(self):
        print("Change MAC selected (run as root)")
        os.system('clear')
        os.system('python lib/change_mac.py')
        os.system('python arkyide.py')

    def anon_surfing(self):
        print("Anon Surfing selected")
        os.system('clear')
        os.system('python lib/anon.py')
        os.system('python arkyide.py')



    def credits(self):
        print("Credits selected")
        self.Credits()
        os.system('python arkyide.py')

    def exit_program(self):
        print("Exiting program")
        exit()

    def invalid_selection(self):
        print("Invalid selection")

def main():
    a = Aesthetic() 
    a.disclaimer_start()
    a.menu()

if __name__ == "__main__":
    main()
