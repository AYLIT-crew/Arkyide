import subprocess, sys, os, time
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

os.system('clear')

def welcome():
    print(cl('='*32, 'red'))
    print(cl(ff('Anon'), 'red'))
    print(cl('\t\t-Surf anonymous', 'red'))
    print(cl('='*32, 'red'))

welcome()

try:
    subprocess.check_output('sudo service tor start'.split())
except:
    print(cl('Tor is not installed.', 'red'))
    install = input(cl('Install Tor(y/n)? ', 'red')).strip().lower()
    if install == 'y':
        subprocess.call('sudo apt install tor', shell=True)
        os.system('clear')
        welcome()

browser = input(cl('Enter installed browser of choice:', 'yellow'))
try:
    subprocess.call(f'proxychains {browser}', shell=True)
    os.system('clear')
except:
    print(cl('Unexpected error, pls check proxychains files in etc/proxychains4.conf and make required changes.', 'red'))
    subprocess.call('service tor stop')

subprocess.call('sudo service tor stop', shell=True)
