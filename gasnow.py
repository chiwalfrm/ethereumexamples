import requests
r = requests.get(url='https://www.gasnow.org/api/v3/gas/price?utm_source=:YourAPPName')
for key, value in r.json()['data'].items():
        if key != 'timestamp':
                print(key.ljust(8), str(int(value/1000000000)).rjust(3))
