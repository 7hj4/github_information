#!usr/bin/python3

import requests
import time 
import sys
import json
from termcolor import colored

print('##################################################')
print('\n')
print('[+] twitter : y0usef_11 ')
print('[+] Get information for username Github ')
print('[+] usage : '+ sys.argv[0] + ' username github')
print('\n')
print('##################################################')



session = requests.Session()

url = session.get("https://api.github.com/users/"+ sys.argv[1])

contents = url.text

if url.status_code == 200:
    print(colored("[+] wait for fetching data","green"))
    time.sleep(2)
    data = json.loads(contents)
    
    #json fatch data
    
    print(colored("[+] Username Found","green"))
    print (colored('[+] login ' + str(data.get('login')),"green"))
    print (colored('[+] ID number ' + str(data.get('id')),"green"))
    print (colored('[+] Name ' + str(data.get('name').encode('utf8')),"green"))
    print (colored('[+] Company ' + str(data.get('company')),"green"))
    print (colored('[+] Blog is ' + str(data.get('blog')),"green"))
    print (colored('[+] Location ' + str(data.get('location')),"green"))
    print (colored('[+] Bio is ' + str(data.get('bio')),"green"))
    print (colored('[+] public repos ' + str(data.get('public_repos')),"green"))
    print (colored('[+] followers ' + str(data.get('followers')),"green"))
    print (colored('[+] following ' + str(data.get('following')),"green"))
    print (colored('[+] twitter username ' + str(data.get('twitter_username')),"green"))
    print (colored('[+] created account ' + str(data.get('created_at')),"green"))
    print (colored('[+] updated account ' + str(data.get('updated_at')),"green"))
    
else: 
    print(colored("[-] Username Not Found","red"))
