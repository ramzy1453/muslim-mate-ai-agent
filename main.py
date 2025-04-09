from src.utils.quran import QuranUtils

quran = QuranUtils()

surahs = quran.get_surahs('en.asad')

print(surahs)