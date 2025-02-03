from django.urls import path
from apis.users.views import UserListCreateView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]
