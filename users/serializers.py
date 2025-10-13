from .models import CustomeUser
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomeUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'profile_picture', 'password', 'password2']


    def validate(self, attri):
        if attri['password'] != attri['password2']:
            raise serializers.ValidationError({"message: passwords do not match"})
        return attri

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomeUser.objects.create_user(**validated_data)
        return user
