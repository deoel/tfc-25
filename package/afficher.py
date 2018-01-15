
from package.config import *
from package.lire_donnees import *
from package.autres  import *

def afficher_presence(cmd):
    acro = cmd[0]   #acronyme indiqué dans la commande
    date = ""
    if len(cmd)>1:
        date = cmd[1]
    mats = ""
    if len(cmd)>2 and cmd[2]!="":
        mats = (cmd[2]).split(',')


    chemin_cours = get_chemin_fichier_cours()   #on demande le chemin qui mène au fichier des cours
    liste_cours = generer_liste(chemin_cours)   #on génère la liste des cours en lisant le fichier
    cours = element_exist( liste_cours,acro,0)  #on cherche dans la liste, le cours dont l'acronyme est celui indiqué dans la commande
    
    if cours == False:                          #si on a False dans cours, c'est qu'aucun cours ne porte l'acronyme indiqué dans la commande
        print("Erreur: acronyme incorrect!")    #alos on affiche le message d'erreur 
        return False                            #et on qui la fonction

    dossier = get_chemin_dossier_presence() + acro
    if date!="":                                #on doit afficher la présence à une date donnée
        chemin = dossier +'/'+date+'.txt'       #on reconstruit le chemin vers le fichier de présence
    
        if not fichier_existe(chemin):          #existe-t-il vraiment un fichier au bout de ce chemin
            print("Aucune présence le",date,"en",cours[1])
            return False
        afficher_presence_date(chemin,date,cours,mats)#affiche la liste les présence du fichier chemin
    
    else:                                       #on doit afficher toutes les présence au cousr
        if not dossier_existe(dossier):
            print("Aucune présence au cours de: ",cours[1])
            return False
        afficher_presence_cours(dossier,cours,mats)#affiche la liste les présence du fichier chemin

def afficher_presence_date(chemin_pres,date,cours,mats):
    liste_p = generer_liste(chemin_pres)        #ouverture du fichier de présence et génération de la liste assosciée
    chemin_etuds = get_chemin_fichier_etudiant()#on demande le chemin qui mène au fichier des étudiant
    liste_etuds = generer_liste(chemin_etuds)   #on génère la liste des étudiants en lisant le fichier
    
    print("======== Présence du ",date,"au cours de :",cours[1],"============")
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
                print(text)
            else:
                pass
    

def afficher_presence_cours(dossier,cours,mats):
    fichiers_pres = get_contenu_dossier(dossier)#on récupère tous les fichiers de présence du dossier
    
    dico = {}
    for fichier in fichiers_pres:               #pour chaque fichier de présence
        liste_p = generer_liste(fichier)        #ouverture du fichier de présence et génération de la liste assosciée
        for p in liste_p:
            i = 0
            if p[1]=='P':
                i = 1
            if(dico.get(p[0],'0')=='0'):
                dico[p[0]] = i
            else :
                dico[p[0]] += i
    
    chemin_etuds = get_chemin_fichier_etudiant()#on demande le chemin qui mène au fichier des étudiant
    liste_etuds = generer_liste(chemin_etuds)   #on génère la liste des étudiants en lisant le fichier
    
    maxi = len(fichiers_pres)
    print("======== Taux de fréquentation au cours de :",cours[1],"============")
    for mat in dico:
        if (len(mats)!=0 and mat in mats) or len(mats)==0 :
            taux = dico[mat]
            etud = element_exist( liste_etuds,mat,0)  #on cherche dans la liste, l'étudiant dont le matricule est celui indiqué dans mat
            if etud!= False:
                text = (">>>>>> ",str(taux/maxi*100)+"%",(" ".join(etud)) )
                print(text)
            else:
                pass
    