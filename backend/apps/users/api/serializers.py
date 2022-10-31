# Rest imports
from rest_framework import serializers

# Models imports
from apps.users.models import User


# Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """
        Correción la encriptacion de la password al crear un usuario.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
    

    def update(self, instance, validated_data):
        """
        Correción la encriptacion de la password al editar un usuario.
        """
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()


        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }