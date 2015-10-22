from lxml import html
import requests
import re

url = 'https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/?flow=CSEBS11&title=Computer+Science+BS+-+Students+entering+CS+Fall+2011+or+Later'

def get_flowsheet_info(url):
    flowsheetPage = requests.get('https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/?flow=CSEBS11&title=Computer+Science+BS+-+Students+entering+CS+Fall+2011+or+Later')
    flowsheetHTML = html.fromstring(flowsheetPage.text)
    rawFlowsheetData = flowsheetHTML.text_content()
    #refinedFlowsheetData = re.sub('pattern', 'substitute', rawFlowsheetData)
    #refinedFlowsheetData = re.sub('pattern', 'substitute', refinedFlowsheetData)
    print 'end\n'

    return rawFlowsheetData

get_flowsheet_info(url)


# ssh into server
# "cd ubflowproject/fecklessbarnacle"
# "python parse.py"