# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=250, blank=False)
    urls = models.ManyToManyField(
        'URL',
        through='Occurence',
        through_fields=('document', 'url'),
    )

    class Meta:
        ordering = ('created', )

    def get_urls_count(self):
        return self.urls.count()

    @classmethod
    def create_from_file(cls, file_object):
        instance = cls.objects.create(
            filename=file_object.name
        )

        return instance


class URL(models.Model):
    url = models.CharField(max_length=2000, blank=False)
    documents = models.ManyToManyField(
        'Document',
        through='Occurence',
        through_fields=('url', 'document'),
    )

    def get_documents_count(self):
        return self.documents.count()


class Occurence(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
