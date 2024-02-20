import requests
from requests import Response
from bs4 import BeautifulSoup


class QR:
    def __init__(self, data: str, size: str = '300x300', format_: str = 'svg'):
        self.url = 'http://api.qrserver.com/v1/'
        self.params = {
            'data': data,
            'size': size,
            'format': format_
        }

    def get_r(self, endpoint: str, **extra_params):
        self.params.update(extra_params)
        response = requests.get(
            url=self.url + endpoint,
            params=self.params,
        )
        if response.status_code == 200:
            return response
        else:
            print(response)
            print(response.text)

    @staticmethod
    def get_svg(response: Response):
        soup = BeautifulSoup(response.content, 'lxml')
        svg = soup.find('svg')
        return svg

    def generate_qr(self):
        response = self.get_r('create-qr-code/')
        if self.params.get('format') == 'svg':
            return self.get_svg(response)
