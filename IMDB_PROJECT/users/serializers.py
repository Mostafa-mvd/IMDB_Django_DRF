from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSignUpSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    
    def to_representation(self, instance):
        result = super().to_representation(instance)
        del result['password']
        return result
        
    class Meta:
        model = get_user_model()
        fields = ('username',
                  'password', 
                  'first_name',
                  'last_name',
                  'email')

