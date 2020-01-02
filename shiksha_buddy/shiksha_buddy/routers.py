from rest_framework import routers

from admin_panel.viewsets import PageViewSet, MenuItemViewSet

router = routers.DefaultRouter()
# router.register(r'article', ArticleViewSet)
router.register(r'page', PageViewSet, basename='GenericPage')
router.register(r'menu', MenuItemViewSet)
