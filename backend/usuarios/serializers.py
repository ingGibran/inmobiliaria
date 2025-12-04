from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id', 'date_joined')

    def create(self, validate_data):
        user = Usuario.objects.create_user(
            email=validate_data['email'],
            password=validate_data['password'],
            nombres=validate_data['nombres'],
            apellidos=validate_data['apellidos']
        )
        return user