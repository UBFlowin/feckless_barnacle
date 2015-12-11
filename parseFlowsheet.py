from scrapeFlowsheet import get_flowsheet_info
from scraper import get_url
from app import db, UBClasses, UBRecitation, Degree
import re

base_url = 'https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/'
path = '//*[@id="div_content"]/ul/li/a'

links = get_url(base_url, path)
modified_links = []
for i in range(0,len(links)):
    if i is 1:
        modified_links.append(links[i])
    elif i is 4:
        modified_links.append(links[i])
    elif i is 5:
        modified_links.append(links[i])
    elif i is 6:
        modified_links.append(links[i])
    elif i is 7:
        modified_links.append(links[i])
    elif i is 9:
        modified_links.append(links[i])
    elif i is 11:
        modified_links.append(links[i])
    elif i is 14:
        modified_links.append(links[i])
    elif i is 15:
        modified_links.append(links[i])
    elif i is 17:
        modified_links.append(links[i])
    else:
        pass
print modified_links

for modified_links in modified_links:
    degree = modified_links[6:]
    degree = ''.join([i for i in degree if not i.isdigit()])
    if degree == 'CSEBS':
        degree = 'CSE'
    if degree == 'CEN':
        pass

    sheet_url = base_url + modified_links
    sheet = get_flowsheet_info(sheet_url)

    sem_index = 0
    gen_ed_counter = 0
    for semester in sheet:
        sem_index += 1
        for j in range(1, len(semester)):
            if str(semester[j]).find(' or ') != -1:
                index = semester[j].index(' or ')
                semester[j] = semester [j][:index]
            if str(semester[j]).find('Gen Ed') != -1:
                gen_ed_counter += 1
                semester[j] = semester[j] + ' ' + str(gen_ed_counter)
            degree_entry = Degree(degree,semester[j], '', sem_index, 4)
            db.session.add(degree_entry)
            db.session.commit()
            print str(degree_entry.DEGREE_NAME) + ' - ' + str(degree_entry.UBCLASS)  + ' - ' + str(degree_entry.SEM_INDEX)





