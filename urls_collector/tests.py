# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory

from django.test import TestCase
from django.test.client import RequestFactory

from urls_collector import models


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Document
        django_get_or_create = ('filename',)

    filename = factory.faker.Faker('file_name')


class URLFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.URL
        django_get_or_create = ('url',)

    alive = None
    url = factory.faker.Faker('file_path')


class OccurenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Occurence

    document = factory.SubFactory(DocumentFactory)
    url = factory.SubFactory(URLFactory)


class DocumentWithUrlsFactory(DocumentFactory):
    occurence1 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__alive=True
    )
    occurence2 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__alive=True
    )


class TestGetters(TestCase):
    def setUp(self):
        self.document = DocumentWithUrlsFactory()

    def test_get_documents(self):
        response = self.client.get('/documents/')
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                "ref_self":"http://testserver/documents/1/",
                "id":1,
                "filename": self.document.filename,
                "urls":2,
                "ref_urls":"http://testserver/documents/1/urls/"
            }
        ]
        self.assertEqual(response.json(), expected)

    def test_get_urls(self):
        response = self.client.get('/urls/')
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'ref_self': u'http://testserver/urls/1/',
                'id': 1,
                'url': self.document.urls.all()[0].url,
                'alive': False,
                'documents': 1,
                'ref_documents': 'http://testserver/urls/1/documents/',
            },
            {
                'ref_self': u'http://testserver/urls/2/',
                'id': 2,
                'url': self.document.urls.all()[1].url,
                'alive': False,
                'documents': 1,
                'ref_documents': 'http://testserver/urls/2/documents/',
            }
        ]
        self.assertEqual(response.json(), expected)
 

class DocumentWithUrlsFactory(DocumentFactory):
    occurence1 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__alive=True
    )
    occurence2 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__alive=True
    )
 

 