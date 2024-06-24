from rest_framework import serializers
from .models import MemberLogin, MemberRegistration,ToDo

# create the serializers here

# serializers for login
class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberLogin
        fields = ["username", "password", "email"]

# serializers for registeration
class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberRegistration
        fields = ["firstName", "lastName", "email", "password", "comfirm_password"]

# serializers for the Todo
class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["activity"]

