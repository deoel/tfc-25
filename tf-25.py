import sys
from package.completer_presence import *
from package.afficher import *
from package.lire_donne_serv import *

def aide():
    aid = """
    --init ou -i "fichier source étudiant" "fichier source cours" 
            : pour initialiser l'application en important les étudiants et les cours
    --presence ou -p acronyme date[dd-mm-aaaa] matricule présence[P|A] 
            : pour marquer la présence d'un étudiant
    -pa acronyme date[dd-mm-aaaa]  
            : pour marquer la présence des étudiant d'une manière aléatoire
    -ms 
            : pour lire les messages du serveur
    --import ou -ip acronyme date[dd-mm-aaaa] "fichier source" indice_mat indice_presence
            : pour importer les présences faites depuis un fichier excel.csv
    --list ou -l acronyme date[dd-mm-aaaa] [mats]
            : pour afficher les présences des étudiants dont le matricule est indiqué
    Avant toute chose, Initialiser tout d'abord l'application SVP!
    Tapez la commande  'chemin vers fichier source étudiant' 'chemin vers fichier source cours'
    """
    print(aid)

if __name__ == '__main__':
    arg = sys.argv
    # on vérifie si les fichier de base n'existent pas et on propose à l'utilisateur d'initialiser l'application
    if len(arg)>=2:
        cmd = arg[1]
        if cmd in ['--presence','-p'] and len(arg)>=6:  #le tableau arg doit avoir une taille minimale de 5 éléments pour faire une présence
            completer_presence(arg[2:])                 # EX:tf-25.py -p processing 12-10-2017 17KNP169 P
                
        elif cmd in ['--import','-ip'] and len(arg)>=7: #le tableau arg doit avoir une taille minimale de 6 éléments pour importer les présences
            importer_presence(arg[2:])                  # EX:tf-25.py -p processing 12-10-2017 fichier_source indice_mat indice_pres
        
        elif cmd in ['--list','-l'] and len(arg)>=3:
            afficher_presence(arg[2:])                  #je vérifie si l'utilisateur veut affichier la liste de présence

        elif cmd == '-pa' and len(arg)>=4:
            presence_aleatoire(arg[2:])                  #je vérifie si l'utilisateur veut affichier la liste de présence

        elif cmd == '-ms':
            lire_message_server()

        elif cmd in ['--init','-i'] and len(arg)>=4:
            csv_etudiant = arg[2]
            csv_cours = arg[3]
            reinitialiser_tout_le_system(csv_etudiant,csv_cours)
        else:
            aide()
    elif not fichier_existe(get_chemin_fichier_cours()) :
        aide()
    else:
        aide()
        print("Tapez une bonne commande svp!")

