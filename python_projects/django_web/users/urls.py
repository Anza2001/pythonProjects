#  -*- UTF-8 -*- #
"""
@filename:urls.py
@author:Anza
@time:2023-07-22
"""

from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

""" 为应用程序users定义URL模式"""

urlpatterns = [
    # 登陆页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销页面
    path('logout/', views.logout_view, name='logout'),
    # 注册用户
    path('register/', views.register, name='register')
]
