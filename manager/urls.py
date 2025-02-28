from django.urls import path
from manager.views import *

urlpatterns=[
    path('manager_home', manager_home, name='manager_home'),
    path('add_emplyee', add_emplyee, name='add_emplyee'),
    path('manager_login', manager_login, name='manager_login'),
    path('manager_logout', manager_logout, name='manager_logout')
]