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
            ex = r["ssl_info"].get("expiration", "")
            print(couleur(f"   SSL   : émis par {em}, expire le {ex}", COULEURS.BLEU))
        cdn = r.get("cdn_info")
        if cdn:
            if cdn.get("is_imperva"):
                print(couleur(f"   🛡️ PROTÉGÉ PAR IMPERVA (IP: {cdn.get('ip')}, ASN: {cdn.get('asn')})", COULEURS.ROUGE + COULEURS.GRAS))
            elif cdn.get("is_cdn"):
                print(couleur(f"   🌍 Derrière un CDN ({cdn.get('asn_description')})", COULEURS.JAUNE))
        if r["ports_ouverts"]:
            print(couleur(f"   Ports ouverts : {', '.join(map(str, r['ports_ouverts']))}", COULEURS.ROUGE))

# ---------- RECHERCHE IP ----------
def rechercher_info_ip(adresse_ip):
    url = f"https://api.hackertarget.com/aslookup/?q={adresse_ip}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return {"erreur": f"Erreur HTTP {r.status_code}"}
        contenu = r.text.strip()
        if contenu.startswith("error") or "No records" in contenu:
            return {"erreur": "Aucune information trouvée."}
        p = contenu.split('","')
        if len(p) >= 4:
            return {"ip": adresse_ip, "asn": f"AS{p[1].replace('\"','')}", "cidr": p[2].replace('\"',''), "description": p[3].replace('\"','')}
    except Exception as e:
        return {"erreur": str(e)}
    return {"erreur": "Format inattendu"}

# ---------- RÉSOLUTION DNS ----------
def menu_resolution_dns():
    while True:
        print(couleur("\n🌐 RÉSOLUTION DNS & INFORMATIONS IP", COULEURS.BLEU + COULEURS.GRAS))
        print("  1. Convertir nom d'hôte → IP")
        print("  2. Convertir IP → nom d'hôte")
        print("  3. Infos détaillées sur une IP")
        print("  4. Retour")
        try:
            ch = input(couleur("👉 Choix (1/2/3/4) : ", COULEURS.JAUNE)).strip()
        except KeyboardInterrupt:
            break
        if ch == "1":
            h = input(couleur("Hôte : ", COULEURS.JAUNE)).strip()
            if h:
                try:
                    print(couleur(f"✅ {h} → {socket.gethostbyname(h)}", COULEURS.VERT))
                except:
                    print(couleur("❌ Échec", COULEURS.ROUGE))
            afficher_signature()
        elif ch == "2":
            ip = input(couleur("IP : ", COULEURS.JAUNE)).strip()
            if ip:
                try:
                    nom, _, _ = socket.gethostbyaddr(ip)
                    print(couleur(f"✅ {ip} → {nom}", COULEURS.VERT))
                except:
                    print(couleur("❌ Pas de PTR", COULEURS.ROUGE))
            afficher_signature()
        elif ch == "3":
            ip = input(couleur("IP : ", COULEURS.JAUNE)).strip()
            if ip:
                print(couleur("⏳ Recherche...", COULEURS.JAUNE))
                inf = rechercher_info_ip(ip)
                if "erreur" in inf:
                    print(couleur(f"❌ {inf['erreur']}", COULEURS.ROUGE))
                else:
                    print(couleur(f"\n📋 IP : {inf['ip']}", COULEURS.VERT))
                    print(couleur(f"   ASN : {inf['asn']}", COULEURS.VERT))
                    print(couleur(f"   CIDR : {inf['cidr']}", COULEURS.VERT))
                    print(couleur(f"   Description : {inf['description']}", COULEURS.VERT))
            afficher_signature()
        elif ch == "4":
            break

