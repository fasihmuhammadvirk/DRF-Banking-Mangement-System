from rest_framework import serializers
from apis.transactions.models import Transaction
from apis.accounts.models import Account

class TransactionSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(write_only=True)
    transactions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account_number', 'amount', 'transaction_type', 'created_at', 'transactions']

    def get_transactions(self, obj):
        """Retrieve all transactions for the given account number."""
        account_number = self.context.get('account_number')  # Get from context
        if account_number:
            transactions = Transaction.objects.filter(account__account_number=account_number).order_by('-created_at')
            return TransactionHistorySerializer(transactions, many=True).data
        return []

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

        data["account"] = account  # Store account object in validated data
        return data

    def create(self, validated_data):
        validated_data.pop('account_number')  # Remove account_number since we now have the account object
        transaction = Transaction.objects.create(**validated_data)

        account = validated_data['account']

        # Update account balance
        if transaction.transaction_type == 'deposit':
            account.balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            account.balance -= transaction.amount

        account.save()
        return transaction

class TransactionHistorySerializer(serializers.ModelSerializer):
    """Serializer for transaction history (simplified output)."""
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'created_at']
