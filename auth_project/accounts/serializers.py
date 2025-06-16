from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

# ✅ 1. Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # password GET मध्ये दिसू नये

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# ✅ 2. Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Invalid email or password")
