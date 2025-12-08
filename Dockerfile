# Utiliser une image Python slim (légère et sécurisée)
FROM python:3.11-slim

# Empêcher le buffering des logs Python pour les conteneurs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# ==============================================================================
# 1. PRÉPARATION DE L'ENVIRONNEMENT (Root)
# ==============================================================================

# Créer un utilisateur non-root 'app' pour l'exécution (BEST PRACTICE de sécurité)
RUN addgroup --gid 1000 app \
    && adduser --uid 1000 --ingroup app --shell /bin/sh --disabled-password --home /usr/src/app app

# Installer les dépendances système nécessaires
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    netcat-openbsd \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# ==============================================================================
# 2. INSTALLATION DES DÉPENDANCES PYTHON
# ==============================================================================

# Copier requirements.txt et l'installer
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ==============================================================================
# 3. COPIE DU CODE ET SÉCURITÉ
# ==============================================================================

# Copier le script d'entrée (entrypoint) et le rendre exécutable
COPY entrypoint.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh

# Copier le reste du code
COPY . .

# Créer les dossiers nécessaires
RUN mkdir -p /usr/src/app/staticfiles /usr/src/app/media

# Donner la propriété de tout le répertoire de travail à l'utilisateur 'app'
RUN chown -R app:app /usr/src/app

# Changer l'utilisateur pour l'exécution de l'application (DROP PRIVILEGES)
USER app

# ==============================================================================
# 4. EXÉCUTION
# ==============================================================================

# Exposer le port que l'application utilisera
EXPOSE 8000

# Définir le point d'entrée
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Commande par défaut (Gunicorn pour la production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "djoknone_portfolio.wsgi:application"]