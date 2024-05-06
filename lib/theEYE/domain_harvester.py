from termcolor import colored as cl
import subprocess, threading, socket
from pyfiglet import figlet_format as ff

def check_tool():
    data = subprocess.check_output('ls'.split()).decode().split('\n')
    if 'theHarvester' not in data:
        url = 'https://github.com/laramies/theHarvester.git'
        cmd = f'git clone {url}'
        subprocess.call(cmd, shell=True)
        subprocess.call('pip install -r ./theHarvester/requirements.txt', shell=True)
        subprocess.call('clear', shell=True)

check_tool()

def hosts_data(d):
    ind = 0
    for i in range(len(d)):
        if 'Hosts found' in d[i]:
            ind = i
            break
    hosts = d[ind+2:-1]
    hosts_with_ip, hosts_without_ip, final_hosts = [], [], []
    for i in hosts:
        try:
            socket.inet_aton(i.split(':')[-1])
            hosts_with_ip.append(i)
        except:
            hosts_without_ip.append(i)
    for i in hosts_without_ip:
        for j in hosts_with_ip:
            if i == j.split(':')[0]:
                break
        else:
            final_hosts.append(i)
    final_hosts = hosts_with_ip+final_hosts
    if final_hosts == []:
        print(cl('No hosts found', 'red'))
    else:
        print(cl('Hosts found:', 'blue'))
        cnt = 0
        for i in final_hosts:
            print(cl(f'{str(cnt+1)}. {i}', 'blue'))
            cnt += 1
    print('-'*43)

def asns_data(d):
    ind1, ind2 = 0, 0
    for i in range(len(d)):
        if 'ASNS found' in data[i]:
            ind1 = i
        elif 'Interesting Urls found' in data[i]:
            ind2 = i
            break
    asns = data[ind1+2:ind2-1]
    if asns == []:
        print(cl('No ASNS found', 'red'))
    else:
        cnt = 0
        print(cl('ASNS found:', 'blue'))
        for i in asns:
            print(cl(f'{str(cnt+1)}. {i}', 'blue'))
            cnt += 1
    print('-'*43)

def ips_data(d):
    ind1, ind2 = 0, 0
    for i in range(len(d)):
        if 'IPs found' in d[i]:
            ind1 = i
            break
    for j in range(ind1, len(d)):
        if d[j] == '':
            ind2 = j
            break
    ips = d[ind1+2:ind2]
    if ips == []:
        print(cl('No IPs found', 'red'))
    else:
        cnt = 0
        print(cl('IPs found:', 'blue'))
        for i in ips:
            print(cl(f'{str(cnt+1)}. {i}', 'blue'))
            cnt += 1
    print('-'*43)

subprocess.call('clear', shell=True)

print(cl('='*43, 'red'))
print(cl(ff('Hollow')+'\n\t\t-A domain harvester program\n\t\t-An AYLIT production', 'red'))
print(cl('='*43, 'red'))

domain = input(cl('Enter domain:', 'yellow'))
cmd = f'python ./theHarvester/theHarvester.py -d {domain} -b dnsdumpster,rapiddns,subdomaincenter,subdomainfinderc99,urlscan'
data = subprocess.check_output(cmd.split()).decode().split('\n')
print('-'*43)

t1 = threading.Thread(target=asns_data(data), daemon=True)
t2 = threading.Thread(target=ips_data(data), daemon=True)
t3 = threading.Thread(target=hosts_data(data), daemon=True)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

inp = input(cl('Press enter to continue', 'red'))
if inp == '':
    subprocess.call('clear', shell=True)
else:
    subprocess.call('clear', shell=True)
