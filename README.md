# Treachery app #
[![Build Status](https://travis-ci.org/TreacheryLarp/downtime.svg?branch=master)](https://travis-ci.org/TreacheryLarp/downtime)
[ ![Codeship Status for TreacheryLarp/downtime](https://codeship.com/projects/c708dbd0-b06f-0133-9188-565ee1f98c10/status?branch=master)](https://codeship.com/projects/132663)

This app handles management of the Treachery downtime system. The system is designed for Dokku/Heroku.

## Installation ##
There are two modes to run the app in.

### Development
1. Create a venv `python -m venv venv`
2. Set environ `source venv/bin/activate`
3. Install dependencies `python -m pip install -r requirements_development.txt`
4. Migrate database
5. Create superuser
6. Load fixtures ```python manage.py loaddata treachery_rules```
7. Run server `python manage.py runserver`

### Production
1. Set the following environment variables on Dokku:
```json
DJANGO_PRODUCTION=true
DJANGO_ALLOWED_HOSTS=your_domain,your_other_domain,your_third_domain
DATABASE_URL=postgres://
DJANGO_DEBUG=false
DJANGO_EMAIL_HOST=...
DJANGO_EMAIL_PASSWORD=...
DJANGO_EMAIL_USER=...
DJANGO_SECRET=...
```
2. Push master to dokku
3. Migrate database
4. Create superuser
5. Load fixtures ```python manage.py loaddata treachery_rules```

### Dependencies ###
See the requirements.txt and runtime.txt files for dependencies.

### Fixtures
The system is intended to be flexible and support rules changes. To that effect the system stores a rules preset as fixtures.

## License
Treachery Downtime System

Copyright (C) 2016  Erik Gärtner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
