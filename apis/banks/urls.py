from django.urls import path
from apis.banks.views import BankListCreateView, BankRetrieveUpdateDeleteView

urlpatterns = [
    path('api/v1/', BankListCreateView.as_view(), name='bank-list-create'),  # List & Create
    path('api/v1/<int:pk>/', BankRetrieveUpdateDeleteView.as_view(), name='bank-detail'),  # Retrieve, Update & Delete
]
