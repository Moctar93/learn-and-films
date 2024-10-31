#!/bin/bash

# Lancer le serveur Django sur le port 8000 en arrière-plan
echo "Démarrage du serveur Django sur le port 8000..."
(cd backend && python3 manage.py runserver 8000) &

# Attendre quelques secondes pour laisser le temps au backend de démarrer
sleep 5

# Lancer le serveur React
echo "Démarrage du serveur React..."
(cd frontend/learn-and-films && npm start)

