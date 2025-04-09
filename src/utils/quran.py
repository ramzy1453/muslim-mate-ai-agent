import requests

class QuranUtils:
    
    def __init__(self):

        self.base_url = 'http://api.alquran.cloud/v1'
    
    def get_surahs(self, edition: str):

        url =  f'{self.base_url}/quran/{edition}'
        res = requests.get(url)
        data = res.json()

        return data['data']['surahs']