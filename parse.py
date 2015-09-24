from scraper import get_info
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
location = []
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
    return data


#def get_cell(data, location):
 #   curr = 0
 #   iter = 0
 #   while curr < location:


def get_course_num(info):
    global course_num
    data = isolate_data(info)

    print data
    return course_num

stuff = get_info(given_url)
get_course_num(stuff)