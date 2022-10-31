# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Serializers imports
from apps.users.api.serializers import (
    UserSerializer,
    UserListSerializer
)


# Models imports
from apps.users.models import User


# Views
@api_view(['GET', 'POST'])
def user_api_view(request):
    """
    Listar y crear usuarios.
    """

    # List
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserListSerializer(users, many=True)

        return Response(data=users_serializer.data,status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        # Validación
        if user_serializer.is_valid():

            # User
            user_serializer.save()
            return Response(data=user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk):
    """
    Detallar, actualizar y eliminar un usuario.
    """

    # Validacion
    try:
        user = User.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Usuario no encontrado'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data)

    # Update
    elif request.method == 'PUT':
        user_serializer = UserSerializer(user, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()

            return Response(data=user_serializer.data)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    elif request.method == 'DELETE':
        user.delete()

        return Response(
            {'message': 'Usuario eliminado correctamente'},
            status=status.HTTP_200_OK
        )