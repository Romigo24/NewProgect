import requests


def main():
    url_template = 'https://wttr.in/{}?M?nTqu&lang=ru'
    svo = url_template.format('СВО')
    response = requests.get(svo)
    print(response.text)

    london = url_template.format('Лондон')
    response = requests.get(london)
    print(response.text)

    cherepovets = url_template.format('Череповец')
    response = requests.get(cherepovets)
    print(response.text)

if __name__ == '__main__':
    main()