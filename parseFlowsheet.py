from scrapeFlowsheet import get_flowsheet_info
#from app import db, UBClasses, UBRecitation
import re

flowsheet_url = 'https://www.eng.buffalo.edu/undergrad/advisement/flowsheets/?flow=CSEBS11&title=Computer+Science+BS+-+Students+entering+CS+Fall+2011+or+Later'
degree = []    # ComputerScienceBS, MechanicalEngineeringBS, etc.  All entries are the same for each 'flowsheet_url'
semester = []  # Integer 1...8
course = []    # CSE115, MTH141, Gen Ed, etc.

def isolate_flowsheet_data(flowsheet_info):
    semesterCounter = 0;

    # split flowsheet_info into a large array, with elements delimited by \n.
    # example: flowsheet_data = [CSE115 MTH141 ...]
    flowsheet_data = flowsheet_info.split("\n")
    print flowsheet_data






flowsheetInfo = get_flowsheet_info(flowsheet_url)
isolate_flowsheet_data(flowsheetInfo)
#print flowsheetInfo
