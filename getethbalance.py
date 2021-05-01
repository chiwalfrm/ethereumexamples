import requests
import sys
from decimal import *
from os import path
from etherscan.accounts import Account
from etherscan.tokens import Tokens
etherscankey = 'ETHERSCANKEY'
ethplorerkey = 'ETHPLORERKEY'
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'tokens'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
print('INFO: File', sys.argv[1], 'Loaded', file=sys.stderr)
print('INFO: my_address =', my_address, file=sys.stderr)
print('INFO: my_tokens =', my_tokens, file=sys.stderr)
if len(sys.argv) > 2 and sys.argv[2] == 'tokens':
        for coin, value in my_tokens.items():
                apitoken = Tokens(contract_address=value, api_key=etherscankey)
                balancetoken = apitoken.get_token_balance(address=my_address)
                r = requests.get(url='https://api.ethplorer.io/getTokenInfo/' + value + '?apiKey=' + ethplorerkey)
                if coin == '':
                        coin = 'blank'
                if coin == 'sZRX':
                        divisor = float(Decimal(10 ** 18))
                else:
                        divisor = float(Decimal(10 ** int(r.json()['decimals'])))
                if coin[0:12] == 'variableDebt':
                        divisor = -divisor
                if float(balancetoken) != 0:
                        print(coin.ljust(16), '{0:.18f}'.format(float(balancetoken)/divisor).rjust(37).rstrip('0').rstrip('.'))
else:
        api = Account(address=my_address, api_key=etherscankey)
        print('ETH             ', '{0:.18f}'.format(float(api.get_balance())/float(1e+18)).rjust(37).rstrip('0').rstrip('.'))
