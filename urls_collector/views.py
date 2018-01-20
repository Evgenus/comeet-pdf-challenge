# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import renderers
from urls_collector.models import Document
from urls_collector.models import URL
from urls_collector.serializers import DocumentSerializer
from urls_collector.serializers import URLSerializer


class DocumentViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    """
    A view set for documents
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def list(self, request, url_pk=None):
        queryset = self.queryset
        if url_pk is not None:
            queryset = queryset.filter(urls__id=url_pk)

        serializer = self.serializer_class(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, url_pk=None):
        objects = self.queryset.get(pk=pk)
        serializer = self.serializer_class(
            objects, context={'request': request}, many=False)
        return Response(serializer.data)


class URLViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view set for urls
    """
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def list(self, request, document_pk=None):
        queryset = self.queryset
        if document_pk is not None:
            queryset = queryset.filter(documents__id=document_pk)

        serializer = self.serializer_class(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, document_pk=None):
        objects = self.queryset.get(pk=pk)
        serializer = self.serializer_class(
            objects, context={'request': request}, many=False)
        return Response(serializer.data)
