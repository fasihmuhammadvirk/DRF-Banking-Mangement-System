from rest_framework import serializers
from apis.accounts.models import Account
from apis.users.models import User
from apis.banks.models import Bank
ß
class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)  # User-provided username
    bankname = serializers.CharField(write_only=True)  # User-provided bank name

    class Meta:
        model = Account
        fields = ["id", "username", "bankname", "balance", "account_number", "user", "bank"]
        extra_kwargs = {
            "user": {"read_only": True},  # Auto-set based on username
            "bank": {"read_only": True},  # Auto-set based on bank name
        }

    def validate(self, data):
        username = data.get("username")
        bankname = data.get("bankname")
        account_number = data.get("account_number")

        if not username or not bankname or not account_number:
            raise serializers.ValidationError("Username, bank name, and account number are required.")

        user = User.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError({"username": "User not found."})

        bank = Bank.objects.filter(name=bankname).first()
        if not bank:
            raise serializers.ValidationError({"bankname": "Bank not found."})

        # Check if the account with the same user & bank already exists
        if Account.objects.filter(user=user, bank=bank).exists():
            raise serializers.ValidationError("Account with this user and bank already exists.")

        data["user"] = user
        data["bank"] = bank
        return data

    def create(self, validated_data):
        validated_data.pop("username")
        validated_data.pop("bankname")
        return Account.objects.create(**validated_data)
