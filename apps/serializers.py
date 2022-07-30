from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.tasks import send_register_email
from apps.models import Student, Teacher


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = Teacher
        fields = ('phone_number', 'subject_name', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match!')
        return validated_data


    def create(self, validated_data):
        """ this func is calling when self.save() is called"""
        phone_number = validated_data.get('phone_number')
        password = validated_data.get('password')
        user = Teacher.objects.create_user(phone_number=phone_number, password=password, subject_name=validated_data.get('subject_name'))
        return user

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'), phone_number=phone_number, password=password)
            if not user:
                message = 'unable to log in with provided credintials'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include "phone_number" amd "password".'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


    def create(self, validated_data):
        send_register_email(validated_data['email'])
        return super().create(validated_data) 


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


