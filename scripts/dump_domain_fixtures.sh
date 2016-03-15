#!/usr/bin/env bash
python manage.py dumpdata --indent=2 --natural-primary players.Domain players.Influence players.Population players.Session
