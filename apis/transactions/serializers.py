from rest_framework import serializers
from apis.transactions.models import Transaction
from apis.accounts.models import Account


class TransactionSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(write_only=True)  # Accept account_number instead of account ID

    class Meta:
        model = Transaction
        fields = ['id', 'account_number', 'amount', 'transaction_type', 'created_at']

    def validate(self, data):

        account_number = data['account_number']
        transaction_type = data['transaction_type']
        amount = data['amount']

        try:
            account = Account.objects.get(account_number=account_number)
        except Account.DoesNotExist:
            raise serializers.ValidationError("Account not found.")

        if transaction_type == 'withdrawal' and account.balance < amount:
            raise serializers.ValidationError("Insufficient balance for withdrawal.")

        return data

    def create(self, validated_data):

        account_number = validated_data.pop('account_number')
        account = Account.objects.get(account_number=account_number)

        transaction = Transaction.objects.create(account=account, **validated_data)

        # Update account balance
        if transaction.transaction_type == 'deposit':
            account.balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            account.balance -= transaction.amount

        account.save()
        return transaction
