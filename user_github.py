#!usr/bin/python3

import requests, time, sys, json
from termcolor import colored
from datetime import datetime

print('##################################################')
print('\n')
print('[+] twitter : y0usef_11 ')
print('[+] Get information for username Github ')
print('[+] usage : ' + sys.argv[0] + ' username github')
print('\n')
print('##################################################')


url = requests.get("https://api.github.com/users/"+ sys.argv[1])
contents = url.text

if url.status_code == 200:
    print(colored("[+] wait for fetching data", "green"))
    time.sleep(2)
    json = json.loads(contents)
    print(colored("[+] Username Found", "green"))
    field_title = ['[+] login', '[+] ID number', '[+] Name', '[+] Company', '[+] Blog is', '[+] Location',
                   '[+] Bio is', '[+] public repos', '[+] followers', '[+] following',
                                                                      '[+] twitter username',
                   '[+] created account ', '[+] updated account ']
    info = ['login', 'id', 'name', 'company', 'blog', 'location', 'bio', 'public_repos', 'followers', 'following',
            'twitter_username', 'created_at', 'updated_at']
    date = json['updated_at']

    for field, key in zip(field_title, info):
        if '_at' in key:
            time = datetime.strptime(
                json[key], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d | %H:%M:%S")
            text = " ==> ".join([field, time])
        else:
            text = " ==> ".join([field, str(json[key])])
        print(colored(text, 'green'))


else:
    print(colored("[-] Username Not Found", "red"))
