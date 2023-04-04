import requests
import threading
import random
import time
import string

headers = {
    'Authorization': 'YOUR_DISCORD_TOKEN_HERE'
}

def check_code(code):
    url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('\033[32m[VALID]\033[m ' + code)
        with open('valid.txt', 'a') as f:
            f.write(code + '\n')
    elif response.status_code == 404:
        print('\033[31m[INVALID]\033[m ' + code)
    else:
        print('\033[33m[UNKNOWN]\033[m ' + code)

def generate_codes():
    while True:
        code = 'https://discord.gift/'
        for i in range(16):
            code += random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)

        if '1' not in code and '0' not in code and 'O' not in code and 'I' not in code and 'l' not in code:
            threading.Thread(target=check_code, args=(code,)).start()

        time.sleep(0.1)

print('\033[35m')
print('''       .__  __                    _____              __                         ____ 
  ____ |__|/  |________  ____   _/ ____\_ __   ____ |  | __ ___________  ___  _/_   |
 /    \|  \   __\_  __ \/  _ \  \   __\  |  \_/ ___\|  |/ // __ \_  __ \ \  \/ /|   |
|   |  \  ||  |  |  | \(  <_> )  |  | |  |  /\  \___|    <\  ___/|  | \/  \   / |   |
|___|  /__||__|  |__|   \____/   |__| |____/  \___  >__|_ \\___  >__|      \_/  |___|
     \/                                           \/     \/    \/                    ''')
print('\033[m')

threading.Thread(target=generate_codes).start()
