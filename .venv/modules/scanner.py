import nmap

def scan_target(target):
    data = {}
    #Initialisation du scanner:
    nm = nmap.PortScanner()
    # Debut scan
    nm.scan(hosts=target,ports="20-100",arguments="-sV")
        

    for target in nm.all_hosts():
        if nm[target].state() == "down":
            print(f"{target} is : {nm[target].state()}")
        else:
            print(f"{target} is : {nm[target].state()}")

        for proto in nm[target].all_protocols():
            print("Protocol :" , proto)
            data[proto] = {}
            
            ports = nm[target][proto].keys()#Dictionnaire sur le protocole dont les clés sont les ports
            for port in ports:
                print(f"Port {port} :  {nm[target][proto][port]['state']}  \nservice : {nm[target][proto][port]['name']} \nproduit:{nm[target][proto][port]['product']}")
                data[proto][port] = {

                    'state': nm[target][proto][port]['state'],
                    'service': nm[target][proto][port]['name'],
                    'produit': nm[target][proto][port]['product']
                                                                    }
                
        return data        
                         


    
