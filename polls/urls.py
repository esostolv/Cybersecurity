from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin, auth

from . import views
from.views import indexView, eventView, addView, deleteView, changePassword

urlpatterns = [
    path('', indexView, name='home'),
    path('events/<int:userid>', eventView, name='events'),
    path('add/', addView, name='add'),
    path('events/add/', addView, name='add'),
    path('events/delete/', deleteView, name='delete'),
    path('changePassword/', changePassword, name='changePassword'),

]
