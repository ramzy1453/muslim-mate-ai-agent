from agno.tools import Toolkit
from agno.utils.log import logger
from typing import List
import requests
from src.utils.quran import QuranUtils
import json

class QuranTool(Toolkit):
    def __init__(self):
        super().__init__(name="quran_tool")
        self.quran = QuranUtils()
        self.register(self.get_ayah)
        self.register(self.search_ayah)

    def get_ayah(self, args: List[str]) -> str:
        """
        Get a specific Ayah from the Quran.

        Args:
            args (List[str]): Format: surah ayah edition (e.g., ['2', '255', 'en.asad']).
        Returns:
            str: The ayah text.
        """
        if len(args) < 2:
            return "Please provide at least the surah and ayah number."

        surah = args[0]
        ayah = args[1]
        edition = args[2]

        logger.info(f"Fetching ayah: {surah}:{ayah}/{edition}")
        try:
            ayah = self.quran.get_ayah(surah, ayah, edition)
            return ayah['text'] if ayah else "Ayah not found."
        except Exception as e:
            logger.warning(f"Error fetching ayah: {e}")
            return f"Error: {e}"

    def search_ayah(self, args: List[str]) -> str:
        """
        Search Ayahs that contain a keyword.

        Args:
            args (List[str]): The keyword(s) + edition (e.g., ['mercy', 'en.asad']).
        Returns:
            str: A list of matching ayahs.
        """
        if not args:
            return "Please provide a keyword."

        keyword = args[0]
        edition = args[1]

        logger.info(f"Searching ayah with keyword: {keyword}/{edition}")
        try:
            ayahs = self.quran.search_ayahs(keyword, edition)
            count = ayahs['count']
            matches = ayahs['matches'][:10]
            if count == 0:
                return f"No results found for '{keyword}'."

            result = f"🔍 Found {count} results for '{keyword}':\n\n"
            result += "\n\n".join([f"{m['text']}\n({m['surah']['englishName']} {m['numberInSurah']})" for m in matches])
            return result

        except Exception as e:
            logger.warning(f"Error during search: {e}")
            return f"Error: {e}"