# ---------- SAUVEGARDE ----------
def sauvegarder_resultats(donnees, nom_base="resultats", suffixe=""):
    if not donnees:
        return
    try:
        ch = input(couleur(f"\n💾 Enregistrer{suffixe} ? (o/n) : ", COULEURS.JAUNE)).strip().lower()
    except:
        return
    if ch not in ('o','oui','y','yes'):
        return
    print(couleur("\n📂 Dossier :", COULEURS.BLEU))
    print("  1. Explorateur Android (termux-api)")
    print("  2. Chemin manuel")
    opt = input(couleur("👉 Choix : ", COULEURS.JAUNE)).strip()
    dossier = ""
    if opt == "1" and termux_api_disponible:
        try:
            res = subprocess.run(["termux-storage-get"], capture_output=True, text=True)
            dossier = res.stdout.strip()
        except:
            pass
    if not dossier:
        dossier = input(couleur("📁 Chemin complet : ", COULEURS.JAUNE)).strip()
    if not os.path.isdir(dossier):
        print(couleur("❌ Dossier invalide.", COULEURS.ROUGE))
        return
    nom_defaut = f"vpnking_{nom_base}{suffixe}.txt"
    nom = input(couleur(f"📄 Nom du fichier (défaut: {nom_defaut}) : ", COULEURS.JAUNE)).strip()
    if not nom:
        nom = nom_defaut
    if not nom.endswith(".txt"):
        nom += ".txt"
    chemin = os.path.join(dossier, nom)
    with open(chemin, "w") as f:
        if isinstance(donnees, list) and all(isinstance(x, str) for x in donnees):
            f.write("\n".join(donnees))
        else:
            for el in donnees:
                f.write(f"Hôte: {el['hote']}\n")
                if el.get("http"): f.write(f"  HTTP: {el['http']}\n")
                if el.get("https"): f.write(f"  HTTPS: {el['https']}\n")
                if el.get("ssl_info"): f.write(f"  SSL: {el['ssl_info']}\n")
                if el.get("cdn_info"): f.write(f"  CDN: {el['cdn_info']}\n")
                if el.get("ports_ouverts"): f.write(f"  Ports: {el['ports_ouverts']}\n")
                f.write("\n")
    print(couleur(f"💾 Sauvegardé dans : {chemin}", COULEURS.VERT))

# ---------- MENU PRINCIPAL ----------
def menu_principal():
    print("\n" + couleur("═"*40, COULEURS.JAUNE))
    print(couleur("     👑 VPN‑KING – MENU PRINCIPAL 👑", COULEURS.VERT + COULEURS.GRAS))
    print(couleur("═"*40, COULEURS.JAUNE))
    print("1. Scanner un domaine (+ reverse IP)")
    print("2. Analyser une liste de hosts")
    print("3. Résolution DNS & Infos IP")
    print("4. Changer le mot de passe")
    print("5. Quitter")
    try:
        return input(couleur("👉 Choix (1/2/3/4/5) : ", COULEURS.JAUNE)).strip()
    except KeyboardInterrupt:
        return "5"

