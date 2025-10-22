from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(rascunho=False)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
