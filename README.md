# Learn Vault With GitHub Actions

Simple API Python avec un endpoint type Hello World. L'image affichée peut être personalisée via la variable d'environnement `IMAGE_URL`.

## Forkez-moi ! Clonez-moi !

## Utilisation de Vault avec GitHub Actions

L'intégration de Vault avec GitHub est hyper facile car 100% managée (partenariat GitHub / Vault).

### STEP 01: Créer un compte Docker Hub

### STEP 02: Créer un private repository Docker

Pour héberger l'image de cette application (par défaut nommée `helloworld`).

### STEP 03: Créer un Access Token sur  Docker Hub

My Account > Security > New Access Token

Définir Access Permissions à « Read, Write » :
- Read pour pull l'image
- Write pour push l'image

On garde ça de côté.

### STEP 04: Créer un compte HashiCorp

### STEP 05: Créer une App sur Vault Secrets

L'appeler par exemple `docker`.

### STEP 06: Créer des secrets dans l'App Vault Secret

Les appeler par exemple `docker_hub_username` et `docker_hub_access_token`.

Y mettre les bonnes valeurs.

### STEP 07: Intégrer Vault Secret dans GitHub

Sélectionnez le bon dépôt.

Vérifier que le secret est correctement synced dans GitHub.

### STEP 08: Adapter le code de la CI/CD

Peut-être le nom de vos secrets et le nom de votre private repository.

Éventuellement, ne buildez que pour votre architecture afin d'accélérer l'exécution du pipeline (la step de build).

### STEP 9: Testez de modifier le code de l'API

Ça fonctionne ? Le pipeline est vert ? Votre image Docker est bien mise à jour ?

## Utilisation de Vault avec Kubernetes

Intégration moins facile car le cluster est self-hosted.



