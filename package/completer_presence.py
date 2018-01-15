
from package.config import *
from package.lire_donnees import *
from package.autres  import *

def completer_presence(cmd):
    acro = cmd[0]   #acronyme indiqué dans la commande
    date = cmd[1]
    mats = cmd[2]
    pres = cmd[3].upper()
    if len(cmd)>4:
        adress_machine = cmd[4]
        rediriger_cmd(adress_machine,cmd[0:-1])
        return True

    chemin_cours = get_chemin_fichier_cours()   #on demande le chemin qui mène au fichier des cours
    liste_cours = generer_liste(chemin_cours)   #on génère la liste des cours en lisant le fichier
    cours = element_exist( liste_cours,acro,0)  #on cherche dans la liste, le cours dont l'acronyme est celui indiqué dans la commande
    
    if cours == False:                          #si on a False dans cours, c'est qu'aucun cours ne porte l'acronyme indiqué dans la commande
        print("Erreur: acronyme incorrect!")    #alos on affiche le message d'erreur 
        return False                            #et on qui la fonction

    if pres not in ['A','P']:                   #si la présence est mal mentionnée
        print("Erreur: présence mal indiquée!") #alos on affiche le message d'erreur 
        return False                            #et on qui la fonction
    
                                                #à ce stade c'est que l'acronyme corresponnd à un cours et la présence est bien indiquée
    
    dossier = get_chemin_dossier_presence() + acro #le chemin qui conduit vers le dossier qui contient les fichiers de présence au cours
    
    if not dossier_existe(dossier):             #si le dossier devant contenir les présence du cours n'existe pas
        creer_dossier(dossier)                  #alors on le crée

    chemin = dossier+'/'+date+'.txt'            #en fonction de la date, on construit le chemin du fichier contenant ou qui devra contenir la liste de présence du jour
    ajouter_presence_etuds(chemin,mats,pres)    #et on complète la présence dans le fichier indiqué dans le chemin
    
    print("Présence complétée au cours de :",cours[1])

def ajouter_presence_etuds(fichier,mats,pres):
    """ accède au fichier de présence et ajoute le(s) matricule(s) de(s) étudiant(s) indiqué(s) dans
    le paramètre mats """
    tab_mat = mats.split(',')                   #s'il y plusieur mat dans mats, ils seront alors séparés par des ','
    sep = ','
    sep_presen_ala_lign = sep + pres + "\n"     #pour chaque matricule il faudra un séparateur (',') un P ou A, pui un \n
    text = sep_presen_ala_lign.join(tab_mat)    #on join tous les mats potentiel
    text += sep_presen_ala_lign                 #on complète aussi la présence du dernier élément

    ajouter_dans_fichier(fichier,text)          #on ajoute le texte au fichier
    poursuivre_la_presence(fichier,sep)         #on demande à poursuivre

def poursuivre_la_presence(fichier,sep):
    print("Poursuivez la présence en indiquant le matricule suivi de P ou A. EX: 12KT237 A (-q pour quitter)")
    mat_p = ""
    while True:                                 #on va tourner en boucle et seul l'utiisateur pour nous sortire de la boucle
        mat_p = input(">>>>: ")                 #
        if mat_p in ["-q","-Q"]:                #si l'utilisateur a tapé -q ou -Q
            break                               #alors on arrête la boucle et on quitte la fonction
        P_OK = ['A','P']
        t = mat_p.split(" ")                    #on découpe la chaine saisie sur ses (' ') on s'assure que l'on a bien                
        if len(t)>=2 and t[1].upper() in P_OK:  #un tableau de plus d'une case et que le 2° élément après l'avoir convenrti en majiscule nous donne A ou P
            p = t[1].upper()                
            text = t[0] + sep + p + '\n'        #on construit le texte de présence
            ajouter_dans_fichier(fichier,text)  #et on l'ajoute au fichier
        else:
            print("Données incorrectes! faites -q pour quitter ")

def importer_presence(cmd,sep=","):
    acro = cmd[0]       #acronyme indiqué dans la commande
    date = cmd[1]
    path = cmd[2]
    id_m = int(cmd[3])   #l'indice de la colonne qui contient les matricule
    id_p = int(cmd[4])   #l'indice de la colonne qui contient les présences

    # if len(cmd)>4:
    #     adress_machine = cmd[4]
    #     rediriger_cmd(adress_machine,cmd[0:-1])
    #     return True

    chemin_cours = get_chemin_fichier_cours()   #on demande le chemin qui mène au fichier des cours
    liste_cours = generer_liste(chemin_cours)   #on génère la liste des cours en lisant le fichier
    cours = element_exist( liste_cours,acro,0)  #on cherche dans la liste, le cours dont l'acronyme est celui indiqué dans la commande
    
    if cours == False:                          #si on a False dans cours, c'est qu'aucun cours ne porte l'acronyme indiqué dans la commande
        print("Erreur: acronyme incorrect!")    #alos on affiche le message d'erreur 
        return False                            #et on qui la fonction

                                                #à ce stade c'est que l'acronyme corresponnd à un cours et la présence est bien indiquée
    
    dossier = get_chemin_dossier_presence() + acro #le chemin qui conduit vers le dossier qui contient les fichiers de présence au cours
    
    if not dossier_existe(dossier):             #si le dossier devant contenir les présence du cours n'existe pas
        creer_dossier(dossier)                  #alors on le crée


    if fichier_existe(path):                    #on commence par s'assurer que le fichier existe vraiment
        liste_p = generer_liste(path)           #on génère une liste de données à patir du path indiqué
        P_OK = ['A','P']
        t = len(liste_p[0])
        if t >= id_m and t >= id_p:
            chemin = dossier+'/'+date+'.txt'
            if len(liste_p[-1])==1:
                del liste_p[-1]
            for lg in liste_p:
                p = lg[id_p].upper()    
                if p in P_OK:            
                    text = lg[id_m] + sep + p + '\n'   #on construit le texte de présence
                    ajouter_dans_fichier(chemin,text)  #et on l'ajoute au fichier
                else:
                    print("Erreur:",lg[id_m],", présence mal indiquée!")
        else:
            print("les indices indiquées ne sont pas correcte")
    else:
        print("Erreur: aucun fichier disponible sur le chemin indiqué!")
        return False
    print("Importation Présence effectuée au cours de :",cours[1])

def rediriger_cmd(adrs,cmd):
    pass