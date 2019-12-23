from django.db import models
from django.db.models import DecimalField


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class GenericPage(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=250)


class ContactPage(GenericPage):
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=250)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=50)


class TextImagePage(GenericPage):
    image = models.CharField(max_length=100)
    text = models.TextField()

