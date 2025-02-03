from django.urls import path
from apis.transactions.views import TransactionListCreateView, TransactionRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('api/<str:account_number>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-detail'),
]
