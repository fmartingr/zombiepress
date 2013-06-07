Setup
=====

============
Installation
============

::

    git clone git@github.com:fmartingr/zombiepress.git

=============
Configuration
=============

Zombiepress contains multiple environment variables that you can use to tweak
your installation, these are:

ALLOWED HOSTS
-------------

**Default:** ''

DEBUG
-----

**Default:** False

TIME_ZONE
---------

**Default:** Europe/Madrid

LANGUAGE_CODE
-------------

**Default:** en-us

MEDIA_ROOT
----------

**Default:** /media/

STATIC_ROOT
-----------

**Default:** /static/

DATABASE_URL
------------

**Default:** `nothing` (uses sqlite as database)

Refer to: https://github.com/kennethreitz/dj-database-url

SENTRY_DSN
----------

**Default:** `nothing` (don't loads raven)

Refer to: http://raven.readthedocs.org/en/latest/config/django.html

ZOMBIEPRESS_THEME
-----------------

**Default:** default

MULTILANGUAGE
-------------

**Default:** False
