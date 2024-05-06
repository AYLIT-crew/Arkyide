import requests, subprocess, socket
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

def is_public(ip):
    global data
    data = requests.get('http://ip-api.com/json/'+ip).json()
    try:
        if data['message'] == 'private range':
            return False
    except:
        return True

def get_ip_from_website(url):
    cmd = f'ping -c 1 {url}'
    data = subprocess.check_output(cmd.split()).decode().split('\n')
    data = data[0].split()[2][1:-1]
    return data

def is_ip(inp):
    try:
        sockets.inet_aton(inp)
        return True
    except:
        return False

subprocess.call('clear', shell=True)

print(cl('='*30, 'red'))
print(cl(ff('IPInfo'), 'red'))
print(cl('\t-An IP info provider\n\t-AN AYLIT production', 'red'))
print(cl('='*30, 'red'))

inp = input(cl('Enter the IP address or URL:', 'yellow'))

if is_ip(inp) == False:
    ip = get_ip_from_website(inp)
else:
    ip = inp

print('\n')

if is_public(ip):
    print(cl('-'*10+f'Data for {ip}'+'-'*10, 'blue'))
    print(cl(f"ISP: {data['isp']}", 'blue'))
    print(cl(f"ORG: {data['org']}", 'blue'))
    print(cl(f"Country: {data['country']}", 'blue'))
    print(cl(f"Country Code: {data['countryCode']}", 'blue'))
    print(cl(f"Region: {data['regionName']}", 'blue'))
    print(cl(f"City: {data['city']}", 'blue'))
    print(cl(f"Timezone: {data['timezone']}", 'blue'))
else:
    print(cl('Not a public IP address.', 'red'))

print('\n')

inp = input(cl('Press enter to exit', 'red'))
if inp == '':
    subprocess.call('clear', shell=True)
else:
    subprocess.call('clear', shell=True)
