from django.shortcuts import render

# Create your views here.
""" View: multidisciplinaryConsultation
include: OnloadCurrentOrder, PlaceCurrentOrder, PayCurrentOrder.
security:  CryptInfo(util.public_util)
"""
import json
import simplejson
from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from django.views import View
from util.medicalCare_db import insertUser, editUser, deleteUser, userList, insertDepart, editDepart, deleteDepart, \
    departList, insertActivity, editActivity, deleteActivity, activityList, userInfo, departInfo, activityInfo, \
    permissionList
from django.core import serializers
from django.http import JsonResponse
import jwt

def query_userinfo(request):
    rst = {}
    # if request.GET.get("id"):
    #     rst['id'] = request.GET.get("id")
    if request.GET.get("username"):
        rst['username'] = request.GET.get("username")
    if request.GET.get("name"):
        rst['name'] = request.GET.get("name")
    if request.GET.get("phone"):
        rst['phone'] = request.GET.get("phone")
    if request.GET.get("workNo"):
        rst['workNo'] = request.GET.get("workNo")
    if request.GET.get("identityCard"):
        rst['identityCard'] = request.GET.get("identityCard")
    if request.GET.get("depart_id"):
        rst['depart_id'] = request.GET.get("depart_id")
    if request.GET.get("password"):
        rst['password'] = request.GET.get("password")
    if request.GET.get("permission_id"):
        rst['permission_id'] = request.GET.get("permission_id")
    return rst


class UserAdd(View):
    def post(self, request):
        return HttpResponse('post UserAdd')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_userinfo(request)
        insertUser(rst)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class UserEdit(View):
    def post(self, request):
        return HttpResponse('post UserEdit')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_userinfo(request)
        uid = request.GET.get("id")
        editUser(uid, rst)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class UserDelete(View):
    def post(self, request):
        return HttpResponse('post UserDelete')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        uid = request.GET.get("id")
        deleteUser(uid)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class UserList(View):
    def post(self, request):
        return HttpResponse('post Userlist')

    def get(self, request):
        rst = {}
        print('request')
        print(request.GET)
        if request.GET.get('search'):
            rst['search'] = request.GET['search']
        if request.GET.get('search_type'):
            rst['search_type'] = request.GET['search_type']
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET['pageStart']
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET['pagesize']
        # data_array = json.loads(serializers.serialize("json", userList(rst)))
        userlist_set = userList(rst)
        return_arr = []
        for index in range(len(userlist_set)):
            # print(index, data_array[index]['pk'])
            return_arr.append({
                'id': userlist_set[index].pk,
                'name': userlist_set[index].name,
                'username': userlist_set[index].username,
                'phone': userlist_set[index].phone,
                'workNo': userlist_set[index].workNo,
                'identityCard': userlist_set[index].identityCard,
                'depart_id': userlist_set[index].depart.id,
                'depart_name': userlist_set[index].depart.title,
                'permission_id': userlist_set[index].permission.id,
                'permission_name': userlist_set[index].permission.name,
                'permission_content': userlist_set[index].permission.content_type,
            })
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': return_arr
            }, safe=False)


class DepartAdd(View):
    def post(self, request):
        return HttpResponse('post DepartAdd')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = {'title': request.GET.get('title')}
        insertDepart(rst)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartEdit(View):
    def post(self, request):
        return HttpResponse('post DepartEdit')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = {'title': request.GET.get('title')}
        nid = request.GET.get("id")
        editDepart(nid, rst)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartDelete(View):
    def post(self, request):
        return HttpResponse('post DepartDelete')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        nid = request.GET.get("id")
        deleteDepart(nid)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartList(View):
    def post(self, request):
        return HttpResponse('post UserList')

    def get(self, request):
        rst = {}
        if request.GET.get('search'):
            rst['search'] = request.GET.get('search')
            rst['search_type'] = 'title'
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET.get('pageStart')
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET.get('pagesize')
        data_dict = json.loads(serializers.serialize("json", departList(rst)))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)


class DepartDetails(View):
    def post(self, request):
        return HttpResponse('post UserDetails')

    def get(self, request):
        get_obj = {
            'id': request.GET.get('id'),
        }
        depart_obj = departInfo(get_obj)
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': {
                    'title': depart_obj.title,
                    'id': depart_obj.id
                }
            }, safe=False)


def query_activityinfo(request):
    rst = {}
    # if request.GET.get("id"):
    #     rst['id'] = request.GET.get("id")
    if request.GET.get("name"):
        rst['name'] = request.GET.get("name")
    if request.GET.get("place"):
        rst['place'] = request.GET.get("place")
    if request.GET.get("start_time"):
        rst['start_time'] = request.GET.get("start_time")
    if request.GET.get("lasting_time"):
        rst['lasting_time'] = request.GET.get("lasting_time")
    if request.GET.get("score"):
        rst['score'] = request.GET.get("score")
    if request.GET.get("activity_status"):
        rst['activity_status'] = request.GET.get("activity_status")
    return rst


