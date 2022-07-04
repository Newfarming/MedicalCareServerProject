from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
# from app01.models import Admin
from util.medicalCare_db import userInfo
import jwt
from django.http import JsonResponse
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # 0. 放行不需要验证的网页
        # print(request.path_info)
        response = self.get_response(request)
        # response.setHeader("Access-Control-Allow-Origin", "*");
        # response.setHeader("Access-Control-Allow-Methods", "POST, GET, PUT, OPTIONS, DELETE");
        # print('request.path_info')
        # print(request.path_info)
        # token = request.META.get("HTTP_TOKEN")
        # print('middleware token')
        # print(token)
        # return response
        if request.path_info in ["/MedicalCareServerApp/user/login", "/MedicalCareServerApp/user/info",
                                 "/MedicalCareServerApp/permission/list"]:
            print('进入')
            return response
        # token = request.META.get("HTTP_TOKEN")
        g_token = request.GET.get('token')
        # print('middleware token')
        # print(token)
        print('middleware g_token')
        print(g_token)
        if not g_token:
            return JsonResponse({
                'message': '权限认证失败，没有token',
                'code': 20000,
                'data': 'fail'
            }, safe=False)

        decode_token = jwt.decode(g_token, "secret", algorithms=["HS256"])
        get_obj = {
            'id': decode_token['id'],
        }
        user_obj = userInfo(get_obj)
        permission_type = user_obj.permission.content_type
        permission_content = list(permission_type.split(','))
        # print('request.path_info 非登陆')
        # print(request.path_info)
        if request.path_info in ["/MedicalCareServerApp/user/add"]:
            if '1' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/user/delete"]:
            if '2' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/user/list", "/MedicalCareServerApp/user/details"]:
            print('user List middleware')
            if '3' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/user/edit"]:
            if '4' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/depart/add"]:
            if '5' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/depart/delete"]:
            if '6' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/depart/list", "/MedicalCareServerApp/depart/details"]:
            print('depart List middleware')
            if '7' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/depart/edit"]:
            if '8' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/activity/add"]:
            if '9' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/activity/delete"]:
            if '10' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/activity/list", "/MedicalCareServerApp/activity/details"]:
            print('depart List middleware')
            if '11' in permission_content:
                return response
        if request.path_info in ["/MedicalCareServerApp/activity/edit"]:
            if '12' in permission_content:
                return response


"""
# Django 1.10版本之前中间的定义
class M1(MiddlewareMixin):
     # 中间件 1

    def process_request(self, request):
        print("M1 进来")

    def process_response(self, request, response):
        print("M1 出去")
        return response


class M2(MiddlewareMixin):
    # 中间件 2

    def process_request(self, request):
        print("M2 进来")

    def process_response(self, request, response):
        print("M2 出去")
        return response


# Django 1.10版本之后中间的定义
class M3:
    def __init__(self, get_response):
        self.get_response = get_response
        print("M3 初始化")

    def __call__(self, request):
        print("M3 view调用前")
        response = self.get_response(request)
        print("M3 view被调用后")
        return response

"""
