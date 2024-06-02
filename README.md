# Learn Vault With GitHub Actions

Simple API Python avec un endpoint type Hello World. L'image affichée peut être personalisée via la variable d'environnement `IMAGE_URL`.

## STEP 00: Forkez-moi ! Clonez-moi !

## STEP 01: Créer un compte Docker Hub

## STEP 02: Créer un private repository Docker

Pour héberger l'image de cette application (par défaut nommée `helloworld`).

## STEP 03: Créer un Access Token sur  Docker Hub

My Account > Security > New Access Token

Définir Access Permissions à « Read, Write » :
- Read pour pull l'image
- Write pour push l'image

## STEP 04: Construire le fichier de configuration de Docker

```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "username": "<docker_hub_username>",
            "password": "<docker_hub_access_token"
      }
    }
}
```

On garde ça de côté.

## STEP 05: Créer un compte HashiCorp

## STEP 06: Créer une App sur Vault Secrets

L'appeler par exemple `docker`.

## STEP 07: Créer un secret dans l'App Vault Secret

L'appeler par exemple `docker_config`.

Sa valeur est celle du JSON précédemment construit (pas besoin des espaces / retours à la ligne => c'est du JSON).
*
## STEP 08: Intégrer Vault Secret dans GitHub

Sélectionnez le bon dépôt.

Vérifier que le secret est correctement synced dans GitHub.

## STEP 09: Adapter le code de la CI/CD

Votre username Docker Hub.

Peut-être le nom de votre secret et le nom de votre private repository.

Éventuellement, ne buildez que pour votre architecture afin d'accélérer l'exécution du pipeline (la step de build).

## STEP 10: Testez de modifier le code de l'API

Ça fonctionne ? Le pipeline est vert ? Votre image Docker est bien mise à jour ?