class ActivityDetails(View):
    def post(self, request):
        return HttpResponse('post ActivityDetails')

    def get(self, request):
        get_obj = {
            'id': request.GET.get('id'),
        }
        activity_obj = activityInfo(get_obj)
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': {
                    'name': activity_obj.name,
                    'place': activity_obj.place,
                    'start_time': activity_obj.start_time,
                    'lasting_time': activity_obj.lasting_time,
                    'score': activity_obj.score,
                    'activity_status': activity_obj.activity_status,
                    'id': activity_obj.id
                }
            }, safe=False)



class ActivityAdd(View):
    def post(self, request):
        return HttpResponse('post ActivityAdd')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_activityinfo(request)
        insertActivity(rst)
        return HttpResponse('get ActivityAdd Success')


class ActivityEdit(View):
    def post(self, request):
        return HttpResponse('post ActivityEdit')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_activityinfo(request)
        uid = request.GET.get("id")
        editActivity(uid, rst)
        return HttpResponse('get ActivityEdit Success')


class ActivityDelete(View):
    def post(self, request):
        return HttpResponse('post ActivityDelete')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        nid = request.GET.get("id")
        deleteActivity(nid)
        return HttpResponse('get ActivityDelete Success')


class ActivityList(View):
    def post(self, request):
        return HttpResponse('post ActivityList')

    def get(self, request):
        rst = {}
        if request.GET.get('search'):
            rst['search'] = request.GET.get('search')
        if request.GET.get('search_type'):
            rst['search_type'] = request.GET.get('search_type')
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET.get('pageStart')
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET.get('pagesize')
        data_dict = json.loads(serializers.serialize("json", activityList(rst)))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)


mock_users = {
    'admin-token': {
        'roles': ['admin'],
        'introduction': 'I am a super administrator',
        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        'name': 'Super Admin'
    },
    'editor-token': {
        'roles': ['editor'],
        'introduction': 'I am an editor',
        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        'name': 'Normal Editor'
    }
}
mock_tokens = {
  'admin': {
    'token': 'admin-token'
  },
  'editor': {
    'token': 'editor-token'
  }
}


class UserLogin(View):
    def post(self, request):
        return HttpResponse('post login')

    def get(self, request):
        get_obj = {
            'username': request.GET.get('username'),
            'password': request.GET.get('password')
        }
        user_obj = userInfo(get_obj)

        print('user_obj.phone')
        print(user_obj.phone)
        data_dict = {
            'username': user_obj.username,
            'id': user_obj.id
        }
        encoded_token = jwt.encode(data_dict, "secret", algorithm="HS256")
        return_obj = {
            'token': encoded_token,
            'superAdmin': user_obj.superAdmin,
            'permission_name': user_obj.permission.name,
            'permission_type': user_obj.permission.content_type,

        }
        if user_obj:
            print('have user_obj')
            return_data = {
                'message': 'success',
                'code': 20000,
                'data': return_obj
            }
            return JsonResponse(return_data)
        else:
            return_data = {
                'message': 'fail',
                'code': 100,
                'data': return_obj
            }
            print('no user_obj')
            return JsonResponse(return_data, safe=False)


class User_Info(View):
    def post(self, request):
        return HttpResponse('post User_Info')

    def get(self, request):
        token = request.GET.get('token')
        decode_token = jwt.decode(token, "secret", algorithms=["HS256"])
        # token_obj = json.loads(decode_token)
        # print(str(token_obj))
        get_obj = {
            'id': decode_token['id'],
        }
        user_obj = userInfo(get_obj)
        data_dict = {
            'roles': ['admin'],
            'introduction': '',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': user_obj.name,
            'permission_name': user_obj.permission.name,
            'permission_type': user_obj.permission.content_type,
          }
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': data_dict
            }, safe=False)


class UserDetails(View):
    def post(self, request):
        return HttpResponse('post UserDetails')

    def get(self, request):
        get_obj = {
            'id': request.GET.get('id'),
        }
        user_obj = userInfo(get_obj)
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': {
                    'username': user_obj.username,
                    'name': user_obj.name,
                    'phone': user_obj.phone,
                    'workNo': user_obj.workNo,
                    'depart_id': user_obj.depart_id,
                    'depart_name': user_obj.depart.title,
                    'permission_id': user_obj.permission_id,
                    'permisstion_name': user_obj.permission.name,
                    'permisstion_content': user_obj.permission.content_type,
                    'identityCard': user_obj.identityCard,
                    'id': user_obj.id,
                    'password': user_obj.password
                }
            }, safe=False)


class PermissionList(View):
    def post(self, request):
        return HttpResponse('post UserList')

    def get(self, request):
        rst = {}
        if request.GET.get('search'):
            rst['search'] = request.GET.get('search')
            rst['search_type'] = 'title'
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET.get('pageStart')
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET.get('pagesize')
        data_dict = json.loads(serializers.serialize("json", permissionList(rst)))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)

