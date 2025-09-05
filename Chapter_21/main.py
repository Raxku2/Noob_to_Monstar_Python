from requests import get
from bs4 import BeautifulSoup

# Example 1: Scraping static HTML
html_doc = """
<html><body>
<h1>Hello World</h1>
<p>This is a paragraph</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
print("Extracted H1:", soup.h1.text)
print("Extracted Paragraph:", soup.p.text)

# Example 2: Fetching API data
# (Example API: https://jsonplaceholder.typicode.com/posts)
res = get("https://jsonplaceholder.typicode.com/posts")
if res.status_code == 200:
    data = res.json()
    print(f"Fetched {len(data)} posts")
    print("First Post:", data[0])
else:
    print("API request failed with code:", res.status_code)
````

