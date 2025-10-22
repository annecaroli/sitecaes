from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
# Cria URLs para listagem, detalhe, criação, atualização e deleção em /posts/
router.register(r'posts', PostViewSet, basename='post')

# As URLs do router serão incluídas no arquivo principal
urlpatterns = router.urls