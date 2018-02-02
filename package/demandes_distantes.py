
from package.config import *
from package.lire_donnees import *
def analyser_demande_distante(cmd_str):
    print(cmd_str)
    tab = (cmd_str.decode("utf-8")).split(" ")
    mats = []
    if len(tab)>=2:
        acro = tab[0]
        date = tab[1]
        if len(tab)>2:                              #on s'assure que le matricule est bien là avant de chercher
            if tab[2]!="":
                mats = tab[2].split(",")                #à le prendre
        
        cours = trouver_cours_si_acro_est(acro)     #on recherche le cours dans le fichier à partir de l'acronyme
        if not cours:
            return False                            #si le cours n'existe pas on retourne False

        dossier = get_chemin_dossier_presence() + acro
        if date!="":                                #on doit afficher la présence à une date donnée
            chemin = dossier +'/'+date+'.txt'       #on reconstruit le chemin vers le fichier de présence
        
            liste_p = generer_liste(chemin)         #ouverture du fichier de présence et génération de la liste assosciée
            chemin_etuds = get_chemin_fichier_etudiant()#on demande le chemin qui mène au fichier des étudiant
            liste_etuds = generer_liste(chemin_etuds)   #on génère la liste des étudiants en lisant le fichier
            
            return str_afficher_presence(date,cours[1],liste_p,mats,liste_etuds)
    else:
        return "Requête Mal conçue!"

def str_afficher_presence(date,nom_cours,liste_p,mats,liste_etuds):
    msg = ("======== Présence du "+date+"au cours de :"+nom_cours+"============\n")
    for p in liste_p:
        if (len(mats)!=0 and p[0] in mats) or len(mats)==0 :
            mat = p[0]
            etud = element_exist( liste_etuds,mat,0)  #on cherche dans la liste, l'étudiant dont le matricule est celui indiqué dans mat
            if etud!= False:
                text = (" ".join(etud))
                if p[1]=="P":
                    text = ">>>>>> "+text      #tous les étudiants présents seront précédés de '>>>>>>'          
                else:
                    text = "       "+text
                msg += (text+"\n")
            else:
                pass
    return msg
