from agno.tools import Toolkit
from typing import List
from agno.utils.log import logger
from src.utils.prayer_times import PrayerTimesUtils
from datetime import datetime

class PrayerTimesTool(Toolkit):
    def __init__(self):
        super().__init__(name="prayer_times_agent_tool")
        self.prayer_utils = PrayerTimesUtils()
        self.register(self.get_prayer_times)

    def get_prayer_times(self, args: List[str]) -> str:
        """
        Fetches the prayer times for the specified address and date.

        Args:
            args (List[str]): The address (city and country) and an optional date.
        Returns:
            str: The prayer times or an error message.
        """
        if not args:
            return "Error: No location provided. Please provide an address (e.g., 'Paris, France')."

        address = " ".join(args[:-1])
        address = address.strip()

        date_str = args[-1] if len(args) > 1 else datetime.today().strftime('%Y-%m-%d')
        
        try:
            prayer_times = self.prayer_utils.get_prayer_times_by_address(address, date_str)
            if "error" in prayer_times:
                return prayer_times["error"]
            
            formatted_times = (
                f"Prayer times for {address} on {date_str}:\n"
                f"Fajr: {prayer_times['Fajr']}\n"
                f"Sunrise: {prayer_times['Sunrise']}\n"
                f"Dhuhr: {prayer_times['Dhuhr']}\n"
                f"Asr: {prayer_times['Asr']}\n"
                f"Maghrib: {prayer_times['Maghrib']}\n"
                f"Isha: {prayer_times['Isha']}"
            )
            return formatted_times
        
        except Exception as e:
            logger.warning(f"Error fetching prayer times: {e}")
            return f"Error: {e}"
