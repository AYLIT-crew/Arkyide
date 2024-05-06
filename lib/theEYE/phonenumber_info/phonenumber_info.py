import subprocess, phonenumbers
from termcolor import colored as cl
from pyfiglet import figlet_format as ff
from phonenumbers import carrier, timezone, geocoder 

def carrier_info(num):
    try:
        return carrier.name_for_valid_number(num, 'en')
    except:
        return None

def geo_info(num):
    try:
        return geocoder.description_for_valid_number(num, 'en')
    except:
        return None

def timezone_info(num):
    try:
        return timezone.time_zones_for_number(num)
    except:
        return None

def number_type(num):
    try:
        num_type = str(phonenumbers.number_type(num))
        file = open('./phonenumber_types.txt', 'r')
        file_data = file.read().split('\n')
        for i in file_data:
            if num_type in i:
                return i.split('=')[0].strip()
    except:
        return None

subprocess.call('clear', shell=True)
print(cl('='*47, 'red'))
print(cl(ff('Phonsint')+'\n\t-A primitive OSINT program for numbers', 'red'))
print(cl('\t-An AYILT Production', 'red'))
print(cl('='*47, 'red'))
no_of_nums = input(cl('Single or Multiple Numbers(S/M):', 'yellow'))
if no_of_nums == 'S':
    number = input(cl('Enter number:', 'yellow'))
    try:
        pnum = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(pnum):
            print(cl(f'Collecting basic information about {number}', 'blue'))
            print(cl('Phone number is valid', 'green'))
            print('-'*10)
            carrier_data = carrier_info(pnum)
            country_data = geo_info(pnum)
            time_zone = timezone_info(pnum)
            num_type = number_type(pnum)
            print(cl(f'Carrier: {carrier_data}', 'blue'))
            print(cl(f'Location: {country_data}', 'blue'))
            print(cl(f'Timezone: ', 'blue'), end='')
            for i in range(len(time_zone)):
                if i != len(time_zone)-1:
                    print(cl(time_zone[i], 'blue'), end=', ')
                else:
                    print(cl(time_zone[i], 'blue'))
            print(cl(f'Number type: {num_type}', 'blue'))
        else:
            print(cl('Phone number is not valid.', 'red'))
    except:
        print(cl('Phone number not given in the correct format.', 'red'))
else:
    manual_typing = input(cl('Manual typing(Y/N):', 'yellow'))
    if manual_typing == 'Y':
        ph_nums = input(cl('Enter phonenumbers(spaces between numbers):', 'yellow')).split()
        for i in ph_nums:
            try:
                pnum = phonenumbers.parse(i)
                if phonenumbers.is_valid_number(pnum):
                    print(cl(f'Collecting basic information about {i}.', 'blue'))
                    print(cl('Phone number is valid', 'green'))
                    print('-'*10)
                    carrier_data = carrier_info(pnum)
                    country_data = geo_info(pnum)
                    time_zone = timezone_info(pnum)
                    num_type = number_type(pnum)
                    print(cl(f'Carrier: {carrier_data}', 'blue'))
                    print(cl(f'Location: {country_data}', 'blue'))
                    print(cl(f'Timezone: ', 'blue'), end='')
                    for i in range(len(time_zone)):
                        if i != len(time_zone)-1:
                            print(cl(time_zone[i], 'blue'), end=', ')
                        else:
                            print(cl(time_zone[i], 'blue'))
                    print(cl(f'Number type: {num_type}', 'blue'))
                    print('-'*47)
                else:
                    print(cl('Phone number not valid.', 'red'))
            except:
                print(cl('Phone number not given in correct format.', 'red'))
    else:
        path = input(cl('Enter file path:', 'yellow'))
        file = open(path, mode='r')
        ph_nums = file.read().split('\n')
        for i in ph_nums:
            try:
                pnum = phonenumbers.parse(i)
                if phonenumbers.is_valid_number(pnum):
                    print(cl(f'Collecting basic information about {i}', 'blue'))
                    print(cl('Phone number is valid', 'green'))
                    print('-'*10)
                    carrier_data = carrier_info(pnum)
                    country_data = geo_info(pnum)
                    time_zone = timezone_info(pnum)
                    num_type = number_type(pnum)
                    print(cl(f'Carrier: {carrier_data}', 'blue'))
                    print(cl(f'Location: {country_data}', 'blue'))
                    print(cl(f'Timezone: ', 'blue'))
                    for i in time_zone:
                        if i != len(time_zone)-1:
                            print(cl(time_zone[i], 'blue'), end=', ')
                        else:
                            print(cl(time_zone[i], 'blue'))
                    print(cl(f'Number type: {num_type}', 'blue'))
                    print('-'*47)
                else:
                    print(cl('Phone number not valid', 'red'))
            except:
                print(cl('Phone number not given in correct format.', 'red'))
exit_inp = input(cl('Press enter to exit', 'red'))
if exit_inp == '':
    subprocess.call('clear', shell=True)
else:
    subprocess.call('clear', shell=True)
