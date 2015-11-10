from scraper import get_info, get_url
from app import db, UBClasses, UBRecitation
import re


base_url = 'http://registrar.buffalo.edu/schedules/index.php'
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
    data = re.sub("(.*)'(.*)'~\d+ Courses~", '', data)
    data = re.sub('Class~Course~Title~Section~Type~Days~Time~Room~Location~Instructor \(\*\) additional instructors~Status', '', data)
    data = re.sub('~~', '~', data)
    data = re.sub('~-~', ' - ', data)
    data = re.sub('~\* ', ' * ', data)
    #print data
    position = 0
    combine = 0
    curr_data = ''
    for i in range(len(data)):
        if(data[i] == '~'):
            if(position == 1):
                course_id.append(curr_data)
            elif(position == 2):
                course_num.append(curr_data)
                #print curr_data
            elif(position == 3):
                course_name.append(curr_data)
            elif(position == 4):
                if(len(curr_data) < 5):
                    section.append(curr_data)
                else:
                    position = 3
            elif(position == 5):
                type.append(curr_data)
            elif(position == 6):
                days.append(curr_data)
            elif(position == 7):
                time.append(curr_data)
            elif(position == 8):
                if(curr_data == 'North Campus'):
                    room.append('-')
                    campus.append(curr_data)
                    position += 1
                elif(curr_data == 'South Campus'):
                    room.append('-')
                    campus.append(curr_data)
                    position += 1
                elif(curr_data == 'Overseas Campus'):
                    room.append('-')
                    campus.append(curr_data)
                    position += 1
                else:
                    room.append(curr_data)
            elif(position == 9):
                campus.append(curr_data)
            elif(position == 10):
                if(combine == 1):
                    curr_data = '* ' + curr_data
                    instructor.append(curr_data)
                    combine = 0
                elif(curr_data == '*'):
                    combine = 1
                    position = 9
                else:
                    instructor.append(curr_data)
            elif(position == 11):

                status.append(curr_data)
            if(position >= 11):
                position = 1
            else:
                position += 1
            curr_data = ''
        else:
            curr_data += data[i]
    return data

index=0
semester_links = get_url(base_url, '//*[@id="content_internal"]/ul/li/a')
semester_links.remove(semester_links[1])
semester_links.remove(semester_links[0])
semester_links.remove(semester_links[0])
semester_links.remove(semester_links[0])
semester_links.remove(semester_links[0])
semester_links.remove(semester_links[0])
for semm in semester_links:
    print semm


broken_departments = []
for semester in semester_links:
    print semester # print link
    department_links = get_url(semester, '/html/body/table[4]/tr/td[1]/table/tr/td[1]/a')
    for department in department_links:
        info = get_info(department)
        isolate_data(info)
        print department
        # print "course_num length = " + str(len(course_num))
        # print "course_name length = " + str(len(course_name))
        # print "course_id length   = " + str(len(course_id))
        # print "section length     = " + str(len(section))
        # print "type length        = " + str(len(type))
        # print "days length        = " + str(len(days))
        # print "time length        = " + str(len(time))
        # print "room length        = " + str(len(room))
        # print "campus length      = " + str(len(campus))
        # print "instructor length  = " + str(len(instructor))
        # print "status length      = " + str(len(status))
        sem = ''
        new_course = ''
        dept_code = ''

        if len(course_num) == len(course_id) and len(course_num) == len(course_name) and len(course_num) == len(section) and len(course_num) == len(type) and len(course_num) == len(days) and len(course_num) == len(time) and len(course_num) == len(room) and len(course_num) == len(campus) and len(course_num) == len(instructor) and len(course_num) == len(status):
            if len(course_num) != 0:
                dept_code = course_num[0][:3]
                dept_code.replace(" ", "")

                new_course = course_num[index]
                length = len(new_course)
                while new_course[-1:].isalpha():
                    new_course = new_course[:-1]
                    length -= 1
                new_course = new_course.replace(' ', '')

                sem = "semester="
                if sem in department:
                    start = department.find(sem)+9
                    end = department.find("&", start)
                    sem = department[start:end]
                    sem = sem.title()

                max = 0
                print "LENGTH OF COURSE_NUM: " + str(len(course_num))
                for z in range(0, len(course_num)):
                    new_course = course_num[z]
                    length = len(new_course)
                    while new_course[-1:].isalpha():
                        new_course = new_course[:-1]
                        length -= 1
                    new_course = new_course.replace(' ', '')

                    UBCLASS = new_course
                    HUB_ID = course_id[z]
                    TITLE = course_name[z]
                    DEPARTMENT = dept_code
                    SECTION = section[z]
                    TYPE = type[z]
                    DAYS = days[z]
                    TIME = time[z]
                    BUILDING = room[z]
                    ROOM_NUMBER = room[z]
                    LOCATION = campus[z]
                    PROFESSOR = instructor[z]
                    STATUS = status[z]
                    YEAR = "none"
                    SEMESTER = sem
                    PRE1 = "none"
                    PRE2 = "none"
                    PRE3 = "none"
                    CO_REQ1 = "none"
                    CO_REQ2 = "none"
                    DEGREE = "none"
                    print UBCLASS
                    if TYPE == 'LEC':
                        class1 = UBClasses(UBCLASS,TITLE,DEPARTMENT,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,PROFESSOR,STATUS,YEAR,SEMESTER,PRE1,PRE2,PRE3,CO_REQ1,CO_REQ2,DEGREE)
                        db.session.add(class1)
                        db.session.commit()
                    else:
                        if dept_code == "NAH":
                            break
                        results = UBClasses.query.all()
                        for result in results:
                            temp_max = result.ID
                            if temp_max > max:
                                max = temp_max
                        class1 = UBRecitation(UBCLASS,HUB_ID,max,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,STATUS,YEAR,SEMESTER)
                        db.session.add(class1)
                        db.session.commit()
        else:
            broken_departments.append(department)
            # store the broken ones
        print course_num
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

for broke in broken_departments:
    print broke
