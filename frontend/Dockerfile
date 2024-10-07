# Utiliser l'image Nginx officielle depuis Docker Hub
FROM nginx:latest

# Copier les fichiers de configuration Nginx dans le conteneur
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Copier les fichiers du front-end dans le répertoire par défaut de Nginx
COPY . /var/www/html/learn-and-films

# Exposer le port 9000 pour accéder au site
EXPOSE 9000

# Démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]

