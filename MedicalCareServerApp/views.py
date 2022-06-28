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
    departList, insertActivity, editActivity, deleteActivity, activityList, userInfo
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
        return HttpResponse('get UserEdit Success')


class UserDelete(View):
    def post(self, request):
        return HttpResponse('post UserDelete')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        uid = request.GET.get("id")
        deleteUser(uid)
        return HttpResponse('get UserDelete Success')


class UserList(View):
    def post(self, request):
        rst = {}
        print('request search')
        print(request.GET.get('search'))
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
        data_dict = json.loads(serializers.serialize("json", userList(rst)))
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': data_dict
            }, safe=False)


class DepartAdd(View):
    def post(self, request):
        return HttpResponse('post DepartAdd')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = {'title': request.GET.get('title')}
        insertDepart(rst)
        return HttpResponse('get DepartAdd Success')


class UserInfo(View):
    def post(self, request):
        return HttpResponse('post UserInfo')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = {'title': request.GET.get('title')}
        insertDepart(rst)
        return HttpResponse('get UserInfo Success')


class DepartEdit(View):
    def post(self, request):
        return HttpResponse('post DepartEdit')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = {'title': request.GET.get('title')}
        nid = request.GET.get("id")
        editDepart(nid, rst)
        return HttpResponse('get UserEdit Success')


class DepartDelete(View):
    def post(self, request):
        return HttpResponse('post DepartDelete')

    def get(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        nid = request.GET.get("id")
        deleteDepart(nid)
        return HttpResponse('get UserDelete Success')


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
        data = serializers.serialize("json", activityList(rst))
        return HttpResponse(data, content_type="application/json")


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
        return_obj = {'token': encoded_token}
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
        print('token')
        print(token)
        decode_token = jwt.decode(token, "secret", algorithms=["HS256"])
        print('decode_token')
        print(decode_token)
        # token_obj = json.loads(decode_token)
        # print(str(token_obj))
        get_obj = {
            'id': decode_token['id'],
        }
        user_obj = userInfo(get_obj)

        print('User_Info user_obj.phone')
        print(user_obj.phone)
        data_dict = {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin'
          }
        return JsonResponse({
                'message': 'success',
                'code': 20000,
                'data': data_dict
            }, safe=False)


