import requests

class QuranUtils:
    def __init__(self):
        self.base_url = 'http://api.alquran.cloud/v1'

    def get_ayah(self, surah: int, ayah: int, edition: str) -> str:
        """
        Fetch a specific Ayah from the Quran by Surah and Ayah number.

        Args:
            surah (int): Surah number.
            ayah (int): Ayah number.
            edition (str): The Quran edition (e.g., 'en.asad', 'ar.alafasy').

        Returns:
            str: The text of the requested Ayah.
        """
        url = f'{self.base_url}/ayah/{surah}:{ayah}/{edition}'
        res = requests.get(url)
        data = res.json()

        if res.status_code == 200 and data.get('data'):
            return data['data']
        else:
            return f"Error fetching ayah {surah}:{ayah} with edition '{edition}'"

    def search_ayahs(self, keyword: str, edition: str) -> dict:
        """
        Search Ayahs that contain a given keyword.

        Args:
            keyword (str): The word or phrase to search.
            edition (str): The edition to search in.

        Returns:
            dict: The search results.
        """
        url = f'{self.base_url}/search/{keyword}/all/{edition}'
        res = requests.get(url)
        data = res.json()

        if res.status_code == 200 and data.get('data'):
            return data['data']
        else:
            return {"error": f"Error searching for '{keyword}' in edition '{edition}'"}
    
    @staticmethod
    def get_editions():
        url = 'http://api.alquran.cloud/v1/edition'
        res = requests.get(url)

        data = res.json()
        if res.status_code == 200 and data.get('data'):
            return data['data']
        else:
            return {"error": f"Error searching for editions"}
