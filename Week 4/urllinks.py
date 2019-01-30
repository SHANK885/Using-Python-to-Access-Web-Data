import urllib
from bs4 import BeautifulSoup

#url = input("Enter URL: ")
url = "http://py4e-data.dr-chuck.net/known_by_Bisma.html"
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

while count > 0:
    print("retrieving: {0}".format(url))
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print(names[-1])