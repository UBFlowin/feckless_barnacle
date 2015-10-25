from lxml import html
import requests
import re

def get_flowsheet_info(flowsheet_url):
    flowsheetPage = requests.get(flowsheet_url)
    flowsheetHTML = html.fromstring(flowsheetPage.text)
    rawFlowsheetData = flowsheetHTML.text_content()
    refinedFlowsheetData = re.sub('\s\s+', '\n\n', rawFlowsheetData)
    refinedFlowsheetData = re.sub('required if in Finish in Four', ' required if in Finish in Four\n', refinedFlowsheetData)
    refinedFlowsheetData = re.sub('Faculty Advisor approval required', ' Faculty Advisor approval required\n', refinedFlowsheetData)
    refinedFlowsheetData = re.sub('(.*)Fall\n\nSpring\n\n', '', refinedFlowsheetData, flags=re.DOTALL)
    refinedFlowsheetData = re.sub('\n\n', '\nEND OF SEMESTER\n', refinedFlowsheetData, count=8)
    refinedFlowsheetData = refinedFlowsheetData.encode('ascii', 'ignore').decode('ascii')
    return refinedFlowsheetData

# ssh into server
# "cd ubflowproject/fecklessbarnacle"
# "python parse.py"