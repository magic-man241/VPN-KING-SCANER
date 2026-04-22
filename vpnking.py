#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ██╗   ██╗██████╗ ███╗   ██╗      ██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║   ██║██╔══██╗████╗  ██║      ██║ ██╔╝██║████╗  ██║██╔════╝
 ██║   ██║██████╔╝██╔██╗ ██║█████╗█████╔╝ ██║██╔██╗ ██║██║  ███╗
 ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║╚════╝██╔═██╗ ██║██║╚██╗██║██║   ██║
  ╚████╔╝ ██║     ██║ ╚████║      ██║  ██╗██║██║ ╚████║╚██████╔╝
   ╚═══╝  ╚═╝     ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

           👑 VPN‑KING – BY MAGIC MAN 👑
        Le moissonneur de sous-domaines ultime
"""

import sys
import subprocess
import os
import hashlib
import getpass
import signal
import shutil
import stat

# ---------- GESTION CTRL+C ----------
def signal_handler(sig, frame):
    print(couleur("\n\n⚠️  Interruption détectée. Retour au menu...", COULEURS["JAUNE"]))
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, signal_handler)

# ---------- COULEURS GABON ----------
class COULEURS:
    VERT = "\033[92m"
    JAUNE = "\033[93m"
    BLEU = "\033[94m"
    ROUGE = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GRIS = "\033[90m"
    BLANC = "\033[97m"
    GRAS = "\033[1m"
    SOULIGNE = "\033[4m"
    RESET = "\033[0m"

def couleur(texte, code):
    return f"{code}{texte}{COULEURS.RESET}"

# ---------- AUTO‑INSTALLATION ----------
def est_installe():
    return shutil.which("vpnking") is not None

def installer_script():
    print(couleur("\n🔧 PREMIÈRE UTILISATION – INSTALLATION AUTOMATIQUE", COULEURS.VERT + COULEURS.GRAS))
    print(couleur("Le script va se configurer pour être lancé avec la commande 'vpnking'.", COULEURS.BLEU))
    try:
        reponse = input(couleur("👉 Continuer ? (o/n) : ", COULEURS.JAUNE)).strip().lower()
    except KeyboardInterrupt:
        print(couleur("\nInstallation annulée. Vous pouvez relancer le script manuellement.", COULEURS.JAUNE))
        sys.exit(0)
    if reponse not in ('o', 'oui', 'y', 'yes'):
        print(couleur("Installation annulée. Le script fonctionnera uniquement en mode manuel.", COULEURS.JAUNE))
        return

    dossier_bin = os.path.expanduser("~/bin")
    if not os.path.exists(dossier_bin):
        os.makedirs(dossier_bin, exist_ok=True)

    script_source = os.path.abspath(__file__)
    script_dest = os.path.join(dossier_bin, "vpnking")

    try:
        shutil.copy2(script_source, script_dest)
        os.chmod(script_dest, os.stat(script_dest).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print(couleur(f"✅ Script copié dans {script_dest}", COULEURS.VERT))
    except Exception as e:
        print(couleur(f"❌ Erreur lors de la copie : {e}", COULEURS.ROUGE))
        return

    chemin_bashrc = os.path.expanduser("~/.bashrc")
    ligne_path = 'export PATH="$HOME/bin:$PATH"'
    try:
        with open(chemin_bashrc, "r") as f:
            contenu = f.read()
        if ligne_path not in contenu:
            with open(chemin_bashrc, "a") as f:
                f.write(f"\n# Ajouté par VPN‑KING\n{ligne_path}\n")
            print(couleur("✅ PATH mis à jour dans .bashrc", COULEURS.VERT))
        else:
            print(couleur("ℹ️  Le PATH est déjà configuré.", COULEURS.BLEU))
    except Exception as e:
        print(couleur(f"⚠️  Impossible de modifier .bashrc : {e}", COULEURS.JAUNE))

    alias_line = "alias vpnking='python ~/bin/vpnking'"
    try:
        with open(chemin_bashrc, "r") as f:
            contenu = f.read()
        if alias_line not in contenu:
            with open(chemin_bashrc, "a") as f:
                f.write(f"{alias_line}\n")
            print(couleur("✅ Alias ajouté dans .bashrc", COULEURS.VERT))
    except:
        pass

    print(couleur("\n🎉 INSTALLATION TERMINÉE !", COULEURS.VERT + COULEURS.GRAS))
    print(couleur("Pour utiliser VPN‑KING, fermez et rouvrez Termux, ou tapez :", COULEURS.BLEU))
    print(couleur("   source ~/.bashrc", COULEURS.JAUNE))
    print(couleur("Ensuite, lancez simplement : vpnking", COULEURS.VERT))
    input(couleur("\nAppuyez sur Entrée pour continuer avec cette session...", COULEURS.GRIS))

# ---------- LOGO COMPACT ----------
def afficher_logo():
    logo = f"""
{couleur("╔══════════════════════════════════╗", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("█╗   █╗██████╗ ███╗  ██╗      ██╗  ██╗██╗███╗  ██╗ ██████╗", COULEURS.VERT)} {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("██╗  █║██╔══██╗████╗ ██║      ██║ ██╔╝██║████╗ ██║██╔════╝", COULEURS.VERT)} {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("█╔█╗ █║██████╔╝██╔██╗██║█████╗█████╔╝ ██║██╔██╗██║██║  ███╗", COULEURS.JAUNE)} {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("█║╚██╔╝██╔═══╝ ██║╚████║╚════╝██╔═██╗ ██║██║╚████║██║   ██║", COULEURS.BLEU)} {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("█║ ╚█╔╝ ██║     ██║ ╚███║      ██║  ██╗██║██║ ╚███║╚██████╔╝", COULEURS.BLEU)} {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}  {couleur("╚═╝  ╚═╝ ╚═╝     ╚═╝  ╚══╝      ╚═╝  ╚═╝╚═╝╚═╝  ╚══╝ ╚═════╝", COULEURS.BLEU)} {couleur("║", COULEURS.JAUNE)}
{couleur("╠══════════════════════════════════╣", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}     {couleur("👑 VPN‑KING – BY MAGIC MAN 👑", COULEURS.VERT + COULEURS.GRAS)}     {couleur("║", COULEURS.JAUNE)}
{couleur("║", COULEURS.JAUNE)}        {couleur("Le moissonneur de sous-domaines", COULEURS.BLEU)}          {couleur("║", COULEURS.JAUNE)}
{couleur("╚══════════════════════════════════╝", COULEURS.JAUNE)}
"""
    print(logo)

# ---------- GESTION MOT DE PASSE ----------
FICHIER_MDP = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".vpnking_pass")

def hash_mdp(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()

def definir_mdp_initial():
    with open(FICHIER_MDP, "w") as f:
        f.write(hash_mdp("idiot"))

def verifier_mdp():
    if not os.path.exists(FICHIER_MDP):
        definir_mdp_initial()
    with open(FICHIER_MDP, "r") as f:
        hash_stocke = f.read().strip()
    tentatives = 3
    while tentatives > 0:
        try:
            mdp_saisi = getpass.getpass(couleur("🔑 Mot de passe : ", COULEURS.JAUNE))
        except KeyboardInterrupt:
            print(couleur("\n👋 Au revoir !", COULEURS.VERT))
            sys.exit(0)
        if hash_mdp(mdp_saisi) == hash_stocke:
            print(couleur("✅ Accès autorisé.", COULEURS.VERT))
            return True
        else:
            tentatives -= 1
            print(couleur(f"❌ Mot de passe incorrect. {tentatives} tentative(s) restante(s).", COULEURS.ROUGE))
    print(couleur("🚫 Accès refusé.", COULEURS.ROUGE))
    sys.exit(1)

def changer_mdp():
    print(couleur("\n🔐 Changement du mot de passe", COULEURS.BLEU))
    try:
        ancien = getpass.getpass(couleur("Ancien mot de passe : ", COULEURS.JAUNE))
    except KeyboardInterrupt:
        print(couleur("\nAnnulé.", COULEURS.JAUNE))
        return
    with open(FICHIER_MDP, "r") as f:
        if hash_mdp(ancien) != f.read().strip():
            print(couleur("❌ Ancien mot de passe incorrect.", COULEURS.ROUGE))
            return
    try:
        nouveau = getpass.getpass(couleur("Nouveau mot de passe : ", COULEURS.JAUNE))
        confirmation = getpass.getpass(couleur("Confirmez le nouveau mot de passe : ", COULEURS.JAUNE))
    except KeyboardInterrupt:
        print(couleur("\nAnnulé.", COULEURS.JAUNE))
        return
    if nouveau != confirmation:
        print(couleur("❌ Les mots de passe ne correspondent pas.", COULEURS.ROUGE))
        return
    with open(FICHIER_MDP, "w") as f:
        f.write(hash_mdp(nouveau))
    print(couleur("✅ Mot de passe changé avec succès.", COULEURS.VERT))

# ---------- VÉRIFICATION DÉPENDANCES ----------
def verifier_et_installer_dependances():
    manquants = []
    try:
        import requests
    except ImportError:
        manquants.append("requests")

    if manquants:
        print(couleur("❌ Modules Python manquants : " + ", ".join(manquants), COULEURS.ROUGE))
        print(couleur("Pour les installer automatiquement, exécutez :", COULEURS.JAUNE))
        print(f"   pip install {' '.join(manquants)}")
        reponse = input(couleur("👉 Voulez-vous que le script tente l'installation maintenant ? (o/n) : ", COULEURS.JAUNE)).strip().lower()
        if reponse in ('o', 'oui', 'y', 'yes'):
            for module in manquants:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(couleur("✅ Modules installés. Redémarrez le script.", COULEURS.VERT))
            sys.exit(0)
        else:
            print(couleur("❌ Veuillez installer les dépendances manuellement puis relancer le script.", COULEURS.ROUGE))
            sys.exit(1)

    termux_api_ok = False
    try:
        subprocess.run(["termux-storage-get"], capture_output=True, check=False)
        termux_api_ok = True
    except FileNotFoundError:
        pass

    if not termux_api_ok:
        print(couleur("⚠️  termux-api n'est pas installé. La sélection de dossier via l'explorateur Android ne fonctionnera pas.", COULEURS.JAUNE))
        print(couleur("   Pour l'installer : pkg install termux-api", COULEURS.JAUNE))
        print(couleur("   Vous pourrez toujours entrer le chemin manuellement.\n", COULEURS.JAUNE))
    return termux_api_ok

# ---------- SIGNATURE ----------
AUTEUR = "MAGIC-MAN"
SLOGAN = "Le Dieu du net"
WHATSAPP = "+241 60 14 16 33"

def afficher_signature():
    print("\n" + couleur("═"*40, COULEURS.JAUNE))
    print(couleur(f"   👑 {AUTEUR} – {SLOGAN} 👑", COULEURS.VERT + COULEURS.GRAS))
    print(couleur(f"   WhatsApp : {WHATSAPP}", COULEURS.BLEU))
    print(couleur("   Partage libre – Crédit obligatoire", COULEURS.GRIS))
    print(couleur("═"*40, COULEURS.JAUNE))

# ---------- CONFIGURATION ----------
AGENTS_UTILISATEUR = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36",
]

DELAI_TIMEOUT = 10
TENTATIVES = 2
NOMBRE_THREADS = 10

SOURCES = {
    "crt.sh": "https://crt.sh/?q=%25.{domain}&exclude=expired&deduplicate=Y&output=json",
    "certspotter": "https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names",
    "hackertarget": "https://api.hackertarget.com/hostsearch/?q={domain}",
    "alienvault": "https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns",
}

PORTS_A_SCANNER = [80, 443, 8080, 8443, 21, 22, 25, 3306, 3389]

# ---------- IMPORTS ----------
import requests
import time
import random
import socket
import ssl
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

termux_api_disponible = False

# ---------- FONCTIONS UTILITAIRES ----------
def agent_aleatoire():
    return random.choice(AGENTS_UTILISATEUR)

def telecharger_url(url, en_tetes=None, tentatives=TENTATIVES):
    for tentative in range(tentatives):
        try:
            h = {"User-Agent": agent_aleatoire()}
            if en_tetes:
                h.update(en_tetes)
            reponse = requests.get(url, headers=h, timeout=DELAI_TIMEOUT)
            if reponse.status_code == 200:
                return reponse
            else:
                time.sleep(2 ** tentative)
        except Exception:
            time.sleep(2 ** tentative)
    return None

# ---------- DÉTECTION CDN / IMPERVA ----------
def detecter_cdn_imperva(hote):
    resultat = {"ip": None, "asn": None, "asn_description": None, "is_imperva": False, "is_cdn": False}
    try:
        ip = socket.gethostbyname(hote)
        resultat["ip"] = ip
    except:
        return resultat

    try:
        url = f"https://api.hackertarget.com/aslookup/?q={ip}"
        reponse = requests.get(url, timeout=5)
        if reponse.status_code == 200:
            contenu = reponse.text.strip()
            if not contenu.startswith("error") and "No records" not in contenu:
                parties = contenu.split('","')
                if len(parties) >= 4:
                    asn = parties[1].replace('"', '')
                    desc = parties[3].replace('"', '')
                    resultat["asn"] = f"AS{asn}"
                    resultat["asn_description"] = desc
                    if asn == "19551":
                        resultat["is_imperva"] = True
                        resultat["is_cdn"] = True
                    cdn_asns = ["13335", "20940", "16509", "16625", "54113", "14618"]
                    if asn in cdn_asns:
                        resultat["is_cdn"] = True
    except:
        pass
    return resultat

# ---------- EXTRACTEURS SOUS‑DOMAINES ----------
def extraire_crtsh(domaine, callback):
    url = SOURCES["crt.sh"].format(domain=domaine)
    reponse = telecharger_url(url)
    if not reponse: return
    try:
        for entree in reponse.json():
            for nom in entree.get("name_value", "").split("\n"):
                nom = nom.strip().lower()
                if nom and nom.endswith(domaine) and "*" not in nom:
                    callback(nom)
    except: pass

def extraire_certspotter(domaine, callback):
    url = SOURCES["certspotter"].format(domain=domaine)
    reponse = telecharger_url(url)
    if not reponse: return
    try:
        for cert in reponse.json():
            for dns in cert.get("dns_names", []):
                dns = dns.strip().lower()
                if dns.endswith(domaine) and "*" not in dns:
                    callback(dns)
    except: pass

def extraire_hackertarget(domaine, callback):
    url = SOURCES["hackertarget"].format(domain=domaine)
    reponse = telecharger_url(url)
    if not reponse: return
    for ligne in reponse.text.splitlines():
        if "," in ligne:
            sous = ligne.split(",")[0].strip().lower()
            if sous.endswith(domaine):
                callback(sous)

def extraire_alienvault(domaine, callback):
    url = SOURCES["alienvault"].format(domain=domaine)
    reponse = telecharger_url(url, en_tetes={"X-OTX-API-KEY": ""})
    if not reponse: return
    try:
        for entree in reponse.json().get("passive_dns", []):
            nom = entree.get("hostname", "").strip().lower()
            if nom.endswith(domaine):
                callback(nom)
    except: pass

def recolter_sous_domaines(domaine):
    print(couleur(f"\n👑 VPN‑KING scanne : {domaine}", COULEURS.VERT + COULEURS.GRAS))
    tous = set()
    verrou = threading.Lock()
    def cb(sous):
        with verrou:
            if sous not in tous:
                tous.add(sous)
                print(couleur(f"  ➕ {sous}", COULEURS.VERT))
    taches = [extraire_crtsh, extraire_certspotter, extraire_hackertarget, extraire_alienvault]
    with ThreadPoolExecutor(max_workers=NOMBRE_THREADS) as ex:
        futures = [ex.submit(f, domaine, cb) for f in taches]
        for _ in as_completed(futures): pass
    return sorted(tous)

# ---------- REVERSE IP LOOKUP ----------
def reverse_ip_lookup(ip):
    if not ip:
        return []
    url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
    try:
        reponse = requests.get(url, timeout=15)
        if reponse.status_code == 200:
            lignes = reponse.text.strip().splitlines()
            return [l.strip().lower() for l in lignes if l.strip() and not l.startswith("#")]
    except:
        pass
    return []

# ---------- ANALYSE DE HOSTS ----------
def verifier_hote(sous_domaine):
    res = {"hote": sous_domaine, "http": None, "https": None, "ssl_info": None, "ports_ouverts": [], "cdn_info": None}
    res["cdn_info"] = detecter_cdn_imperva(sous_domaine)
    try:
        r = requests.get(f"http://{sous_domaine}", timeout=5, allow_redirects=True)
        res["http"] = {"statut": r.status_code, "titre": extraire_titre(r.text) if r.text else "", "serveur": r.headers.get("Server", "Inconnu")}
    except: res["http"] = {"erreur": "timeout/refusé"}
    try:
        r = requests.get(f"https://{sous_domaine}", timeout=5, allow_redirects=True)
        res["https"] = {"statut": r.status_code, "titre": extraire_titre(r.text) if r.text else "", "serveur": r.headers.get("Server", "Inconnu")}
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=sous_domaine) as s:
                s.settimeout(5)
                s.connect((sous_domaine, 443))
                cert = s.getpeercert()
                res["ssl_info"] = {
                    "emetteur": dict(x[0] for x in cert.get("issuer", [])),
                    "expiration": cert.get("notAfter"),
                    "sujet": dict(x[0] for x in cert.get("subject", []))
                }
        except: res["ssl_info"] = {"erreur": "certificat non récupérable"}
    except: res["https"] = {"erreur": "timeout/refusé"}
    for port in PORTS_A_SCANNER:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        if sock.connect_ex((sous_domaine, port)) == 0:
            res["ports_ouverts"].append(port)
        sock.close()
    return res

def extraire_titre(html):
    import re
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    return m.group(1).strip() if m else ""

def lancer_verification_hotes(liste_hotes, afficher_progression=True):
    if afficher_progression:
        print(couleur("\n🔎 ANALYSE DE SURFACE", COULEURS.BLEU + COULEURS.GRAS))
        print(couleur("   (HTTP/HTTPS, SSL, ports, détection Imperva)", COULEURS.JAUNE))
    resultats = []
    verrou = threading.Lock()
    fait = 0
    total = len(liste_hotes)
    def verifier_et_stocker(hote):
        nonlocal fait
        r = verifier_hote(hote)
        with verrou:
            resultats.append(r)
            fait += 1
            if afficher_progression:
                etat = "🌐"
                if r["https"] and "statut" in r["https"]:
                    etat = f"✅ HTTPS {r['https']['statut']}"
                elif r["http"] and "statut" in r["http"]:
                    etat = f"⚠️  HTTP {r['http']['statut']}"
                else:
                    etat = "❌ Aucune réponse"
                cdn = r.get("cdn_info", {})
                if cdn and cdn.get("is_imperva"):
                    etat += couleur(" 🛡️IMPERVA", COULEURS.ROUGE + COULEURS.GRAS)
                elif cdn and cdn.get("is_cdn"):
                    etat += couleur(" 🌍CDN", COULEURS.JAUNE)
                ports = f" (ports: {','.join(map(str, r['ports_ouverts']))})" if r["ports_ouverts"] else ""
                print(f"[{fait}/{total}] {hote} → {etat}{ports}")
    with ThreadPoolExecutor(max_workers=NOMBRE_THREADS) as ex:
        futures = [ex.submit(verifier_et_stocker, h) for h in liste_hotes]
        for _ in as_completed(futures): pass
    return resultats

def afficher_resultats_verification(resultats):
    print("\n" + couleur("═"*50, COULEURS.JAUNE))
    print(couleur("📊 RAPPORT D'ANALYSE", COULEURS.VERT + COULEURS.GRAS))
    print(couleur("═"*50, COULEURS.JAUNE))
    for r in resultats:
        print(couleur(f"\n🔹 {r['hote']}", COULEURS.BLEU))
        if r["http"] and "statut" in r["http"]:
            print(couleur(f"   HTTP  : {r['http']['statut']} - {r['http'].get('titre','')[:50]}", COULEURS.JAUNE))
        if r["https"] and "statut" in r["https"]:
            print(couleur(f"   HTTPS : {r['https']['statut']} - {r['https'].get('titre','')[:50]}", COULEURS.VERT))
        if r["ssl_info"] and "emetteur" in r["ssl_info"]:
            em = r["ssl_info"]["emetteur"].get("organizationName", "Inconnu")
            ex = r["ssl_info"].get(
