from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('redeem', views.Redeem, name="redeem"),
    # path('login', views.Login, name="login"),
    # path('logout/', views.Logout, name="logout"),
    # path('students', views.Students, name="students"),
    # path('logsession', views.LogSession, name="logsession"),
    # path('logdoubtsession', views.LogDoubtSession, name="logdoubtsession"),
    # path('getweek', views.GetWeek, name="getweek"),
    # path('generatereport', views.GenerateReport, name="generatereport"),
]