import requests
from urllib.parse import urljoin

def weater_forecast(location):
    url_template = urljoin(f'https://wttr.in/{location}', '?M=&nTq=&lang=ru')
    response = requests.get(url_template)
    print(response.text)

if __name__ == '__main__':
    locations = ['SVO', 'London', 'Череповец']
    for location in locations:
        weater_forecast(location)
