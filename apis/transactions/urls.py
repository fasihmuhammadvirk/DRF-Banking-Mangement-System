from django.urls import path
from apis.transactions.views import TransactionListView
urlpatterns = [

    path('history/<str:account_number>', TransactionListView.as_view(), name='transactions-list'),
    # path('make/<str:account_number>', TransactionCreateView.as_view(), name='make-transaction'),

]
