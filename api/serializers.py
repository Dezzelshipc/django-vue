from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email has already registered")
        return email

    def validate_username(self, username):
        if username in ['null', 'undefined']:
            raise serializers.ValidationError("This username is forbidden to use")
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username has already registered")
        return username

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegisterSerializer, self).create(validated_data)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, username):
        if username in ['null', 'undefined']:
            raise serializers.ValidationError("This username is forbidden to use")
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username doesn't exists")
        return username

    def validate(self, attrs):
        if not check_password(attrs['password'], User.objects.filter(username=attrs['username']).values().get()['password']):
            raise serializers.ValidationError("This user doesn't exists")
        return super().validate(attrs)

class UserSerializerAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'created_at']