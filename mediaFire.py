from fake_useragent import UserAgent
from dotenv import load_dotenv
from urllib.parse import urlparse
from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
from os import environ

load_dotenv()

class Media:
    def __init__(self) -> None:
        self.ua = UserAgent()
        self.BeautifulSoup = BeautifulSoup
        self.CloudScraper = CloudScraper
        self.API_URL = f"https://{environ['API_URL']}" if not urlparse(environ['API_URL']).scheme else environ['API_URL']
        self.HEADERS = {
            'Authority': 'www.mediafire.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'pt-BR,pt;q=0.9',
            'cache-control': 'cache',
            'dnt': '1',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'upgrade-insecure-requests': '0',
            'user-agent': self.ua.random,
        }

    async def _send_request(self, url: str):
        data = {
            'status': True,
            'message': None,
            'details': None
        }
        try:
            scraper = CloudScraper.create_scraper()
            resp = scraper.get(url)
            data['message'] = resp.text
        except Exception as e:
            data['status'] = False
            data['details'] = f"{type(e).__name__}: {str(e)}"
        return data

    async def getLink(self, url: str) -> dict:
        resp = await self._send_request(url)
        if resp['status']:
            try:
                soup = self.BeautifulSoup(resp['message'], 'html.parser')
                link = soup.find(class_='popsok').get('href')
                name = soup.find(class_='promoDownloadName').getText(strip=True)
                resp['message'] = {'name': name, 'link': link}
            except AttributeError:
                resp['status'] = False
                resp['message'] = None
                resp['details'] = f'Invalid id'
            except Exception as e:
                resp['status'] = False
                resp['details'] = f'{e}'
            return resp
        return resp

    async def init(self, file_id: str) -> dict:
        URL = f'{self.API_URL}/file/{file_id}/?dkey=ac6rwoqrs86&r=1637'
        return await self.getLink(URL)