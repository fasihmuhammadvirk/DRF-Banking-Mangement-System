from rest_framework import generics
from .models import Bank
from .serializers import BankSerializer


class BankListCreateView(generics.ListCreateAPIView):
    """
    GET: List all banks
    POST: Create a new bank
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific bank
    PATCH/PUT: Update a specific bank
    DELETE: Delete a specific bank
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
