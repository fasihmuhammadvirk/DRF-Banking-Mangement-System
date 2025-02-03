from rest_framework import serializers
from api.accounts.models import Account
from api.users.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'balance', 'account_number', 'bank', 'user']


class AccountUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user details in the account.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Account
        fields = ['user']
