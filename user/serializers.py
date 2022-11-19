from rest_framework import serializers

from .models import UserEntity


class UserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=False)
    first_name = serializers.CharField(required=True, max_length=32)
    last_name = serializers.CharField(required=True, max_length=32)
    username = serializers.CharField(required=True, max_length=32)
    password = serializers.CharField(required=True, max_length=32)

    def create(self, validated_data) -> UserEntity:
        """
        Create a new user
        :param validated_data: Data — (first_name, last_name, username, password)
        :return: User instance
        """
        user = UserEntity.objects.create(**validated_data)
        return user

    def update(self, instance: UserEntity, validated_data) -> UserEntity:
        """
        Update User and return
        :param instance: Old instance of User
        :param validated_data: Data — (first_name, last_name, username, password)
        :return: Updated instance of User
        """
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance

    class Meta:
        model = UserEntity


class CredentialSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=32)
    password = serializers.CharField(required=True, max_length=32)

    def validate(self, data):
        username = data.get("username", "None")
        password = data.get("password", "None")
        is_authenticated = self.login(username=username, password=password)

        return is_authenticated

    def login(self, username, password):
        """
        World's most basic authentication :D
        Details: https://www.youtube.com/watch?v=dQw4w9WgXcQ
        """
        try:
            UserEntity.objects.get(username=username, password=password)
            return True
        except UserEntity.DoesNotExist:
            raise False
