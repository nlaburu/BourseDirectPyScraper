# BourseDirectPyScraper

Un petit script Python pour accéder au solde total de votre portefeuille sur le site [Bourse Direct](https://www.boursedirect.fr), inspiré du projet [BourDirConnect](https://github.com/wadael/BourDirConnect), mais réécrit entièrement en Python.

## ⚠️ Avertissement

> **Ce projet n'est pas affilié à Bourse Direct. Il est fourni *sans aucune garantie*. Utilisez-le *à vos risques et périls* 😄.**

- Une mauvaise utilisation de l'outil (comme un mauvais mot de passe ou passcode) **pourrait entraîner un blocage temporaire ou permanent de votre compte**.
- Pendant le développement, mes appels ont **tous abouti**, et **aucun blocage de compte n'a été observé**. Il est **possible** que Bourse Direct ne détecte pas (ou tolère) un certain seuil de connexions successives, mais **cela n'est en rien garanti**.
- Si le design du site change (notamment les `XPath`), **le scraper cessera de fonctionner**. Une mise à jour du code sera alors nécessaire.

---

## ✅ Fonctionnalités

- Authentification à votre compte Bourse Direct (via identifiant + passcode + 2FA)
- Récupération :
    - Solde total du portefeuille
---

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 💡 Remarques

- Ce script fonctionne uniquement sur la version **Web Desktop** de Bourse Direct.
- Le site n’offre **aucune API publique** : ce scraper utilise des requêtes HTTP simulant un navigateur.
---

## 🤝 Contributions

Les PR sont les bienvenues ! Merci de vérifier que votre code suit la logique existante et est bien documenté.

---