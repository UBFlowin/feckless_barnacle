from lxml import html,etree
import requests
import re

path = '//*[@id="sem'


def get_flowsheet_info(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    fullset = []
    for sem in range(1, 9):
        set = tree.xpath(path+str(sem)+'"]/div')
        for i in range(0, len(set)):
            set[i] = etree.tostring(set[i])
            set[i] = set[i].encode('ascii', 'ignore').decode('ascii')
            set[i] = re.sub('<br(.*)$', '', set[i])
            set[i] = re.sub('^(.*)">', '', set[i])
            set[i] = re.sub('</d(.*)$', '', set[i])
            set[i] = re.sub('^<div>', '', set[i])
            set[i] = re.sub('\n', '', set[i])
        set.insert(0, 'sem'+str(sem))
        fullset.append(set)
    return fullset
