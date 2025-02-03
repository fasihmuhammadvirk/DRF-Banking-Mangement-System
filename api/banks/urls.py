from django.urls import path
from .views import BankListCreateView, BankRetrieveUpdateDeleteView

urlpatterns = [
    path('api/v1/', BankListCreateView.as_view(), name='bank-list-create'),
    path('api/v1/<int:pk>/', BankRetrieveUpdateDeleteView.as_view(), name='bank-detail'),
]
