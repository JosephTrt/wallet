# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Serializers imports
from apps.transaction.api.serializers import (
    TransactionSerializer,
    TransactionListSerializer
)


# Models imports
from apps.transaction.models import Transaction


# Views
@api_view(['GET', 'POST'])
def transaction_api_view(request):

    # List
    if request.method == 'GET':
        transaction = Transaction.objects.all().values('id', 'date', 'amount', 'operation_type')
        transaction_serializer = TransactionListSerializer(transaction, many=True)

        return Response(data=transaction_serializer.data, status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':


        transaction_serializer = TransactionSerializer(data=request.data)

        # Validación
        if transaction_serializer.is_valid():

            # User
            transaction_serializer.save()
            return Response(data=transaction_serializer.data, status=status.HTTP_201_CREATED)

        return Response(transaction_serializer.errors)


@api_view(['GET'])
def transaction_detail_view(request, pk):
    """
    Detallar la operacion
    """

    # Validacion
    try:
        transaction = Transaction.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Cuenta no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        account_serializer = TransactionSerializer(transaction)

        return Response(account_serializer.data)