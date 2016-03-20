# Treachery app #
[![Build Status](https://travis-ci.org/TreacheryLarp/downtime.svg?branch=master)](https://travis-ci.org/TreacheryLarp/downtime)
[ ![Codeship Status for TreacheryLarp/downtime](https://codeship.com/projects/c708dbd0-b06f-0133-9188-565ee1f98c10/status?branch=master)](https://codeship.com/projects/132663)

This app handles management of the Treachery downtime system. This app is optimised for Dokku.

## Installation ##
There are two modes to run the app in.

### Development
1. Create a venv `python -m venv venv`
2. Set environ `source venv/bin/activate`
3. Install dependencies `python -m pip install -r requirements_development.txt`
4. Migrate database
5. Create superuser
6. Run server `python manage.py runserver`

### Production
1. Set the following environment variables on Dokku:
```json
DJANGO_PRODUCTION=true
DJANGO_ALLOWED_HOSTS=["your_domain"]
DATABASE_URL=postgres://
DJANGO_DEBUG=false
DJANGO_EMAIL_HOST
DJANGO_EMAIL_PASSWORD
DJANGO_EMAIL_USER
DJANGO_SECRET
```
2. Push master to dokku
3. Migrate database
4. Create superuser

### Dependencies ###
See the requirements.txt and runtime.txt files for dependencies.

### Fixtures
The system is intended to be flexible and support rules changes. To that effect the system stores a rules preset as fixtures.
