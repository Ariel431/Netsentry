import json
from datetime import datetime

def generate_report(data,target):
    #Ajout de la date actuelle dans data
    data["date"] = datetime.now().strftime("%d/%m/%Y à %Hh%M")
    #Nom du fichier
    file_name = f'rapport_{target}'
    # Ecriture dans le json
    with open (file_name,'w') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
        print(f'[+] Rapport sauvegardé : {file_name}')
    return file_name

