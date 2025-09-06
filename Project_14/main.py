from requests import get
from bs4 import BeautifulSoup

URL = "https://www.thehindu.com/news/national/"
res = get(URL)

raw_html = res.text

soup = BeautifulSoup(raw_html, "html.parser") # soup obj.  (str tekhe ==> html)

data_div = soup.find("div",class_="result")

all_data = data_div.find_all("h3",class_="title")

for i,data in enumerate(all_data):
    print(i+1,'.',data.find("a").get_text(strip=True))

