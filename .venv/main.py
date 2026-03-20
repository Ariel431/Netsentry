import argparse
from modules.scanner import scan_target
from modules.osint import osint_target
from modules.report import generate_report

parser = argparse.ArgumentParser(
                    prog='Netsentry',
                    description='Outil de scan réseau et OSINT ',
                                                         )

parser.add_argument("--target",required=True,help="IP ou nom de domaine de la cible")
parser.add_argument("--scan",action="store_true",help="Scanner les ports")
parser.add_argument("--osint",action="store_true",help="Recherche OSINT")

args = parser.parse_args()

rapport = {"target" : args.target}

if args.scan:
    #Appelle de ma fonction depuis scanner.py
    print(f"[+]Scan activer sur la cible {args.target} ")
    rapport['scan'] = scan_target(args.target)
if args.osint:
    print(f"[+]OSINT activé sur la cible {args.target}")
    rapport['osint'] = osint_target(args.target)

if not args.scan and not args.osint:
    print("[!]Aucune action choisie. Utilise --scan ou --osint")
else:
    generate_report(rapport,args.target)

'''
    Les adresses IP locales (ou privées), comme celles des plages 192.168.x.x,
      10.x.x.x et 172.16.x.x, ne peuvent pas faire l'objet d'une recherche WHOIS publique. 
    Ces adresses sont réservées à un usage privé selon la norme RFC 1918 et ne sont pas 
    routables sur Internet. 
    Elles ne sont pas attribuées par les registres Internet régionaux (RIR) comme ARIN ou 
    RIPE NCC, donc aucune information WHOIS n'est disponible. 
    Une requête WHOIS sur une IP privée ne retournera aucun résultat utile, car ces adresses
      ne sont pas uniques à l'échelle mondiale. 
    Pour identifier un appareil sur un réseau local, utilisez :

    La table ARP de votre routeur (arp -a)
    Ainsi en voulant utiliser --osint assurez vous que l'ip est routable sur internet. 
    
    '''


