from django.urls import path
from .views import BankListCreateView, BankRetrieveUpdateDeleteView

urlpatterns = [
    path('apis/v1/', BankListCreateView.as_view(), name='bank-list-create'),
    path('apis/v1/<int:pk>/', BankRetrieveUpdateDeleteView.as_view(), name='bank-detail'),
]
