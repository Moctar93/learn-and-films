#!/bin/bash

# Lancer le serveur Django en arrière-plan
(cd backend && python manage.py runserver 0.0.0.0:8000) &

# Lancer le serveur React
(cd frontend/learn-and-films && npm start)

