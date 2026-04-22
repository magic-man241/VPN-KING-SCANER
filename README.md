# 👑 VPN‑KING SCANER – BY MAGIC MAN

![Version](https://img.shields.io/badge/version-1.0-vert)
![Python](https://img.shields.io/badge/Python-3.6%2B-bleu)
![Licence](https://img.shields.io/badge/licence-Libre%20(Cr%C3%A9dit%20obligatoire)-jaune)
![Plateforme](https://img.shields.io/badge/Plateforme-Termux%20%7C%20Linux-cyan)

**Le moissonneur de sous-domaines ultime, conçu pour l'audit de sécurité et l'analyse de surface réseau.**

---

## 🇬🇦 À propos

**VPN‑KING** est un outil tout-en-un d'énumération de sous-domaines et d'analyse de hosts, spécialement optimisé pour **Termux** sur Android. Il permet de découvrir rapidement la surface d'exposition d'un domaine, de détecter les protections (Imperva, CDN), et d'analyser les services exposés.

Créé par **MAGIC‑MAN** (alias *Le Dieu du net*), cet outil se veut simple d'utilisation tout en offrant des fonctionnalités avancées.

---

## ✨ Fonctionnalités

- 🔍 **Scan de sous-domaines passif** : Utilise crt.sh, CertSpotter, HackerTarget et AlienVault (aucune requête directe vers la cible).
- 🛡️ **Détection Imperva / CDN** : Identifie les hôtes protégés par **Imperva (AS19551)** ou d'autres CDN (Cloudflare, Akamai, etc.).
- 🌐 **Reverse IP Lookup** : Trouve tous les domaines hébergés sur une même adresse IP.
- 🔎 **Analyse de surface** :
  - Test HTTP / HTTPS (code statut, titre, serveur)
  - Extraction des certificats SSL (émetteur, expiration)
  - Scan rapide des ports courants (80, 443, 21, 22, 3306, etc.)
- 📡 **Résolution DNS & Infos IP** : Conversion hôte ↔ IP, recherche ASN, plage CIDR, opérateur.
- 💾 **Sauvegarde des résultats** : Export en fichier texte avec choix du dossier (support de l'explorateur Android via `termux-api`).
- 🔐 **Protection par mot de passe** : Code par défaut `idiot` (modifiable).
- 🚀 **Auto‑installation** : Se configure automatiquement en tant que commande `vpnking` dans Termux.

---

## 📲 Installation sur Termux (Android)

### 📦 Méthode 1 : Téléchargement direct avec `curl` (recommandé)

```bash
# 1. Mise à jour de Termux et installation de Python
pkg update && pkg upgrade -y
pkg install python -y

# 2. Téléchargement du script
curl -L https://raw.githubusercontent.com/magic-man241/VPN-KING-SCANER/main/vpnking.py -o vpnking.py

# 3. Lancement du script (l'auto‑installation se déclenchera)
python vpnking.py
