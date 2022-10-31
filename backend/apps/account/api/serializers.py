# Rest imports
from rest_framework import serializers

# Models imports
from apps.account.models import Account


# Serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'user': instance['user'],
            'account_number': instance['account_number'],
            'alias': instance['alias']
        }