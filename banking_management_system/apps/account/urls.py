from django.urls import path
from . import views

urlpatterns = [

    path("user_account_list/", views.get_user_account_list, name='user_account_list'),

]
