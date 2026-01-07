from bs4 import BeautifulSoup
from requests import get
from rich import print
from rich.table import Table

url = "https://www.bbc.com"
res = get(url+"/news/world/asia/india")
data = res.text

soup = BeautifulSoup(data, 'lxml')

news_container_div = soup.find(attrs ={ "data-testid":"alaska-section"})

all_news_container = news_container_div.find_all('a')

all_newses = []


news_table = Table(title = "Latest newses from BBC")

news_table.add_column("Updated on", overflow="fold", no_wrap=False)
news_table.add_column("Headline", overflow="fold", no_wrap=False)
news_table.add_column("Description", overflow="fold", no_wrap=False)
news_table.add_column("url", overflow="fold", no_wrap=False)


for news_set in all_news_container:
	news_updated = news_set.find(attrs={"data-testid":"card-metadata-lastupdated"}).text
	news_headline = news_set.find(attrs={"data-testid":"card-headline"}).text
	news_description = news_set.find(attrs={"data-testid":"card-description"}).text
	news_url = url+news_set.get('href')
	all_newses.append({
	"time":news_updated,
	"headline":news_headline,
	"desc":news_description,
	"url":news_url
	})
	news_table.add_row(str(news_updated),str(news_headline),str(news_description),f"[link={str(news_url)}] {str(news_url)} [/link]  " )

print(news_table)









