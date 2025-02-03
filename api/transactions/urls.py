from django.urls import path
from api.transactions.views import TransactionListCreateView, TransactionRetrieveUpdateDeleteView

urlpatterns = [
    path('api/v1/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('api/v1/<int:pk>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-detail'),
]
