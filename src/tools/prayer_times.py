import requests
from agno.tools import Toolkit
from agno.utils.log import logger
from typing import List
from datetime import datetime, timedelta
import dateparser
from urllib.parse import quote

class PrayerTimesTool(Toolkit):
    def __init__(self):
        super().__init__(name="prayer_times_tool")
        self.register(self.get_prayer_times)

    def get_prayer_times(self, args: List[str]) -> str:
        """
        Fetches the prayer times for the specified date.
        If no date is provided, it fetches prayer times for today.
        If relative date (e.g., 'tomorrow', 'next week') is mentioned, it will calculate the correct date.

        Args:
            args (List[str]): The address (e.g., "Algiers, Algeria") followed by an optional date.
        Returns:
            str: The prayer times for the given date.
        """    
        if not args:
            return "Error: No location provided. Please provide a location (e.g., 'Algiers, Algeria')."

        location = args[0].strip()

        date_str = args[-1] if len(args) > 1 else "today"
        date_obj = self.parse_date(date_str)
        if not date_obj:
            return f"Error: I could not understand the date '{date_str}'. Please provide a valid date (e.g., 'tomorrow', '2025-04-12')."

        date_formatted = date_obj.strftime("%Y-%m-%d")

        
        api_url = f"http://api.aladhan.com/v1/timingsByAddress/{date_formatted}?address={quote(location)}&method=2"
        
        try:
            response = requests.get(api_url)
            data = response.json()
            
            if data['code'] == 200:
                timings = data['data']['timings']
                prayer_times = (
                    f"Prayer times for {location} on {date_formatted}:\n"
                    f"Fajr: {timings['Fajr']}\n"
                    f"Sunrise: {timings['Sunrise']}\n"
                    f"Dhuhr: {timings['Dhuhr']}\n"
                    f"Asr: {timings['Asr']}\n"
                    f"Maghrib: {timings['Maghrib']}\n"
                    f"Isha: {timings['Isha']}"
                )
                return prayer_times
            else:
                return f"Error: Could not retrieve prayer times for {location} on {date_formatted}."
        
        except Exception as e:
            logger.warning(f"Error while fetching prayer times: {e}")
            return f"Error: {e}"

    def parse_date(self, date_str: str) -> datetime:
        """
        Parse a date string into a datetime object. Supports relative dates like 'tomorrow', 'next week', etc.
        
        Args:
            date_str (str): The date string to parse (e.g., "tomorrow", "next week", "2025-04-12").
        
        Returns:
            datetime: The parsed date or None if invalid.
        """
        try:
            parsed_date = dateparser.parse(date_str, languages=['en', 'fr'])
            if parsed_date:
                return parsed_date
            else:
                return None
        except Exception as e:
            logger.warning(f"Error parsing date: {e}")
            return None