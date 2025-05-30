from urllib.parse import urlparse

from django.conf import settings


def sentry_url(sentry_dsn):
    """
    Returns the url to the lazy Sentry Javascript SDK loader for the given
    sentry_dsn or None if the given sentry_dsn is invalid.

    Example:
    >>> sentry_url('https://00000000000000000000000000000000@o111111.ingest.sentry.io/2222222')
    'https://js.sentry-cdn.com/00000000000000000000000000000000.min.js'

    See also: https://docs.sentry.io/platforms/javascript/#lazy-loading-sentry
    """
    key = urlparse(sentry_dsn or "").username
    if key:
        return f"https://js.sentry-cdn.com/{key}.min.js"


def sentry_vars(context):
    return {
        "sentry_environment": getattr(settings, "SENTRY_ENVIRONMENT", None),
        "sentry_dsn": getattr(settings, "SENTRY_DSN", None),
        "sentry_url": sentry_url(getattr(settings, "SENTRY_DSN", None)),
    }
