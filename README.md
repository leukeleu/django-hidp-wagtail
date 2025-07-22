# HIdP Wagtail

A Wagtail-themed template and integration pack for [Hello, ID Please (HIdP)](https://github.com/leukeleu/django-hidp), providing improved authentication, account management, and security for Wagtail-based Django projects.

## Features

- Wagtail-styled templates for HIdP authentication and account management flows.
- Middleware to enforce OTP (One-Time Password) for Wagtail admin access.
- Context processor for account management links.
- Custom admin menu item for account security.
- CSS for consistent look and feel with Wagtail.

## Installation

1. Install the package (from PyPI or your local source):

    ```sh
    pip install django-hidp-wagtail
    ```

2. Add to your `INSTALLED_APPS` **above** `hidp` in your Django settings:

    ```python
    INSTALLED_APPS = [
        # ...
        "hidp_wagtail",  # Should be above "hidp" for templates to work
        "hidp",
        # ...
    ]
    ```

3. Set the Wagtail admin login URL to use HIdP:

    ```python
    WAGTAILADMIN_LOGIN_URL = 'hidp_accounts:login'
    ```

4. Add the context processor for account management links:

    ```python
    TEMPLATES = [
        {
            # ...
            'OPTIONS': {
                'context_processors': [
                    # ...
                    "hidp_wagtail.context_processors.account_management_links",
                ],
            },
        },
    ]
    ```

5. (Recommended) Add the OTP middleware to protect Wagtail admin:

    ```python
    MIDDLEWARE = [
        # ...
        "hidp_wagtail.middleware.OTPRequiredForWagtailAdminMiddleware",
        # ...
    ]
    ```

## Usage

- The package provides templates for both pre-login and post-login HIdP flows, styled for Wagtail.
- Account management links are available in the context for use in templates.
- The middleware [`OTPRequiredForWagtailAdminMiddleware`](hidp_wagtail/middleware.py) ensures only OTP-verified users with admin access can use the Wagtail admin.

## Development

- Lint and check: `make lint`
- Build: `make build`
- See [Makefile](Makefile) for more commands.

## License

[BSD-3-Clause](LICENSE)

## Links

- [Source code](https://github.com/leukeleu/django-hidp-wagtail/)
- [Issues](https://github.com/leukeleu/django-hidp-wagtail/issues)
