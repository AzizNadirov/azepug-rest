from dataclasses import fields
from rest_framework import serializers

from .models import Profile



class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'user_name', 'password']
        extra_kwargs = {'password':{"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['email', 'user_name', 'first_name', 'surname', 'start_date', 'image', 'about', 'contacts']
        read_only_fields = ['start_date', 'user_name']
    
class MiniProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user_name', 'image']
