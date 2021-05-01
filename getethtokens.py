import pprint
import json
import requests
import sys
from os import path
pp = pprint.PrettyPrinter(width=41, compact=True)
ethplorerkey = 'ETHPLORERKEY'
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'showshit'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
print('INFO: File', sys.argv[1], 'Loaded', file=sys.stderr)
print('INFO: my_address =', my_address, file=sys.stderr)
print('INFO: my_tokens =', my_tokens, file=sys.stderr)
r = requests.get(url='https://api.ethplorer.io/getAddressInfo/' + my_address + '?apiKey=' + ethplorerkey)
my_tokens2 = { }
if 'tokens' not in r.json():
        exit()
for dictionary in r.json()['tokens']:
        if 'symbol' in dictionary['tokenInfo']:
                if ( len(sys.argv) > 2 and sys.argv[2] == 'showshit' ) or dictionary['tokenInfo']['address'] not in { \
'0x0cf0ee63788a0849fe5297f3407f701e122cc023', \
'0x0d8775f648430679a709e98d2b0cb6250d2887ef', \
'0x0f71b8de197a1c84d31de0f1fa7926c365f052b3', \
'0x1234567461d3f8db7496581774bd869c83d51c93', \
'0x1e28439d814486c9d989e55b1993c2f1447957cc', \
'0x2b591e99afe9f32eaa6214f7b7629768c40eeb39', \
'0x4092678e4e78230f46a1534c0fbc8fa39780892b', \
'0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce', \
'0x519475b31653e46d20cd09f9fdcf3b12bdacb4f5', \
'0x52903256dd18d85c2dc4a6c999907c9793ea61e3', \
'0x58b6a8a3302369daec383334672404ee733ab239', \
'0x5eac95ad5b287cf44e058dcf694419333b796123', \
'0x68e14bb5a45b9681327e16e528084b9d962c1a39', \
'0x70a72833d6bf7f508c8224ce59ea1ef3d0ea3a38', \
'0x77fe30b2cf39245267c0a5084b66a560f1cf9e1f', \
'0x7b2f9706cd8473b4f5b7758b0171a9933fc6c4d6', \
'0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359', \
'0xab95e915c123fded5bdfb6325e35ef5515f1ea69', \
'0xaf47ebbd460f21c2b3262726572ca8812d7143b0', \
'0xb2f7eb1f2c37645be61d73953035360e768d81e6', \
'0xb33839e05ce9fc53236ae325324a27612f4d110d', \
'0xbaf9a5d4b0052359326a6cdab54babaa3a3a9643', \
'0xbddab785b306bcd9fb056da189615cc8ece1d823', \
'0xc12d1c73ee7dc3615ba4e37e4abfdbddfa38907e', \
'0xd037a81b22e7f814bc6f87d50e5bd67d8c329fa2', \
'0xd3ace836e47f7cf4948dffd8ca2937494c52580c', \
'0xd49ff13661451313ca1553fd6954bd1d9b6e02b9', \
'0xd4de05944572d142fbf70f3f010891a35ac15188', \
'0xdb455c71c1bc2de4e80ca451184041ef32054001', \
'0xe1a178b681bd05964d3e3ed33ae731577d9d96dd', \
'0xe530441f4f73bdb6dc2fa5af7c3fc5fd551ec838', \
'0xe769d988ceda1559aee07963e59e62bd730dbba6', \
'0xef68e7c694f40c8202821edf525de3782458639f', \
'0xf230b790e05390fc8295f4d3f60332c93bed42e2', \
'0xf97f07c370918a762e2bfb689301d544fbc3b7d7' }:
                        if dictionary['tokenInfo']['symbol'] in my_tokens2:
                                print('WARN:', dictionary['tokenInfo']['symbol'], 'duplicated')
                                print('WARN:    ', dictionary['tokenInfo']['address'], 'OLD')
                                print('WARN:    ', my_tokens2[dictionary['tokenInfo']['symbol']], 'NEW')
                        my_tokens2[dictionary['tokenInfo']['symbol']] = dictionary['tokenInfo']['address']
if len(my_tokens2) > 0:
        my_tokens2 = {k: my_tokens2[k] for k in sorted(my_tokens2)}
        pp.pprint(my_tokens2)
