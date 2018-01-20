from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from urls_collector import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'documents', views.DocumentViewSet)
router.register(r'urls', views.URLViewSet)

documents_router = routers.NestedDefaultRouter(
    router,
    r'documents',
    lookup='document'
)

documents_router.register(
    r'urls',
    views.URLViewSet,
    base_name='document-urls'
)

urls_router = routers.NestedDefaultRouter(
    router,
    r'urls',
    lookup='url'
)

urls_router.register(
    r'documents',
    views.DocumentViewSet,
    base_name='url-documents'
)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(documents_router.urls)),
    url(r'^', include(urls_router.urls)),
]
