import subprocess
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

subprocess.call('clear', shell=True)

def EmailHarvester(dom):
    cmd = f'python ./EmailHarvester/EmailHarvester.py -d {dom} -e googles'
    try:
        data = subprocess.check_output(cmd.split()).decode()
        subprocess.call('clear', shell=True)
        print(cl('='*62, 'red'))
        print(cl(ff('MailHarvester')+'\n\t\t\t\t-A mail harvester program\n\t\t\t\t-An AYLIT production', 'red'))
        print(cl('='*62, 'red'))
        data = data.split('\n')
        ind = 0
        for i in range(len(data)):
            if 'Emails found' in data[i]:
                ind = i
                break
        return data[ind+1:-1]
    except:
        print(cl('EmailHarvester not working... trying theHarvester', 'red'))
        print('-'*20)

def theHarvester(dom):
    cmd = f'python ./theHarvester/theHarvester.py -d {dom} -b duckduckgo,yahoo,bing'
    try:
        data = subprocess.check_output(cmd.split()).decode().split('\n')
        ind1, ind2 = 0, 0
        for i in range(len(data)):
            if 'No emails found' in data[i]:
                return []
        for i in range(len(data)):
            if 'Emails found' in data[i]:
                ind1 = i
                break
        for i in range(len(data)):
            if 'Hosts found' in data[i]:
                ind2 = i
                break
        emails = data[ind1+2:ind2]
        return emails
    except:
        print(cl('theHarvester not working....', 'red'))

print(cl('''
 ██████   ██████            ███  ████  █████   █████                                                   █████   
░░██████ ██████            ░░░  ░░███ ░░███   ░░███                                                   ░░███    
 ░███░█████░███   ██████   ████  ░███  ░███    ░███   ██████   ████████  █████ █████  ██████   █████  ███████  
 ░███░░███ ░███  ░░░░░███ ░░███  ░███  ░███████████  ░░░░░███ ░░███░░███░░███ ░░███  ███░░███ ███░░  ░░░███░   
 ░███ ░░░  ░███   ███████  ░███  ░███  ░███░░░░░███   ███████  ░███ ░░░  ░███  ░███ ░███████ ░░█████   ░███    
 ░███      ░███  ███░░███  ░███  ░███  ░███    ░███  ███░░███  ░███      ░░███ ███  ░███░░░   ░░░░███  ░███ ███
 █████     █████░░████████ █████ █████ █████   █████░░████████ █████      ░░█████   ░░██████  ██████   ░░█████ 
░░░░░     ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░   ░░░░░  ░░░░░░░░ ░░░░░        ░░░░░     ░░░░░░  ░░░░░░     ░░░░░                                                                                                     
         ''', 'red'))

domain = input(cl('Enter the domain:', 'yellow'))
print('-'*62)
data = EmailHarvester(domain)
data += theHarvester(domain)
data = list(set(data))
cnt = 0
for i in range(len(data)):
    if data[i] != '':
        cnt += 1
        print(cl(f'{str(cnt)}. {data[i]}', 'blue'))

inp = input(cl('Press enter to exit', 'red'))
if inp == '':
    subprocess.call('clear', shell=True)
else:
    subprocess.call('clear', shell=True)
