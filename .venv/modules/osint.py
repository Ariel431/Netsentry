import dns.resolver
import whois


def osint_target(target):
    data ={}
    #DNS
    print(f"[+] DNS pour {target}")
    try:
        result = dns.resolver.resolve(target,"A")#A pour resolution IPV4
        for ip in result:
            data['ipv4'] = ip.address
            print(f"Nom de domaine de {target} : {ip.address}")
    except ( dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        print("Pas d'enregistrement A")
        data['ipv4'] =  None
            
        
    try:
        mx_result = dns.resolver.resolve(target,"MX")#A pour resolution IPV4
        data['mx'] = []
        for mx in mx_result:
             data["mx"].append(str(mx.exchange))
             print(f"Serveur MX : {mx.exchange}")
    except ( dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        print("Pas d'enregistrement MX")
        data['mx'] = None
    #WHOIS
    
    try:   
        info = whois.whois(target)
        #Proprietaire
        data['proprietaire'] = info.org
        print(f" Propriétaire : {info.org}")
                # Creation
        creation = info.creation_date
        if isinstance(creation, list):
            creation = creation[0]

        if creation:
            data['creation'] = creation.isoformat()
        else:
            data['creation'] = None

        print(f" Creer le : {creation}")

        # Expiration
        expiration = info.expiration_date
        if isinstance(expiration, list):
            expiration = expiration[0]

        if expiration:
            data['expiration'] = expiration.isoformat()
        else:
            data['expiration'] = None

        print(f" Expire le : {expiration}")
        
    except whois.exceptions.WhoisCommandFailedError:
                print("Erreur")

    return data



