from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username","password","first_name","last_name","phone_number","bio","updated_at",
        ]
        read_only_fields = ["updated_at"]

def create(self, validated_data):
    user = CustomUser.objects.create_user(
        username=validated_data["username"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
        phone_number=validated_data["phone_number"],
        bio=validated_data["bio"],
        password=validated_data["password"],
    )

    return user