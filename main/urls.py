from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('etraps/', login_required(views.etraps), name='etraps'),
    path('users/', login_required(views.users), name='users'),
    path('add-info/', login_required(views.add_info), name='add_info'),
    path('add-info-file/', login_required(views.add_info_file), name='add_info_file'),
]