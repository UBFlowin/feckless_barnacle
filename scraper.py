from lxml import html
import requests
import re


def get_info(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    set = tree.text_content()
    set2 = re.sub('\s\s+', '~', set)
    set2 = re.sub('\n+', '', set2)
    set2 = re.sub('(.*)Descriptions for ', '', set2)
    set2 = re.sub('Office of(.*)$', '', set2)
    set2 = set2.encode('ascii', 'ignore').decode('ascii')
    print set2
    file = open("info.txt", "w")
    file.write(set2)
    file.close()
    return set2

