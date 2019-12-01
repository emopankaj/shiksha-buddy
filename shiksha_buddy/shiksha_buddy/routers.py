from rest_framework import routers
from admin_panel.viewsets import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
