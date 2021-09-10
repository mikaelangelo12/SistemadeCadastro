from rest_framework import serializers
from .models import novoPaciente

class novoPacienteSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = novoPaciente
        fields = ['id','nome', 'sobreNome','datadeNascimento', 'cpf', 'Endereço', 'Bairro', 'Cidade', 'Cep', 'sus', 'telefone', 'email' ]