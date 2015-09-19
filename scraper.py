from lxml import html
import requests
import re

given_url = 'http://www.buffalo.edu/class-schedule?switch=showcourses&semester=fall&division=UGRD&dept=EE'


def get_info(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    set = tree.text_content()
    set2 = re.sub('\s\s+', '|', set)
    set2 = re.sub('\n+', '', set2)
    set2 = re.sub('(.*)Descriptions for ', '', set2)
    set2 = re.sub('Office of(.*)$', '', set2)
    return set2


def get_abv(info):
    if(info[3] == r"'"):
        abv = info[1:3]
    else:
        abv = info[1:4]
    return abv


def get_dep_name(info):
    info2 = info
    info2 = re.sub("(.*)for '", "", info2)
    info2 = re.sub("'\\|\d(.*)$", "", info2)
    return info2

print get_info(given_url)


