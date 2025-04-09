import requests
from datetime import datetime
from typing import Optional
import dateparser

class PrayerTimesUtils:
    def __init__(self):
        self.base_url = 'http://api.aladhan.com/v1/'
        
    def get_prayer_times_by_address(self, address: str, date: Optional[str] = None) -> dict:
        """
        Fetch prayer times for a given address (city and country).

        Args:
            address (str): The address in the format "City, Country" (e.g., 'Paris, France').
            date (str, optional): The date for which to fetch prayer times (in 'YYYY-MM-DD' format). Defaults to None (today).

        Returns:
            dict: The prayer times as a dictionary, or an error message if the request fails.
        """
        if date:
            parsed_date = dateparser.parse(date)
            if parsed_date:
                date = parsed_date.strftime('%Y-%m-%d')
            else:
                return {"error": "Invalid date format. Please provide a valid date (e.g., 'tomorrow', '2025-04-10')."}
        else:
            date = datetime.now().strftime('%Y-%m-%d')

        api_url = f"{self.base_url}/timingsByAddress/{date}?address={address}&method=2"

        try:
            response = requests.get(api_url)
            data = response.json()
            
            if data['code'] == 200:
                return data['data']['timings']
            else:
                return {"error": f"Could not fetch prayer times for {address}."}
        except Exception as e:
            return {"error": f"Error while fetching prayer times: {str(e)}"}
