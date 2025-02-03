from django.urls import path
from apis.accounts.views import AccountListCreateView, AccountRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', AccountListCreateView.as_view(), name='account-list-create'),
    path('api/<int:pk>/', AccountRetrieveUpdateDeleteView.as_view(), name='account-detail'),

]
