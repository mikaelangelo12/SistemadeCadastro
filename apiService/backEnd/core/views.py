from rest_framework import viewsets
from .models import novoPaciente
from .serializers import novoPacienteSerializer

class novoPacienteViewSet(viewsets.ModelViewSet):
    queryset = novoPaciente.objects.all()
    serializer_class = novoPacienteSerializer