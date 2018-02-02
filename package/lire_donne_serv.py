from package.gerer_fichier import *

def lire_message_server():
    dossier = "rep_serveur"
    liste = get_contenu_dossier(dossier,True)
    if len(liste):
        liste.reverse()
        for l in liste:
            with open(l,"r") as f:
                print(f.read())
            r = input(">>>>> lire un autre message o/n ")
            if r.lower()!="o":
                break
    else:
        print("-------- MSG: Aucune donnée disponible!!! -----------")
        print(liste)