import lxml
from lxml import html
from lxml import etree
import requests
import re


def get_url(base_url, path):
    page = requests.get(base_url)
    tree = html.document_fromstring(page.text)
    data = tree.xpath(path)
    for i in range(0, len(data)):
        data[i] = etree.tostring(data[i])
        data[i] = data[i].encode('ascii', 'ignore').decode('ascii')
        data[i] = re.sub('\s', '', data[i])
        data[i] = re.sub('">(.*)$', '', data[i])
        data[i] = re.sub('^(.*)"h', 'h', data[i])
    return data


def get_info(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    set = tree.text_content()
    set2 = set.encode('ascii', 'ignore').decode('ascii')
    set2 = re.sub('\s\s+', '~', set2)
    set2 = re.sub('\n+', '', set2)
    set2 = re.sub('^(.*)~Courses', 'Courses', set2)
    set2 = re.sub('Office of(.*)$', '', set2)
    return set2

