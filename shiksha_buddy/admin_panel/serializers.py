from rest_framework import serializers

from admin_panel.menu_models import MenuItem
from admin_panel.page_models import GenericPage, TextImagePage, ContactPage


# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'


class GenericPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericPage
        fields = '__all__'


class TextImagePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextImagePage
        fields = '__all__'


class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
