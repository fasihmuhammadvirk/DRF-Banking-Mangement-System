from django.urls import path
from apis.users.views import UserListCreateView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path('api/v1/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/v1/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]
