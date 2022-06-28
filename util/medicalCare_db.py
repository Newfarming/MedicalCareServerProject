import pymysql,json
from MedicalCareServerApp.models import UserInfo, Department, ActivityInfo


def connect_db():
    db = pymysql.connect(host="localhost", user="root", password="abcddjs921005", db="MedicalCareDatabase",
                         charset="utf8")
    cursor = db.cursor()
    return db, cursor

def userInfo(data_dict):
    return UserInfo.objects.filter(**data_dict).first()


def insertUser(data_dict):
    UserInfo.objects.create(**data_dict)


def deleteUser(nid):
    UserInfo.objects.filter(id=nid).delete()


def editUser(nid, data_dict):
    UserInfo.objects.filter(id=nid).update(**data_dict)


def userList(data_dict):
    # user_set = {}
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        user_set = UserInfo.objects.filter(**data_temp)
    else:
        user_set = UserInfo.objects.all()
    user_set = user_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return user_set


def departInfo(data_dict):
    return Department.objects.filter(**data_dict).first()


def insertDepart(data_dict):
    Department.objects.create(**data_dict)


def deleteDepart(nid):
    Department.objects.filter(id=nid).delete()


def editDepart(nid, data_dict):
    Department.objects.filter(id=nid).update(**data_dict)


def departList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        depart_set = Department.objects.filter(**data_temp)
    else:
        depart_set = Department.objects.all()
    depart_set = depart_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return depart_set


def activityInfo(data_dict):
    return ActivityInfo.objects.filter(**data_dict).first()


def insertActivity(data_dict):
    ActivityInfo.objects.create(**data_dict)


def deleteActivity(nid):
    ActivityInfo.objects.filter(id=nid).delete()


def editActivity(nid, data_dict):
    ActivityInfo.objects.filter(id=nid).update(**data_dict)


def activityList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        activity_set = ActivityInfo.objects.filter(**data_temp)
    else:
        activity_set = ActivityInfo.objects.all()
    activity_set = activity_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return activity_set
