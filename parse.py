from scraper import get_info, get_url
#from app import db, UBClasses, UBRecitation
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
                # curr_data = curr_data.replace("L","")
                # curr_data = curr_data.replace("R","")
                # curr_data = curr_data.replace("B","")
                # curr_data = curr_data.replace("T","")
                # curr_data = curr_data.replace("U","")
                # curr_data = curr_data.replace(" ","")
                #print curr_data
                course_num.append(curr_data)
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
                #
                #
                #
                # if(time_unknown == 0):
                #     if(curr_data == 'North Campus'):
                #         room.append('-')
                #         campus.append(curr_data)
                #         position += 1
                #     else:
                #         room.append(curr_data)
                # else:
                #     if(curr_data == 'ARR'):
                #         room.append(curr_data)
                #     elif(curr_data == 'Online'):
                #         room.append(curr_data)
                #     else:
                #         room.append("-")
                #         position += 1
            elif(position == 9):
                campus.append(curr_data)
            elif(position == 10):
                if(combine == 1):
                    curr_data = '* ' + curr_data
                    instructor.append(curr_data)
                    combine = 0
                if(curr_data == '*'):
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
            # class1 = UBClasses(UBCLASS,HUB_ID,DEPARTMENT,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,0,PROFESSOR,STATUS,RESERVED,SEMESTER)
            # db.add(class1)
            # db.commit()
        else:
            curr_data += data[i]

    # #TODO for loop making an object and adding to the database
    # max = 0
    # for z in range(0,60):
    #     UBCLASS = course_num[z]
    #     HUB_ID = course_id[z]
    #     TITLE = course_name[z]
    #     DEPARTMENT = "CSE"
    #     SECTION = section[z]
    #     TYPE = type[z]
    #     DAYS = days[z]
    #     TIME = time[z]
    #     BUILDING = room[z]
    #     ROOM_NUMBER = room[z]
    #     LOCATION = "North"
    #     PROFESSOR = instructor[z]
    #     STATUS = status[z]
    #     RESERVED = "No"
    #     SEMESTER = "Fall"
    #     PRE1 = "None"
    #     PRE2 = "None"
    #     PRE3 = "None"
    #     PRE4 = "None"
    #     PRE5 = "None"
    #     DEGREE = "None"
    #     if TYPE == 'LEC':
    #         class1 = UBClasses(UBCLASS,TITLE,DEPARTMENT,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,PROFESSOR,STATUS,RESERVED,SEMESTER,PRE1,PRE2,PRE3,PRE4,PRE5,DEGREE)
    #         db.session.add(class1)
    #         db.session.commit()
    #     else:
    #         results = UBClasses.query.all()
    #         for result in results:
    #             temp_max = result.ID
    #             if temp_max > max:
    #                 max = temp_max
    #         print max
    #         class1 = UBRecitation(UBCLASS,HUB_ID,max,SECTION,TYPE,DAYS,TIME,BUILDING,ROOM_NUMBER,LOCATION,STATUS,RESERVED,SEMESTER)
    #         db.session.add(class1)
    #         db.session.commit()
    return data
#

semester_links = get_url(base_url, '//*[@id="content_internal"]/ul/li/a')
semester_links.remove(semester_links[1])
for semester in semester_links:
    print semester
    department_links = get_url(semester, '/html/body/table[4]/tr/td[1]/table/tr/td[1]/a')
    for department in department_links:
        info = get_info(department)
        isolate_data(info)
        print department
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



