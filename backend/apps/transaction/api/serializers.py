# Rest imports
from rest_framework import serializers

# Models imports
from apps.transaction.models import Transaction


# Serializers
class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
   
        


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'date': instance['date'],
            'amount': instance['amount'],
            'operation_type': instance['operation_type']
        }