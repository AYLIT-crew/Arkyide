import subprocess
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

subprocess.call('clear', shell=True)

tools_to_download = ['https://github.com/laramies/theHarvester.git', 'https://github.com/maldevel/EmailHarvester.git']

tools = ['theHarvester', 'EmailHarvester']

def check_tools():
    data = subprocess.check_output('ls'.split()).decode().split('\n')
    for i in range(len(tools)):
        if tools[i] not in data:
            cmd1 = f'git clone {tools_to_download[i]}'
            cmd2 = f'pip install -r {tools[i]}/requirements.txt'
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
            subprocess.call('clear', shell=True)

check_tools()

while True:
    print(cl('='*34, 'red'))
    print(cl(ff('theEYE'), 'red'))
    print(cl('\t     -An OSINT program', 'red'))
    print(cl('\t     -An AYLIT production', 'red'))
    print(cl('='*34, 'red'))

    options = ['IP Information', 'Phonenumber Information', 'Domain harvester', 'Email Harvester', 'WHOIS', 'quit']

    cnt = 1
    for i in options:
        print(cl(f'[{str(cnt)}] {i}', 'red'))
        cnt += 1

    print('-'*34)

    option_number = input(cl('Enter the option number:', 'yellow'))
    if option_number == '1':
        subprocess.call('python ip_info.py', shell=True)
    elif option_number == '2':
        subprocess.call('python phonenumber_info/phonenumber_info.py', shell=True)
    elif option_number == '3':
        subprocess.call('python domain_harvester.py', shell=True)
    elif option_number == '4':
        subprocess.call('python mail_harvester.py', shell=True)
    elif option_number == '5':
        subprocess.call('python whois.py', shell=True)
    elif option_number == '6':
        break
    else:
        print(cl('Wrong option.', 'red'))
        subprocess.call('clear', shell=True)
