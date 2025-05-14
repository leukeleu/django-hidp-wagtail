# Frontend

This directory houses frontend code and resources.

## Structure

## `./assets`

Uncompiled assets such as stylesheets that need to be processed by a build tool (e.g. Tailwind CSS, PostCSS, SASS or
a combination of these) are stored in the `assets` directory.

The output of the build tool is stored in the `../var/dist` directory, which is collected by Django's `collectstatic`.

## `./static`

Files that do not need to be processed by a build tool are stored in the `static` directory.
The contents of this directory is copied (collected) by Django's `collectstatic` management command.

## `./templates`

Django templates are placed in the `templates` directory.

## Icons

The base template already includes all the favicons for iOS and Android. You can replace the default Leukeleu icons
with the project specific icons. Generate a new favicon with https://favicon.io/ and place them in the `./static/icons`
directory.
