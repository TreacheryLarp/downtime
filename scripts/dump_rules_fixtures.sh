#!/usr/bin/env bash
python manage.py dumpdata --indent=2 --natural-primary players.ActionOption players.ActionType players.Age players.Clan players.Discipline players.Title
