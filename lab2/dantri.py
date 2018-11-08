from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
#1. connect to the website 
url = "https://dantri.com.vn"
con = urlopen(url)



#2. Download content from the page
raw_data = con.read()
page_content = raw_data.decode("utf8")
# with open ( "dantri.html", "w") as f:
#     f.write(page_content)

#3. Find the ROI
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") #href= "", id = ""
# print(ul.prettify())
#4. Extract data
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    a = li.h4.a
    # print(a.string)
    title = a.string
    # print(a["href"])
    link = url + a["href"]

    news = OrderedDict({
        "title" : title,
        "link" : link,
    })
    new_list.append(news)
    pyexcel.save_as(records = new_list, dest_file_name = "Dantri.xlsx")
#5. Save Data pip3 install certifi