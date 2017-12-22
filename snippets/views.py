# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from snippets.models import Snippet
from rest_framework import permissions
from snippets.serializers import SnippetSerializer
from snippets.models import UserSerializer
class SnippetList(generics.ListCreateAPIView):
    '''
    List all snippets or create a new snippet
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a snippet instance.
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer