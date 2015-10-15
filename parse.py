from scraper import get_info
from app import db, UBClasses
import re


given_url = 'http://www.buffalo.edu/class-schedule?switch=showcourses&semester=fall&division=UGRD&dept=CSE'
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
    data = re.sub('Class~Course~Title~Section~Type~Days~Time~Room~Location~Instructor \(\*\) additional instructors~Status', '', data)
    data = re.sub('~~', '~', data)
    data = re.sub('~-~', ' - ', data)
    position = 0
    time_unknown = 0
    curr_data = ''
    for i in range(len(data)):
        if(data[i] == '~'):
            if(position == 1):
                course_id.append(curr_data)
            elif(position == 2):
                course_num.append(curr_data)
            elif(position == 3):
                course_name.append(curr_data)
            elif(position == 4):
                section.append(curr_data)
            elif(position == 5):
                type.append(curr_data)
            elif(position == 6):
                days.append(curr_data)
            elif(position == 7):
                time.append(curr_data)
                if(curr_data == 'TBA'):
                    time_unknown = 1
            elif(position == 8):
                if(time_unknown == 0):
                    room.append(curr_data)
                else:
                    if(curr_data == 'ARR'):
                        room.append(curr_data)
                    else:
                        room.append("-")
                        position += 1
                time_unknown = 0
            elif(position == 9):
                campus.append(curr_data)
            elif(position == 10):
                instructor.append(curr_data)
            elif(position == 11):
                status.append(curr_data)
            if(position >= 11):
                position = 1
            else:
                position += 1
            curr_data = ''


            # UBCLASS = course_name[i]
            # DEPARTMENT = "CSE"
            # SECTION = section[i]
            # TYPE = type[i]
            # DAYS = days[i]
            # TIME = time[i]
            # BUILDING = room[i]
            # ROOM_NUMBER = room[i]
            # LOCATION = campus[i]
            # PROFESSOR_ID = 0
            # PROFESSOR = instructor[i]
            # STATUS = status[i]
            # RESERVED = "No"
            # SEMESTER = "Fall"
            # class1 = UBClasses(UBCLASS,DEPARTMENT,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,0,PROFESSOR,STATUS,RESERVED,SEMESTER)
            # db.add(class1)
            # db.commit()
        else:
            curr_data += data[i]

    #TODO for loop making an object and adding to the database
    for z in range(0,171):
        UBCLASS = course_name[z]
        DEPARTMENT = "CSE"
        SECTION = section[z]
        TYPE = type[z]
        DAYS = days[z]
        TIME = time[z]
        BUILDING = room[z]
        ROOM_NUMBER = room[z]
        LOCATION = campus[z]

        PROFESSOR = instructor[z]
        STATUS = status[z]
        RESERVED = "No"
        SEMESTER = "Fall"
        class1 = UBClasses(UBCLASS,DEPARTMENT,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,PROFESSOR,STATUS,RESERVED,SEMESTER)
        db.session.add(class1)
        db.session.commit()
    return data


def get_course_id(data):

    return


def get_course_num(info):
    global course_num
    data = isolate_data(info)

    print data
    return course_num

stuff = get_info(given_url)
print stuff
isolate_data(stuff)