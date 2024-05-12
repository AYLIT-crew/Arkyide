import subprocess, time, sys, os
from pyfiglet import figlet_format
from termcolor import colored as cl

def check_root():
    if os.getuid() == 0:
        return True
    else:
        return False

if not check_root():
    print(cl('You must be root to run this program.', 'red'))
    sys.exit()

def format_add(mac):
    new_mac = ''
    for i in range(12):
        if i%2 == 0 or i == 11:
            new_mac += mac[i]
        else:
            new_mac += mac[i]+':'
    return new_mac

def check_if_mac_avail(mac, i):
    try:
        data = subprocess.check_output(f'ifconfig {i} hw ether {mac}'.split(' '), verbose=False).decode().split('\n')
    except:
        return None

def check_interfaces():
    result = []
    data = subprocess.check_output(['ifconfig']).decode().split('\n')
    result.append(data[0][:data[0].index(':')])
    for i in range(len(data)):
        try:
            if data[i] == '':
                result.append(data[i+1][:data[i+1].index(':')])
        except:
            pass
    return result

def main(ma, i):
    cmd1 = f'ifconfig {i} down'
    cmd2 = f'ifconfig {i} hw ether {ma}'
    cmd3 = f'ifconfog {i} up'
    try:
        subprocess.call(cmd1, shell=True)
        print(cl('Command successful', 'green'))
        print('-'*10)
    except:
        print(cl('Error', 'red'))
        sys.exit()
    try:
        subprocess.call(cmd2, shell=True)
        print(cl('Command successful', 'green'))
        print('-'*10)
    except:
        print(cl('Error', 'red'))
        sys.exit()
    try:
        subprocess.call(cmd3, shell=True)
        print(cl('Command successful', 'green'))
        print('-'*10)
    except:
        print(cl('Error', 'red'))
        sys.exit()

while True:
    subprocess.call('clear', shell=True)
    print(cl('-'*60, 'red'))
    print(cl(figlet_format('Change MAC')+'\n\t-A MAC address changer program\n\t-An AYLIT production', 'red'))
    print(cl('-'*60, 'red'))
    mac_address = input(cl('Enter a 12 character length string:', 'red')).strip()
    interface = input(cl("Enter interface whose MAC should be changed(use 'getifaces' command to get interfaces):", 'red'))
    if interface == 'getifaces':
        print(cl('-'*20, 'red'))
        interfaces = check_interfaces()
        for i in range(len(interfaces)):
            print(cl(f'{str(i+1)}. {interfaces[i]}', 'green'))
        print(cl('-'*20, 'red'))
        interface = input(cl('Enter the interface:', 'red'))
        main(mac_address, interface)
    else:
        if check_if_mac_avail(mac_address, interface) == None:
            print(cl('MAC address not available', 'red'))
            sys.exit()
        main(mac_address, interface)
    cont = input(cl('Press enter to quit', 'red'))
    if cont == '':
        break
