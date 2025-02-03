from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apis.transactions.models import Transaction
from apis.accounts.models import Account
from apis.transactions.serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):
        """Retrieve transaction history by account_number."""
        account_number = request.query_params.get('account_number')

        if not account_number:
            return Response({"error": "Account number is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            account = Account.objects.get(account_number=account_number)
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        transactions = Transaction.objects.filter(account=account).order_by('-created_at')
        serializer = TransactionSerializer(transactions, many=True, context={'account_number': account_number})
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
