from rest_framework.generics import CreateAPIView
from . import serializers


class CreateUser(CreateAPIView):
    serializer_class = serializers.UserSignUpSerializer
