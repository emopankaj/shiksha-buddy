from rest_framework import serializers
from .page_models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

metaclass
context manager
