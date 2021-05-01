import requests
import sys
from os import path
if len(sys.argv) < 1:
        print("ERROR: Must specify file containing api configuration.")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
print('INFO: File', sys.argv[1], 'Loaded', file=sys.stderr)
print('INFO: my_address =', my_address, file=sys.stderr)
r = requests.get(url='https://api.badger.finance/v2/accounts/' + my_address)
for key in r.json()['balances'][0].items():
        if key[0] == 'balance':
                for key2, value2 in key[1][0].items():
                        if key2 == 'balance':
                                print(value2)
