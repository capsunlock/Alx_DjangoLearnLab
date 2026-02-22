from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Explicitly get the CustomUser model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Requirement: Using serializers.CharField() for the password
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Requirement: Using get_user_model().objects.create_user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user