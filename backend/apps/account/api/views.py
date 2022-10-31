# Imports
import random


# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Serializers imports
from apps.account.api.serializers import (
    AccountSerializer,
    AccountListSerializer
)



# Models imports
from apps.account.models import Account
from apps.users.models import User


# Views
@api_view(['GET', 'POST'])
def account_api_view(request):

    # List
    if request.method == 'GET':
        account = Account.objects.all().values('id', 'user', 'account_number', 'alias')
        account_serializer = AccountListSerializer(account, many=True)

        return Response(data=account_serializer.data,status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':

        user = User.objects.get(id=request.data['user_id'])
        alias = str(user.username) + '.wallet'

        data = {
            'user': request.data['user_id'],
            'account_number': random.randint(0, 100000),
            'alias': alias,
            'amount': 0
        }

        account_serializer = AccountSerializer(data=data)

        # Validación
        if account_serializer.is_valid():

            # User
            account_serializer.save()
            return Response(data=account_serializer.data, status=status.HTTP_201_CREATED)

        return Response(account_serializer.errors)


@api_view(['GET'])
def account_detail_view(request, pk):
    """
    Detallar una cuenta
    """

    # Validacion
    try:
        account = Account.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Cuenta no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        account_serializer = AccountSerializer(account)

        return Response(account_serializer.data)