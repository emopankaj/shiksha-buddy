from rest_framework import serializers

from admin_panel.page_models import GenericPage
from .page_models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericPage
        fields = "__all__"
