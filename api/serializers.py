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
            raise serializers.ValidationError("This email has been already registered")
        return email

    def validate_username(self, username: str):
        if username.lower() in ['null', 'undefined', 'all']:
            raise serializers.ValidationError("This username is forbidden to use")
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username has been already registered")
        return username

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegisterSerializer, self).create(validated_data)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Wrong username or password")
        return username

    def validate(self, attrs):
        if not check_password(attrs['password'], User.objects.filter(username=attrs['username']).values().get()['password']):
            raise serializers.ValidationError("Wrong username or password")
        return super().validate(attrs)

class UserSerializerAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'telegram', 'created_at', 'data']

class UserSerializerDataAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'data']

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['data']

class UserTelegramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['telegram']

    def validate_telegram(self, telegram):
        if ['', 'null', 'undefined', 0, None] in telegram:
            raise serializers.ValidationError('Telegram error')
        return telegram