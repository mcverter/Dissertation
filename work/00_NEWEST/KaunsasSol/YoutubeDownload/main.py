import yt_dlp
import os

videos = [
    {"url": "https://www.youtube.com/watch?v=RHbOwi0ENU4", "name": "DecenteringEurope"},
    {"url": "https://www.youtube.com/watch?v=8UtgvsULFuQ", "name": "HomageSolNeely__EricGarret','IndigenousCosmopolitanism__NeelyFamilyAutoEthnography"},
    {"url": "https://www.youtube.com/watch?v=AOqPsBtany8", "name": "MostPowerfuSong"},
    {"url": "https://www.youtube.com/watch?v=LuGvaeOb1vk", "name": "TheFlyingUniversity360North"},
    {"url": "https://www.youtube.com/watch?v=0FsYFTGbFD0", "name": "TheFlyingUniversityCourageForCommunity"},
    {"url": "https://www.youtube.com/watch?v=q-6wwtnE8Ds", "name": "TheFlyingUniversityDocumentary"},
    {"url": "https://www.youtube.com/watch?v=7HyyuS9YmRA", "name": "TheTrailWhereTheyCried"},
    {"url": "https://www.youtube.com/watch?v=pO4Ghp752Ec", "name": "WhyUASFaculty"},
]

for video in videos:
    url = video['url']
    print(url)
    os.system(f'yt-dlp -x --audio-format mp3 --audio-quality 0 {url}')

name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')

