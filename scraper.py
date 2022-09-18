from bs4 import BeautifulSoup
from urllib.request import urlopen

subjects = [
]

url = "https://export.arxiv.org/api/query?search_query=all:psychology&start=0&max_results=200"
paras = []

with urlopen(url) as f:
    file = f.read()

soup = BeautifulSoup(file, "xml")

for summary in soup.find_all("summary"):
    new_summary = summary.text.replace("\n", "").strip()
