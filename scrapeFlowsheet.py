from lxml import html
import requests
import re


url = 'https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/?flow=CSEBS11&title=Computer+Science+BS+-+Students+entering+CS+Fall+2011+or+Later'

def get_flowsheet_info(url):
    flowsheetPage = requests.get('https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/?flow=CSEBS11&title=Computer+Science+BS+-+Students+entering+CS+Fall+2011+or+Later')
    flowsheetHTML = html.fromstring(flowsheetPage.text)
    rawFlowsheetData = flowsheetHTML.text_content()
    refinedFlowsheetData = re.sub('\s\s+', '\n\n', rawFlowsheetData)
    refinedFlowsheetData = re.sub('required if in Finish in Four', ' required if in Finish in Four\n', refinedFlowsheetData)
    refinedFlowsheetData = re.sub('Faculty Advisor approval required', ' Faculty Advisor approval required\n', refinedFlowsheetData)
    refinedFlowsheetData = re.sub('(.*)Fall\n\nSpring\n\n', '', refinedFlowsheetData, flags=re.DOTALL)
    refinedFlowsheetData = re.sub('\n\n', '\nEND OF SEMESTER\n', refinedFlowsheetData, count=8)
    refinedFlowsheetData = refinedFlowsheetData.encode('ascii', 'ignore').decode('ascii')


    print refinedFlowsheetData

    return refinedFlowsheetData

get_flowsheet_info(url)


# ssh into server
# "cd ubflowproject/fecklessbarnacle"
# "python parse.py"