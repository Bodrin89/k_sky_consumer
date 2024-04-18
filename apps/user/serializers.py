from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.user.models import UserModel


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания пользователя."""

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'role')

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_hash = make_password(password)
        validated_data['password'] = password_hash
        return UserModel.objects.create(**validated_data)
