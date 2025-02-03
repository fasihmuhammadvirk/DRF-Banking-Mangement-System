from django.urls import path
from apis.banks.views import BankListCreateView, BankRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', BankListCreateView.as_view(), name='bank-list-create'),  # List & Create
    path('api/<int:pk>/', BankRetrieveUpdateDeleteView.as_view(), name='bank-detail'),  # Retrieve, Update & Delete
]
