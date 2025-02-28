from django.urls import path
from Trainer.views import *

urlpatterns=[
    path('Trainer_home', Trainer_home, name='Trainer_home'),
    path('Trainer_login', Trainer_login, name='Trainer_login'),
    path('Trainer_logout',Trainer_logout, name='Trainer_logout'),
    path('start_mock', start_mock, name='start_mock'),
]