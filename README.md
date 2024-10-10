# Application de Gestion de Bibliothèque

## Description
Cette application permet aux utilisateurs de gérer une bibliothèque, en offrant des fonctionnalités telles que l'ajout de livres, l'emprunt de livres et la réservation de livres. L'application utilise une architecture basée sur Django pour le back-end et Vue.js pour le front-end, avec une API RESTful pour la communication entre les deux.

## Fonctionnalités
- **Gestion des livres** : Ajouter, modifier et supprimer des livres.
- **Emprunt de livres** : Les utilisateurs peuvent emprunter des livres disponibles.
- **Réservation de livres** : Les utilisateurs peuvent réserver des livres qui ne sont pas disponibles.
- **Liste des livres** : Affichage d'une liste des livres avec leurs informations (titre, auteur, statut).
- **Interface utilisateur** : Une interface conviviale développée avec Vue.js, permettant une interaction facile avec l'application.

## Technologies utilisées
- **Back-end** : Django, Django REST Framework
- **Front-end** : Vue.js
- **Base de données** : SQLite3 (facile à configurer et à utiliser pour le développement)
- **Gestion des requêtes HTTP** : Axios pour effectuer des appels API depuis le front-end vers le back-end.

## Installation
1. Clonez le dépôt :
   git clone <url_du_depot>
   cd nom_du_depot

2. Installez les dépendances Python :
  cd backend
  pip install -r requirements.txt

3. Installez les dépendances Node.js :
  cd frontend
  npm install

4. Effectuez les migrations de la base de données :
  cd backend
  python manage.py migrate

5. Démarrez le serveur de développement Django :
    python manage.py runserver

6. Démarrez le serveur de développement Vue.js :
  cd frontend
  npm run serve


