from scraper import get_info
from app import db, UBClasses, UBRecitation
import re

#given_url = 'http://www.buffalo.edu/class-schedule?switch=showcourses&semester=fall&division=UGRD&dept=CSE'
given_url = 'http://www.buffalo.edu/class-schedule?switch=showcourses&semester=spring&division=UGRD&dept=CSE'
dep_abv = ''
dep_name = ''
course_num = []
course_name = []
course_id = []
section = []
type = []
days = []
time = []
room = []
campus = []
instructor = []
status = []


def get_abv(info):
    global dep_abv
    if info[3] == r"'":
        dep_abv = info[1:3]
    else:
        dep_abv = info[1:4]
    return dep_abv


def get_dep_name(info):
    global dep_name
    dep_name = info
    dep_name = re.sub("(.*)for '", "", dep_name)
    dep_name = re.sub("'~\d(.*)$", "", dep_name)
    return dep_name


def isolate_data(info):
    data = info
    data = re.sub("'(.*)'(.*)'(.*)'~\d+ Courses~", '', data)
    data = re.sub(
        'Class~Course~Title~Section~Type~Days~Time~Room~Location~Instructor \(\*\) additional instructors~Status', '',
        data)
    data = re.sub('~~', '~', data)
    data = re.sub('~-~', ' - ', data)
    position = 0
    time_unknown = 0
    curr_data = ''
    print data
    for i in range(len(data)):
        if (data[i] == '~'):
            if (position == 1):
                course_id.append(curr_data)
            elif (position == 2):
                curr_data = curr_data.replace("L", "")
                curr_data = curr_data.replace("R", "")
                curr_data = curr_data.replace("B", "")
                curr_data = curr_data.replace("T", "")
                curr_data = curr_data.replace("U", "")
                curr_data = curr_data.replace(" ", "")
                course_num.append(curr_data)
            elif (position == 3):
                course_name.append(curr_data)
            elif (position == 4):
                section.append(curr_data)
            elif (position == 5):
                type.append(curr_data)
            elif (position == 6):
                days.append(curr_data)
            elif (position == 7):
                if (curr_data == 'TBA'):
                    time.append('TBA')
                    room.append('ARR')
                    position += 1
                else:
                    time.append(curr_data)
            elif (position == 8):
                if 'North' in curr_data:
                    room.append("TBA")
                    campus.append(curr_data)
                    position += 1
                else:
                    room.append(curr_data)
            elif (position == 9):
                campus.append(curr_data)
            elif (position == 10):
                instructor.append(curr_data)
            elif (position == 11):
                if ("Open" in curr_data) or ("Closed" in curr_data):
                    status.append(curr_data)
                else:
                    status.append("Status")
                    position -=1
            if (position >= 11):
                position = 1
            else:
                position += 1
            curr_data = ''

        else:
            curr_data += data[i]

    # TODO for loop making an object and adding to the database
    max = 0
    for z in range(0, len(course_num)-1):
        UBCLASS = course_num[z]
        HUB_ID = course_id[z]
        TITLE = course_name[z]
        DEPARTMENT = "CSE"
        SECTION = section[z]
        TYPE = type[z]
        DAYS = days[z]
        TIME = time[z]
        BUILDING = room[z]
        ROOM_NUMBER = room[z]
        LOCATION = "North"
        PROFESSOR = instructor[z]
        STATUS = status[z]
        RESERVED = "No"
        SEMESTER = "Fall"
        PRE1 = "None"
        PRE2 = "None"
        PRE3 = "None"
        PRE4 = "None"
        PRE5 = "None"
        DEGREE = "None"
        print UBCLASS +"/"+ HUB_ID+"/"+ TITLE+"/"+DEPARTMENT+"/"+ SECTION+"/"+ TYPE+"/"+ DAYS+"/"+ TIME+"/"+ BUILDING+"/"+ ROOM_NUMBER+"/"+ LOCATION+"/"+ PROFESSOR+"/"+ STATUS+"/"+ RESERVED+"/"+SEMESTER
        if TYPE == 'LEC':
            class1 = UBClasses(UBCLASS, TITLE, DEPARTMENT, SECTION, TYPE, DAYS, TIME, BUILDING, ROOM_NUMBER, LOCATION,
                               PROFESSOR, STATUS, RESERVED, SEMESTER, PRE1, PRE2, PRE3, PRE4, PRE5, DEGREE)
            db.session.add(class1)
            db.session.commit()
        else:
            results = UBClasses.query.all()
            for result in results:
                temp_max = result.ID
                if temp_max > max:
                    max = temp_max
            #print max
            class1 = UBRecitation(UBCLASS, HUB_ID, max, SECTION, TYPE, DAYS, TIME, BUILDING, ROOM_NUMBER, LOCATION,
                                  STATUS, RESERVED, SEMESTER)
            db.session.add(class1)
            db.session.commit()
    return data


def get_course_id(data):
    return


def get_course_num(info):
    global course_num
    data = isolate_data(info)

    #print data
    return course_num


stuff = get_info(given_url)
print stuff
isolate_data(stuff)
