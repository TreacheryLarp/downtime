# Treachery app #

[ ![Codeship Status for TreacheryLarp/downtime](https://codeship.com/projects/c708dbd0-b06f-0133-9188-565ee1f98c10/status?branch=develop)](https://codeship.com/projects/132663)

This app handles management of the Treachery downtime system. This app is optimised for Dokku.

## Installation ##
1. Create a venv `python -m venv venv`
2. Set environ `source venv/bin/activate`
3. Install dependencies `python -m pip install -r requirements.txt`
4. Migrate database
5. Create superuser
6. Run server `python manage.py runserver`

### Dependencies ###
See the requirements.txt and runtime.txt files for dependencies.
