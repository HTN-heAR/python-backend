from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://export.arxiv.org/api/query?search_query=all:psychology&start=0&max_results=200s"
paragraphs = []

with urlopen(url) as f:
    file = f.read()

soup = BeautifulSoup(file, features="xml")

for summary in soup.find_all("summary"):
    paragraphs.append(summary.text.replace("\n", "").strip())

#for pasting into the text file
with open('filetuning.txt', 'w') as f:
    for paragraph in paragraphs:
        f.write(paragraph)
        f.write('\n')
        f.write('--SEPERATOR--')
        f.write('\n')
