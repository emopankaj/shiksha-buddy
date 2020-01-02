from rest_framework import viewsets
from rest_framework.response import Response

from admin_panel.menu_models import MenuItem
from admin_panel.page_models import TextImagePage, ContactPage
from admin_panel.serializers import GenericPageSerializer, TextImagePageSerializer, ContactPageSerializer, \
    MenuItemSerializer


# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class PageViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        text_image_page_queryset = TextImagePage.objects.all()
        text_image_page_serializer = TextImagePageSerializer(text_image_page_queryset, many=True)
        contact_page_queryset = ContactPage.objects.all()
        contact_page_serializer = ContactPageSerializer(contact_page_queryset, many=True)

        result = {'TextImagePage': text_image_page_serializer.data,
                  'ContactPage': contact_page_serializer.data}
        return Response(result)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            if self.request.data['pageType'] == TextImagePage.__name__:
                return TextImagePageSerializer

            return ContactPageSerializer

        return GenericPageSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
