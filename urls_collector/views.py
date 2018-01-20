# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import status 
from urls_collector.models import Document
from urls_collector.models import URL
from urls_collector.serializers import DocumentSerializer
from urls_collector.serializers import DocumentCreateSerializer
from urls_collector.serializers import URLSerializer


class DocumentRenderer(renderers.BrowsableAPIRenderer):
    def get_context(self, data, accepted_media_type, renderer_context):
        context = super(DocumentRenderer, self).get_context(
            data, accepted_media_type, renderer_context
        )
        serializer = DocumentCreateSerializer()
        context['display_edit_forms'] = isinstance(data, list)
        context['post_form'] = self.render_form_for_serializer(serializer)
        return context 


class DocumentViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    """
    A view set for documents
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    renderer_classes = (renderers.JSONRenderer, DocumentRenderer)

    def list(self, request, url_pk=None):
        queryset = self.queryset
        if url_pk is not None:
            queryset = queryset.filter(urls__id=url_pk)

        serializer = self.serializer_class(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def create(self, request):
        create_serializer = DocumentCreateSerializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        instance = create_serializer.save()
        display_serializer = self.get_serializer(instance)
        headers = self.get_success_headers(display_serializer.data)
        return Response(
            display_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        ) 


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
