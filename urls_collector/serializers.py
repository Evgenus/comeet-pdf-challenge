from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.utils.field_mapping import get_url_kwargs

from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from urls_collector.models import Document
from urls_collector.models import URL


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = ('ref_self', 'id', 'filename', 'urls', 'ref_urls')

    ref_self = serializers.HyperlinkedIdentityField(
        **get_url_kwargs(Meta.model)
    )
    ref_urls = serializers.HyperlinkedIdentityField(
        view_name='document-urls-list',
        lookup_url_kwarg='document_pk'
    )
    urls = serializers.IntegerField(source='get_urls_count', read_only=True)


class DocumentCreateSerializer(serializers.Serializer):
    document = serializers.FileField()

    def create(self, validated_data):
        return Document.create_from_file(validated_data['document'])


class URLSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = URL
        fields = (
            'ref_self', 'id', 'url', 'alive', 'documents', 'ref_documents'
        )

    ref_self = serializers.HyperlinkedIdentityField(
        **get_url_kwargs(Meta.model)
    )
    ref_documents = serializers.HyperlinkedIdentityField(
        view_name='url-documents-list',
        lookup_url_kwarg='url_pk'
    )
    documents = serializers.IntegerField(
        source='get_documents_count',
        read_only=True
    )
