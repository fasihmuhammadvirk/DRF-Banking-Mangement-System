from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.accounts.models import Account
from api.accounts.serializers import AccountSerializer, AccountUpdateSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter accounts by authenticated user.
        Admins can view all accounts.
        """
        user = self.request.user
        if user.is_staff:  # Allow admin to view all accounts
            return Account.objects.all()
        return Account.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        """
        Update user details in an account.
        """
        account = self.get_object()
        serializer = AccountUpdateSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
