import requests
from flask import Flask, render_template

json_data = requests.get('http://www.floatrates.com/daily/idr.json')
print(json_data.json())
json_data = {
    'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.7939121618828e-05,
            'date': 'Sun, 19 Jul 2020 12:00:01 GMT', 'inverseRate': 14719.059890272},
    'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.9502773589484e-05,
            'date': 'Sun, 19 Jul 2020 12:00:01 GMT', 'inverseRate': 16805.939281068},
    'gbp': {'code': 'GBP', 'alphaCode': 'GBP', 'numericCode': '826', 'name': 'U.K. Pound Sterling',
            'rate': 5.4130537063406e-05, 'date': 'Sun, 19 Jul 2020 12:00:01 GMT', 'inverseRate': 18473.860675512},
    'aud': {'code': 'AUD', 'alphaCode': 'AUD', 'numericCode': '036', 'name': 'Australian Dollar',
            'rate': 9.725965044581e-05, 'date': 'Sun, 19 Jul 2020 12:00:01 GMT', 'inverseRate': 10281.75605625}}
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
if __name__ == '__main__':

