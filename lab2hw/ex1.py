from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel 
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
da = urlopen(url)

raw = da.read()
content = raw.decode("utf8")
soup = BeautifulSoup(content , "html.parser")
section= soup.find("section", "section chart-grid")
div = section.find("div","section-content")
ul = section.find("ul","")
li_list = ul.find_all("li")
newlist = []

for li in li_list:
    a1 = li.h3.a
    a2 = li.h4.a
    ten = a1.string 
    singer = a2.string 
    song =  { 
        "Title" : ten , 
        "Singer" : singer
    }
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([ten])
    newlist.append(song)
pyexcel.save_as(records = newlist, dest_file_name = "Itunes.xlsx")
