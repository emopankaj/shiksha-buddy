from rest_framework import routers
from admin_panel.viewsets import ArticleViewSet, PageViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'page', PageViewSet)
