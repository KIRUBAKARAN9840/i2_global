from rest_framework import viewsets
from .models import User, Notes
from .serializers import UserSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]

