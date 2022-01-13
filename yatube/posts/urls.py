# posts/urls.py

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'group/<slug:path>/',
        views.group_list,
        name='group_list'
        )
]
