from rest_framework import generics
from apps.models import Student, Teacher
from rest_framework.viewsets import ModelViewSet
from apps.serializers import RegisterSerializer, StudentCreateSerializer, StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = RegisterSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer()


    def get_serializer_class(self):
        if self.action == 'create':
            print(self)
            return StudentCreateSerializer
        return StudentSerializer

    @action(methods=['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset().filter(
            Q(email__icontains=q)|
            Q(name__icontains=q)
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)   