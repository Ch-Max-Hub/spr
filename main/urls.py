from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('add-info-file/', login_required(views.add_info_file), name='add_info_file'),
]