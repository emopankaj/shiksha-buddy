from django.db.models import QuerySet
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
    # queryset = QuerySet().union(TextImagePage.objects.all()).union(ContactPage.objects.all())

    def list(self, request, *args, **kwargs):
        text_image_page_queryset = TextImagePage.objects.all()
        text_image_page_serializer = TextImagePageSerializer(text_image_page_queryset, many=True)
        contact_page_queryset = ContactPage.objects.all()
        contact_page_serializer = ContactPageSerializer(contact_page_queryset, many=True)

        text_image_pages = list(map(lambda x: self.attach_page_type_to_result(x, TextImagePage.__name__),
                                    text_image_page_serializer.data))
        contact_pages = list(map(lambda x: self.attach_page_type_to_result(x, ContactPage.__name__),
                                 contact_page_serializer.data))

        return Response(text_image_pages + contact_pages)

    def get_queryset(self):
        if self.request.data['pageType'] == TextImagePage.__name__:
            return TextImagePage.objects.all()

        return ContactPage.objects.all()

    def get_serializer_class(self):
        if self.request.data['pageType'] == TextImagePage.__name__:
            return TextImagePageSerializer

        return ContactPageSerializer

    @staticmethod
    def attach_page_type_to_result(result, pageType):
        result['pageType'] = pageType
        return result


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
