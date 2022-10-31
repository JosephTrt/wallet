# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Serializers imports
from apps.wallet.api.serializer import (
    WalletSerializer,
    WalletListSerializer
)


# Models imports
from apps.wallet.models import Wallet
from apps.transaction.models import Transaction


# Views
@api_view(['GET', 'POST'])
def wallet_api_view(request):

    # List
    if request.method == 'GET':
        wallet = Wallet.objects.all().values('id', 'user')
        wallet_serializer = WalletListSerializer(wallet, many=True)

        return Response(data=wallet_serializer.data, status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':

        transactions = Transaction.objects.filter(credit_account=request.data['account']).first()

        data = {
            'user': request.data['user'],
            'account': request.data['account'],
            'transactions': transactions.id
        }

        wallet_serializer = WalletSerializer(data=data)

        # Validación
        if wallet_serializer.is_valid():

            # User
            wallet_serializer.save()
            return Response(data=wallet_serializer.data, status=status.HTTP_201_CREATED)

        return Response(wallet_serializer.errors)


@api_view(['GET', 'DELETE'])
def wallet_detail_view(request, pk):
    """
    Detallar la operacion
    """

    # Validacion
    try:
        wallet = Wallet.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Wallet no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data)
    
    # Delete
    elif request.method == 'DELETE':
        wallet.delete()

        return Response(
            {'message': 'Cuenta eliminada correctamente'},
            status=status.HTTP_200_OK
        )