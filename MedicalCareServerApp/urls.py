"""WXProgram URL Configuration for amniocentesisAppoint
second-level interface(functions): send_sms_code, submit_form
"""


from django.urls import path
from .views import UserAdd, UserEdit, UserList, UserDelete, DepartAdd, DepartEdit, DepartDelete, DepartList, \
    ActivityList, ActivityEdit, ActivityDelete, ActivityAdd, UserLogin, User_Info, UserDetails, DepartDetails, \
    ActivityDetails


urlpatterns = [
    path("user/add", UserAdd.as_view(), name="user_add"),
    path("user/edit", UserEdit.as_view(), name="user_edit"),
    path("user/list", UserList.as_view(), name="user_list"),
    path("user/delete", UserDelete.as_view(), name="user_delete"),
    path("user/login", UserLogin.as_view(), name="UserLogin"),
    path("user/info", User_Info.as_view(), name="UserInfo"),
    path("user/details", UserDetails.as_view(), name="UserDetails"),
    path("depart/add", DepartAdd.as_view(), name="depart_add"),
    path("depart/edit", DepartEdit.as_view(), name="depart_edit"),
    path("depart/list", DepartList.as_view(), name="depart_list"),
    path("depart/delete", DepartDelete.as_view(), name="depart_delete"),
    path("depart/details", DepartDetails.as_view(), name="depart_delete"),
    path("activity/add", ActivityAdd.as_view(), name="activity_add"),
    path("activity/edit", ActivityEdit.as_view(), name="activity_edit"),
    path("activity/list", ActivityList.as_view(), name="activity_list"),
    path("activity/delete", ActivityDelete.as_view(), name="activity_delete"),
    path("activity/details", ActivityDetails.as_view(), name="depart_delete"),
]