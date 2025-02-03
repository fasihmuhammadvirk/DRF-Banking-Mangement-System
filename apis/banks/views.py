from rest_framework import generics
from apis.banks.models import Bank
from apis.banks.serializers import BankSerializer


class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
