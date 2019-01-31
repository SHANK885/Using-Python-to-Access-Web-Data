import urllib.error
import urllib.parse
import urllib.request
from xml.etree import ElementTree


def parse_xml(url):
    counts = []
    page = urllib.request.urlopen(url)
    tree = ElementTree.parse(page)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))

    return sum(counts)


print(parse_xml('http://python-data.dr-chuck.net/comments_42.xml'))
print(parse_xml('http://py4e-data.dr-chuck.net/comments_40797.xml'))
