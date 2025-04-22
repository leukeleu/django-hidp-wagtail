# HIdP templates for Wagtail

## Overview

This package contains the HIdP templates for Wagtail.

## Installation

1. Install the package using pip:

```bash
pip install leukeleu-hidp-wagtail
```

2. Add the package to your `INSTALLED_APPS` in your Django settings:

```python
INSTALLED_APPS = [
    ...
    "hidp_wagtail",  # Should be above "hidp" for templates to work
]
```

3. Set the correct settings for your project:

```python
WAGTAILADMIN_LOGIN_URL = 'hidp_accounts:login'
```
