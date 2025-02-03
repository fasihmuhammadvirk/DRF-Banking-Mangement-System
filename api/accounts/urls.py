from django.urls import path
from .views import AccountListCreateView, AccountRetrieveUpdateDeleteView

urlpatterns = [
    path('api/v1/', AccountListCreateView.as_view(), name='account-list-create'),
    path('api/v1/<int:pk>/', AccountRetrieveUpdateDeleteView.as_view(), name='account-detail'),

]
