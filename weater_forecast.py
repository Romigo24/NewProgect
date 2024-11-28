import requests


def weater_forecast(location):
    payload = {'M': '',
               'nTq': '',
               'lang': 'ru'
    }
    url_template = 'https://wttr.in/{}'
    url = url_template.format(location)
    response = requests.get(url, params=payload)
    print(response.text)


if __name__ == '__main__':
    weater_forecast('SVO')
    weater_forecast('London')
    weater_forecast('Череповец')