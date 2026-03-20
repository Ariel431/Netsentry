# Netsentry

Outil de reconnaissance réseau en ligne de commande (CLI) développé en Python.

## 🚀 Fonctionnalités

- Scan IP ou nom de domaine avec détection :
  - des ports ouverts
  - du nom des services associés
- Recherche OSINT :
  - DNS
  - WHOIS
- Export des résultats en JSON via `json.dump()`

##  Prérequis

###  Linux (Fedora / Debian / Ubuntu)

```bash
sudo dnf install nmap   # Fedora
sudo apt install nmap   # Debian / Ubuntu
```
# Windows

- Installer nmap depuis : https://nmap.org/download.html

- Puis l’ajouter à la variable d’environnement PATH

# macOS
brew install nmap
## Installation
- git clone https://github.com/Ariel413/Netsentry.git
- cd Netsentry
- pip install -r requirements.txt
## Utilisation
```bash
# Scan + OSINT
python3 main.py --target domaine_ip --scan --osint

# OSINT uniquement
python3 main.py --target domaine_ip --osint

# Aide
python3 main.py Netsentry -h
```
⚠️ Attention !

Cet outil est à utiliser uniquement sur des systèmes dont vous avez l'autorisation explicite.