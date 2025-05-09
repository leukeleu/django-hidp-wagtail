from hidp.config import urls as hidp_urls
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Project
    # Hello, ID Please
    path("", include(hidp_urls)),
    # Django Admin
    path("django-admin/", admin.site.urls),
    # Wagtail
    path("sitemap.xml", sitemap),
    path("wagtail-admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
]
