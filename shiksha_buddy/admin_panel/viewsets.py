from rest_framework import viewsets

from admin_panel.page_models import GenericPage
from admin_panel.serializers import PageSerializer
from .page_models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = GenericPage.objects.all()
    serializer_class = PageSerializer
