# Utiliser une image Python slim (légère et sécurisée)
FROM python:3.11-slim

# Empêcher le buffering des logs Python
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Installer les dépendances système nécessaires pour PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port
EXPOSE 8000

# Commande par défaut pour démarrer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]