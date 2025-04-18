"""
Wagtail override URLs.

Makes sure wagtail works properly with HIdP's login/logout views.

Include this module in the root URL configuration:

    from hidp_wagtail import urls as wagtail_hidp_urls

    # Wagtail
    path("", include(wagtail_hidp_urls)),  # Should be above wagtail and wagtail_admin
    path("wagtail-admin/", include(wagtailadmin_urls)),
    path("", include(hidp_urls)),
    path("", include(wagtail_urls)),

"""

from django.urls import path
from django.views.generic.base import RedirectView

from hidp.accounts import views


app_name = "hidp_wagtail"


auth_urls = [
    # Override the Wagtail logout view to redirect to / instead of the Wagtail login page
    path(
        "wagtail-admin/logout/", views.LogoutView.as_view(), name="wagtailadmin_logout"
    ),
    # Redirect Wagtail login to the custom login view so we only have one login page
    path(
        "wagtail-admin/login/",
        RedirectView.as_view(pattern_name="hidp_accounts:login"),
        name="wagtailadmin_login",
    ),
]

urlpatterns = auth_urls
