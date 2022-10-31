from rest_framework import serializers

# Models imports
from apps.wallet.models import Wallet


# Serializers
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ['transaction']


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'user': instance['user']
        }