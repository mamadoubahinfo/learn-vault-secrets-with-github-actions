# Learn Vault Secrets With GitHub Actions

Simple API Python avec un endpoint type Hello World.

- L'image affichée peut être personalisée via la variable d'environnement `IMAGE_URL`.  
- Un champ supplémentaire peut être affiché via la variable d'environnement `SECRET_VALUE` (la variable d'environnement sera affichée).

## Forkez-moi ! Clonez-moi !

## Utilisation de Vault Secrets avec GitHub Actions

L'intégration de Vault Secrets avec GitHub est hyper facile car 100% managée (partenariat GitHub / Vault).

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

Testez aussi en local.

```shell
docker run --rm -p 80:80 <image>
```

## Utilisation de Vault avec Kubernetes

Intégration moins facile car le cluster est self-hosted.

### STEP 01: Instalation du cluster

Avec l'outil de votre choix : Kind, Minikube, k3s, ...

### STEP 02: Installation de Vault Secrets CLI

En suivant la [documentation officielle](https://developer.hashicorp.com/hcp/tutorials/get-started-hcp-vault-secrets/hcp-vault-secrets-install-cli).

### STEP 03: Création d'un Service Principal

Au niveau de l'organisation. Avec le role viewer. L'appeler par exemple `k8s-vault-secret-operator`.

Générer une clé associée à ce Service Principal.

Noter le Client ID et le Client Secret.

bd4pi2PHCFIv2eGyq7lJAmtALp06KaRT
6W2_SoguIVjHLW21J6ZrsV4qaJ6lYN8cMscY4Pn-C7oODbWexZtJNapyESWfUai6

### STEP 04: Création d'un unique secret K8s

Parce qu'il en faut bien 1. Celui qui permettra à Vault de gérer tous les autres.

Adaptez les variables avec la valeur du Client ID et du Client Secret.

```shell
kubectl create secret generic vso-service-principal \
    --namespace vault-secrets-operator-system \
    --from-literal=clientID=$HCP_CLIENT_ID \
    --from-literal=clientSecret=$HCP_CLIENT_SECRET
```

### STEP 05: Installez l'opérateur Vault Secrets

```shell
helm repo add hashicorp https://helm.releases.hashicorp.com
helm upgrade --install vault-secrets-operator hashicorp/vault-secrets-operator \
     --namespace vault-secrets-operator-system \
     --create-namespace
```

### STEP 06: Adapter et déployez la configuration de l'opérateur

Adaptez le fichier de values du chart Helm : `manifests/vault-secret-operator-config/values.yaml`

```shell
helm upgrade --install vault-secret-operator-config manifests/vault-secret-operator-config \
     --namespace vault-secrets-operator-system \
     --create-namespace
```


