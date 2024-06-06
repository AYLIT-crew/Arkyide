import subprocess
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

subprocess.call('clear', shell=True)

print(cl('''
 █████   ███   █████ █████   █████    ███████    █████  █████████ 
░░███   ░███  ░░███ ░░███   ░░███   ███░░░░░███ ░░███  ███░░░░░███
 ░███   ░███   ░███  ░███    ░███  ███     ░░███ ░███ ░███    ░░░ 
 ░███   ░███   ░███  ░███████████ ░███      ░███ ░███ ░░█████████ 
 ░░███  █████  ███   ░███░░░░░███ ░███      ░███ ░███  ░░░░░░░░███
  ░░░█████░█████░    ░███    ░███ ░░███     ███  ░███  ███    ░███
    ░░███ ░░███      █████   █████ ░░░███████░   █████░░█████████ 
     ░░░   ░░░      ░░░░░   ░░░░░    ░░░░░░░    ░░░░░  ░░░░░░░░░  
         ''', 'red'))

domain = input(cl('Enter domain:', 'yellow'))
cmd = f'whois -H {domain}'
data = subprocess.check_output(cmd.split()).decode()
print(cl(data, 'blue'))

inp = input(cl('Press enter to continue', 'red'))
if inp == '':
    subprocess.call('clear', shell=True)
else:
    subprocess.call('clear', shell=True)
