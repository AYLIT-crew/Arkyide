import subprocess, sys, requests, re
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

def add_custom_cmds():
    pass

def getosversion(d):
    d = d.split('\n')
    ind = 0
    for i in range(len(d)):
        if 'Aggressive' in d[i]:
            ind = i
            break
    return d[ind]

def getversion(d):
    d = d.split('\n')
    ind = 0
    for i in range(len(d)):
        if 'PORT' in d[i]:
            ind = i
    return '\n'.join(d[ind:])

def get_ports_open(d):
    dsplit = d.split('\n')
    ind = 0
    for i in range(len(dsplit)):
        if 'PORT' in dsplit[i]:
            ind = i
    dsplit = dsplit[ind+1:-2]
    ports_open = []
    for i in dsplit:
        if 'open' in i or 'PORT' in i:
            ports_open.append(i)
    return ports_open

def get_ips(d):
    d = d.split('\n')
    for i in range(len(d)):
        if 'TRACEROUTE' in d[i]:
            ind = i
            break
    d = d[ind:]
    ips = []
    for i in d:
        search_result = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i)
        if search_result  != None:
            ips.append(search_result.group())
    return ips

def get_ip_info(d):
    url = 'https://ipapi.co/'
    infos = {}
    for i in d:
        req_url = url+i+'/'+'json/'
        req_data = requests.get(req_url).json()
        try:
            infos[i] = [req_data['org'], req_data['city'], req_data['country']]
        except:
            pass
    return infos

def check_tool():
    output = subprocess.check_output(['nmap', '--version'])
    if 'Nmap' == output.decode().split('\n')[0].split()[0]:
        pass
    else:
        print(cl('Looks like Nmap is not installed in then system.', 'red'))
        opt = input(cl('Want to install Nmap(y/n)? ', 'yellow')).strip().lower()
        if opt == 'y':
            subprocess.call('sudo apt-get install nmap', shell=True)
            print('-'*10)
            print(cl('[+] Successfully installed.', 'green'))
            print('-'*20)
        else:
            print(cl('Cannot run the program without Nmap, sorry.', 'red'))
            sys.exit()

check_tool()
subprocess.call('clear', shell=True)

commands = {'getversion': 'To get the version of software run by the IP', 'getcommands': 'To get a list of commands which can be used for running a Nmap scan', 'trace': 'To trace the transfer of packets', 'getportsopen': 'To get a list of ports open in a host', 'getosversion': 'To predict the OS run by the IP', 
            'stealthscan': 'Stealth Scan makes it difficult for the host to determine the scan', 'customcmd': 'To run your custom commands, for format check commands',
            'createcmd': 'To create your custom command'}

while True: 
    print(cl('='*40, 'red'))
    print(cl(ff('NetScan'), 'red'))
    print(cl('\t\t-Powered by Nmap\n\t\t-An AYLIT production\n\t\t-v1.0', 'red'))
    print(cl('='*40, 'red'), '\n')
    print(cl('Commands available:', 'red'))
    for i in commands:
        print(cl(f'   ->{i}({commands[i]})', 'red'))
    print('-'*20)
    cmd = input(cl('Enter the command:', 'yellow')).lower().strip()
    if cmd == 'quit':
        sys.exit()
    elif cmd == 'customcmd':
        cmd = input(cl('Enter your command:', 'yellow'))
        data = subprocess.check_output(cmd.split(' '))
        print(cl(data.decode(), 'blue'))
    elif cmd == 'getcommands':
        data = subprocess.check_output(['nmap', '-h'])
        print(cl(data.decode(), 'blue'))
    elif cmd == 'createcmd':
        new_cmd = input(cl('Enter your new command:', 'yellow'))
        cmd_desc = input(cl('Enter the command description:', 'yellow'))
        commands[new_cmd] = cmd_desc
    else:
        addr = input(cl('Enter the IP or address of the webiste to run a nmap scan on:', 'yellow'))
        if cmd == 'getversion':
            ctr = f'nmap -sV {addr}'
            print(cl(f'Command to run: {ctr}', 'red'))
            data = subprocess.check_output(ctr.split(' ')).decode()
            print('-'*10)
            print(cl('[+] Scan ran successfully', 'green'))
            print('-'*10)
            print(cl(getversion(data), 'blue'))
            print('-'*20)
        elif cmd == 'trace':
            ctr = f'nmap --traceroute {addr}'
            print(cl(f'Command to run: {ctr}', 'red'))
            term_data = subprocess.check_output(ctr.split(' ')).decode()
            print('-'*10)
            print(cl('[+] Scan ran successfully', 'green'))
            print('-'*10)
            ips = get_ips(term_data)
            ips_info = get_ip_info(ips)
            raw_opt = input(cl('See raw output(y/n)? ', 'red')).lower().strip()
            if raw_opt == 'y':
                print('-'*10)
                print(cl(term_data.decode(), 'blue'))
            else:
                print('-'*10)
                print(cl('Consolidated output:\n', 'red'))
                for i in ips_info:
                    print('-'*10)
                    print(cl(f'IP:{i}', 'blue'))
                    print(cl(f'Organisation:{ips_info[i][0]}\nCity:{ips_info[i][1]}\nCountry:{ips_info[i][-1]}', 'blue'))
                    print('-'*10)
            print('-'*20)
        elif cmd == 'getportsopen':
            ctr = f'nmap {addr}'
            print(cl(f'Command to run: {ctr}', 'red'))
            term_data = subprocess.check_output(ctr.split(' ')).decode()
            print('-'*10)
            print(cl('[+] Scan ran successfully', 'green'))
            print('-'*10)
            get_open_ports = get_ports_open(term_data)
            print(cl('Ports open:\n'+'-'*10, 'blue'))
            if get_open_ports == []:
                print(cl(f'No ports open for {addr}', 'red'))
            else:
                for i in get_open_ports:
                    print(cl(i, 'blue'))
            print('-'*20)
        elif cmd == 'getosversion':
            ctr = f'nmap -O {addr}'
            print(cl(f'Command to run: {ctr}', 'red'))
            ags = input(cl('Aggressive OS guess(y/n)? ', 'yellow'))
            if ags == 'y':
                ctr = f'nmap -O --osscan-guess {addr}'
            data = subprocess.check_output(ctr.split(' ')).decode()
            print('-'*10)
            print(cl('[+] Scan ran successfully', 'green'))
            print('-'*10)
            get_os_data = getosversion(data)
            print(cl(get_os_data, 'blue'))
            print('-'*20)
        elif cmd == 'stealthscan':
            ctr = f'nmap -sS {addr}'
            print(cl(f'Command to run: {ctr}', 'red'))
            data = subprocess.check_output(ctr.split(' '))
            print('-'*10)
            print(cl('[+] Scan ran successfully', 'green'))
            print('-'*10)
            print(cl(data.decode(), 'blue'))
            print('-'*20)
        elif cmd == 'createcmd':
            print(cl('Still on work, sorry for the inconvenience.', 'red'))
        else:
            print(cl('Wrong option', 'red'))
            print('-'*20)
    press = input(cl('Press enter to clear screen', 'red'))
    if press == '':
        subprocess.call('clear', shell=True)
