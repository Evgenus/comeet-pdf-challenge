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
        url__url="http://google.com",
        url__alive=True,
    )
    occurence2 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__url="http://msn.com",
        url__alive=True,
    )
    occurence3 = factory.RelatedFactory(
        OccurenceFactory,
        'document',
        url__url="http://some-malformed-urls.duh",
        url__alive=False,
    )


class TestGettersOneDocument(TestCase):
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
                "urls":3,
                "ref_urls":"http://testserver/documents/1/urls/"
            }
        ]
        self.assertEqual(response.json(), expected)

    def test_get_document(self):
        response = self.client.get('/documents/1/')
        self.assertEqual(response.status_code, 200)
        expected = {
            "ref_self":"http://testserver/documents/1/",
            "id":1,
            "filename": self.document.filename,
            "urls":3,
            "ref_urls":"http://testserver/documents/1/urls/"
        }
        self.assertEqual(response.json(), expected)

    def test_get_urls(self):
        response = self.client.get('/urls/')
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'ref_self': u'http://testserver/urls/1/',
                'id': 1,
                'url': "http://google.com",
                'alive': True,
                'documents': 1,
                'ref_documents': 'http://testserver/urls/1/documents/',
            },
            {
                'ref_self': u'http://testserver/urls/2/',
                'id': 2,
                'url': "http://msn.com",
                'alive': True,
                'documents': 1,
                'ref_documents': 'http://testserver/urls/2/documents/',
            },
            {
                'ref_self': u'http://testserver/urls/3/',
                'id': 3,
                'url': "http://some-malformed-urls.duh",
                'alive': False,
                'documents': 1,
                'ref_documents': 'http://testserver/urls/3/documents/',
            }
        ]
        self.assertEqual(response.json(), expected)

    def test_get_url(self):
        response = self.client.get('/urls/1/')
        self.assertEqual(response.status_code, 200)
        expected = {
            'ref_self': u'http://testserver/urls/1/',
            'id': 1,
            'url': "http://google.com",
            'alive': True,
            'documents': 1,
            'ref_documents': 'http://testserver/urls/1/documents/',
        }
        self.assertEqual(response.json(), expected)
