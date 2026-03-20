# Netsentry
Outil de reconnaissance réseau en ligne de commande (CLI) développé en python.

## Fonctionnalités

-    Scan ip ou nom de domaine avec detection des ports ouverts et le nom des services associés
-    Recherche OSINT (DNS, WHOIS)
-    Export des résultats en JSON via JSON.dump()

## Installation

- git clone https://github.com/Ariel413/Netsentry.git 
- cd Netsentry 
- pip install -r requirements.txt (Pour satisfaire les dépendances du projet)

## Utilisation

- python3 main.py --target domaine_ip --scan --osint 
- python3 main.py --target domaine_ip --osint 
- python3 main.py --target domaine_ip --scan --osint
- python3 main.py Netsentry --help pour plus de précisions.

## Attention !

Cet outil est à utiliser uniquement sur des systèmes dont vous avez l'autorisation explicite .