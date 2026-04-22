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
```

📦 Méthode 2 : Cloner le dépôt avec git

```bash
# 1. Installer git si ce n'est pas déjà fait
pkg install git -y

# 2. Cloner le dépôt
git clone https://github.com/magic-man241/VPN-KING-SCANER.git

# 3. Se déplacer dans le dossier et lancer
cd VPN-KING-SCANER
python vpnking.py
```

---

🚀 Auto‑installation (premier lancement)

Lors du premier lancement, le script vous proposera de s'installer définitivement en tant que commande vpnking.
Acceptez (tapez o), puis :

· Redémarrez Termux (fermez et rouvrez l'application)
    OU
· Tapez source ~/.bashrc

Ensuite, vous pourrez lancer l'outil depuis n'importe quel dossier avec :

```bash
vpnking
```

🔑 Mot de passe par défaut : idiot (modifiable via l'option 4 du menu).

---

🖥️ Utilisation

Une fois lancé, choisissez parmi les options du menu principal :

```
1. Scanner un domaine (+ reverse IP)
2. Analyser une liste de hosts
3. Résolution DNS & Infos IP
4. Changer le mot de passe
5. Quitter
```

Exemple de scan complet

```
🔍 Domaine (ex: airtel.ga) : airtel.ga

👑 VPN‑KING scanne : airtel.ga
  ➕ www.airtel.ga
  ➕ mail.airtel.ga
  ➕ cloud.airtel.ga
  ...

🎯 42 sous-domaines uniques

🔄 Voulez-vous effectuer un reverse IP lookup ? (o/n) : o

🌍 5 IP(s) uniques trouvées.
   🔹 45.60.78.92
      → 12 domaine(s) hébergés :
         airtel.ga
         www.airtel.ga
         ...
```

---

📊 Exemple de rapport d'analyse

```
══════════════════════════════════════════════════
📊 RAPPORT D'ANALYSE
══════════════════════════════════════════════════

🔹 airtel.ga
   HTTPS : 200 - Airtel Gabon
   SSL   : émis par DigiCert Inc, expire le 2025-12-01
   🛡️ PROTÉGÉ PAR IMPERVA (IP: 45.60.78.92, ASN: AS19551)
   Ports ouverts : 80, 443

🔹 cloud-monitor.airtel.ga
   HTTP  : 200 - Dashboard
   HTTPS : 200 - Dashboard
   SSL   : émis par Let's Encrypt, expire le 2025-10-15
   Ports ouverts : 22, 80, 443, 3306
```

---

⚙️ Dépendances

· Python 3.6+
· Module Python requests (installé automatiquement si manquant)
· Optionnel : termux-api pour le sélecteur de dossier Android
  ```bash
  pkg install termux-api -y
  ```

---

👑 Auteur

MAGIC‑MAN – Le Dieu du net
📞 WhatsApp : +241 60 14 16 33

---

📄 Licence

Ce projet est libre de partage à condition de créditer l'auteur (MAGIC‑MAN).
Toute modification ou redistribution doit mentionner le créateur original.

---

⚠️ Avertissement

Cet outil est destiné à des fins éducatives et d'audit de sécurité autorisé.
L'utilisateur est seul responsable de l'usage qu'il en fait.
Respectez les lois en vigueur dans votre pays.

**MAGIC‑MAN** – *Le Dieu du net* 🇬🇦
