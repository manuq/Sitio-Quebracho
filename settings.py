#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010 Código Sur - Nuestra América Asoc. Civil / Fundación Pacificar.
# All rights reserved.
#
# This file is part of Cyclope.
#
# Cyclope is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyclope is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from cyclope.default_settings import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CYCLOPE_PROJECT_PATH = os.path.dirname(__file__)

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(CYCLOPE_PROJECT_PATH, 'db/site.db')

TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(CYCLOPE_PROJECT_PATH, 'media/')

STATIC_ROOT = os.path.join(CYCLOPE_PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'quebracho_sitio.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(CYCLOPE_PROJECT_PATH, 'templates'),
)

INSTALLED_APPS += (
    'quebracho_sitio',
)

LOGIN_REDIRECT_URL = '/inicio'


# Add real email account setup here for registration to work properly.

# The host to use for sending e-mail. Default: 'localhost'
EMAIL_HOST='smtp.gmail.com'

# Username to use for the SMTP server defined in EMAIL_HOST. If empty,
# Django won't attempt authentication. Default: '' (Empty string)
EMAIL_HOST_USER='anon.email.noreply'

# Password to use for the SMTP server defined in EMAIL_HOST. This setting
# is used in conjunction with EMAIL_HOST_USER when authenticating to the
# SMTP server. If either of these settings is empty, Django won't attempt
# authentication. Default: '' (Empty string)
EMAIL_HOST_PASSWORD='anon.email'

# Port to use for the SMTP server defined in EMAIL_HOST. Default: 25
EMAIL_PORT='587'

# Default e-mail address to use for various automated correspondence from
# the site manager(s). Default: 'webmaster@localhost'
#DEFAULT_FROM_EMAIL = ""

# The e-mail address that error messages come from, such as those sent to
# ADMINS and MANAGERS. Default: 'root@localhost'
#SERVER_EMAIL = ""

# Whether to use a TLS (secure) connection when talking to the SMTP server.
# Default: False
EMAIL_USE_TLS = True  # we set this to True for the sample email config

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
                    'mail_admins': {
                                    'level': 'ERROR',
                                    'class': 'django.utils.log.AdminEmailHandler'
                                }
                },
        'loggers': {
                    'django.request': {
                                    'handlers': ['mail_admins'],
                                    'level': 'ERROR',
                                    'propagate': True,
                                },
                }
}


# Cyclope settings

CYCLOPE_LOCAL_THEMES_DIR = os.path.join(CYCLOPE_PROJECT_PATH, 'templates/cyclope/themes/')
CYCLOPE_LOCAL_THEMES_MEDIA_PREFIX = '/media/local_themes/'

CYCLOPE_PREFIX = ''

#CYCLOPE_CONTACTS_PROFILE_MODULE = "app.model"
#CYCLOPE_CONTACTS_PROFILE_ADMIN_INLINE_MODULE = "project.app.admin.ProfileModuleInline"
#CYCLOPE_CONTACTS_PROFILE_TEMPLATE = "app/profile_template.html"

# possible values for TEXT_STYLE are:
# textile (saves markup, renders with corresponding filter)
# wysiwyg (rich text editor, saves HTML, renders with safe filter)
# raw (simple text area saves the raw input, renders with safe filter)

CYCLOPE_TEXT_STYLE = 'textile'


CYCLOPE_PAGINATION = {'TEASER' : 3, 'LABELED_ICON' : 5,
                      'FORUM' : 2, 'DETAIL': 5}


HAYSTACK_SITECONF = 'quebracho_sitio.search_sites'
HAYSTACK_WHOOSH_PATH = os.path.join(CYCLOPE_PROJECT_PATH, 'cyclope_project_index')

#FILEBROWSER_MAX_UPLOAD_SIZE = 1048576 # 10 MB

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gnqqvsqje(g9x1s)*s)ywr9%mw6q0se$s3u8(#b=s-jw544hw0'