# ---------- SCAN DOMAINE + REVERSE IP ----------
def scanner_domaine():
    try:
        domaine = input(couleur("\n🔍 Domaine (ex: airtel.ga) : ", COULEURS.JAUNE)).strip().lower()
    except:
        return
    if not domaine or "." not in domaine:
        print(couleur("❌ Domaine invalide.", COULEURS.ROUGE))
        afficher_signature()
        return
    if domaine.startswith("http"):
        domaine = urlparse(domaine).netloc

    sous_domaines = recolter_sous_domaines(domaine)
    print(couleur(f"\n🎯 {len(sous_domaines)} sous-domaines uniques", COULEURS.VERT))
    if not sous_domaines:
        print(couleur("😵 Aucun trouvé.", COULEURS.ROUGE))
        afficher_signature()
        return

    print(couleur("\n--- Liste ---", COULEURS.BLEU))
    for s in sous_domaines:
        print(s)

    print(couleur("\n🔄 Voulez-vous effectuer un reverse IP lookup sur les IP trouvées ?", COULEURS.BLEU))
    try:
        rev = input(couleur("   (o/n) : ", COULEURS.JAUNE)).strip().lower()
    except:
        rev = "n"
    if rev in ('o','oui','y','yes'):
        ips_vues = set()
        for s in sous_domaines:
            try:
                ip = socket.gethostbyname(s)
                ips_vues.add(ip)
            except:
                pass
        print(couleur(f"\n🌍 {len(ips_vues)} IP(s) uniques trouvées.", COULEURS.BLEU))
        for ip in sorted(ips_vues):
            print(couleur(f"   🔹 {ip}", COULEURS.JAUNE))
            domaines_ip = reverse_ip_lookup(ip)
            if domaines_ip:
                print(couleur(f"      → {len(domaines_ip)} domaine(s) hébergés :", COULEURS.VERT))
                for d in domaines_ip[:20]:
                    print(f"         {d}")
                if len(domaines_ip) > 20:
                    print(couleur(f"         ... et {len(domaines_ip)-20} autres", COULEURS.GRIS))
            else:
                print(couleur("      → Aucun domaine trouvé (ou API limitée)", COULEURS.GRIS))

    print(couleur("\n📌 Actions :", COULEURS.BLEU))
    print("  1. Sauvegarder liste brute")
    print("  2. Analyse de surface")
    print("  3. Les deux")
    print("  4. Passer")
    try:
        action = input(couleur("👉 Choix (1/2/3/4) : ", COULEURS.JAUNE)).strip()
    except:
        action = "4"
    if action == "1":
        sauvegarder_resultats(sous_domaines, domaine, "")
    elif action == "2":
        print(couleur("\n⚠️  Analyse réseau (consommation data).", COULEURS.JAUNE))
        try:
            if input(couleur("Continuer ? (o/n) : ", COULEURS.JAUNE)).strip().lower() in ('o','oui','y','yes'):
                res = lancer_verification_hotes(sous_domaines)
                afficher_resultats_verification(res)
                sauvegarder_resultats(res, domaine, "_verification")
        except KeyboardInterrupt:
            print(couleur("\nInterrompu.", COULEURS.JAUNE))
    elif action == "3":
        sauvegarder_resultats(sous_domaines, domaine, "")
        print(couleur("\n⚠️  Analyse réseau.", COULEURS.JAUNE))
        try:
            if input(couleur("Continuer ? (o/n) : ", COULEURS.JAUNE)).strip().lower() in ('o','oui','y','yes'):
                res = lancer_verification_hotes(sous_domaines)
                afficher_resultats_verification(res)
                sauvegarder_resultats(res, domaine, "_verification")
        except KeyboardInterrupt:
            print(couleur("\nInterrompu.", COULEURS.JAUNE))
    afficher_signature()

def analyser_liste_hosts():
    print(couleur("\n📋 Collez vos hosts (un par ligne, tapez FIN pour terminer) :", COULEURS.BLEU))
    lignes = []
    while True:
        try:
            l = input()
        except KeyboardInterrupt:
            break
        if l.strip().upper() == "FIN":
            break
        if l.strip():
            lignes.append(l.strip())
    if not lignes:
        print(couleur("❌ Aucun host.", COULEURS.ROUGE))
        afficher_signature()
        return
    hosts = []
    for h in lignes:
        if h.startswith("http://") or h.startswith("https://"):
            h = urlparse(h).netloc
        hosts.append(h)
    print(couleur(f"\n📊 {len(hosts)} hosts.", COULEURS.VERT))
    try:
        if input(couleur("Continuer ? (o/n) : ", COULEURS.JAUNE)).strip().lower() not in ('o','oui','y','yes'):
            afficher_signature()
            return
    except:
        return
    res = lancer_verification_hotes(hosts)
    afficher_resultats_verification(res)
    nom = input(couleur("\n💾 Nom du fichier (sans extension) : ", COULEURS.JAUNE)).strip()
    if not nom:
        nom = "analyse_hosts"
    sauvegarder_resultats(res, nom, "")
    afficher_signature()

# ---------- MAIN ----------
def main():
    if not est_installe():
        installer_script()

    afficher_logo()
    verifier_mdp()
    global termux_api_disponible
    termux_api_disponible = verifier_et_installer_dependances()
    while True:
        try:
            choix = menu_principal()
        except KeyboardInterrupt:
            choix = "5"
        if choix == "1":
            scanner_domaine()
        elif choix == "2":
            analyser_liste_hosts()
        elif choix == "3":
            menu_resolution_dns()
        elif choix == "4":
            changer_mdp()
        elif choix == "5":
            print(couleur("\n👋 VPN‑KING vous salue !", COULEURS.VERT))
            afficher_signature()
            sys.exit(0)
        else:
            print(couleur("❌ Choix invalide.", COULEURS.ROUGE))

if __name__ == "__main__":
    main()
