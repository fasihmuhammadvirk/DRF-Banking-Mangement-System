from rest_framework import generics
from apis.accounts.models import Account
from apis.accounts.serializers import AccountSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
