import os

def creer_fichier(chemin):
    if chemin[-1]!="/":                #le dernier caractère du chemin ne doit pas être un '/'
        f = open(chemin,'w')           #on crée le fichier à partir du chemin réçu et
        f.close()                      #on le ferme aussitôt après, sans rien n'y écrire

# le paramètre chemin est de la forme: presence/G1/py/12-01-2018.txt
def creer_dossier_puis_fichier(chemin):    
    """ la fonction crée le fichier dont le chemin est fourni en paramètre """
    r = os.path.split(chemin) # sépare le fichier des dossiers
    les_dossier = r[0]        # les différents dossiers EX: presence/G1/py/
    fichier     = r[1]        # le fichier              Ex: 12-01-2018.txt

    try:
        if not os.path.isdir(les_dossier): #si le dossier et les sous-dossier du chemin n'existent pas
            os.makedirs(les_dossier)       #on les crée, et après cela 
            creer_fichier(chemin)          #on crée le fichier
        #ou alors si les dossiers existent, on s'assure que le fichier lui n'exite pas, de cette manière on peut le créer
        elif not os.path.isfile(chemin):   #si le fichier n'existe pas
            creer_fichier(chemin)          #on crée le fichier
        
        else:       # sinon comprennez bien que dans ce cas c'est que les dossiers
            pass    # existent et le fichier existe donc inutile de créer quoique ce soit
        return True
    except :
        print ("Erreur: impossible de créer le fichier")
        return False

# le paramètre chemin est de la forme: presence/G1/py/
def get_contenu_dossier(dossier):
    """ la fonction dois trouver tous les fichiers qu'il y a dans le dossier py, 
    sous dossiers du dossier py et le renvoyer dans une liste """
    if(dossier[-1]=='/'):           #si le dernier caractère du chemin du dossier indiqué en paramètre
        dossier = dossier[0:-1]     #est un '/' alors on le supprime, très cooool non!!!
    L_contenu = [] 
    if os.path.isdir(dossier):                          #on vérifie si le dossier existe bel-et-bien
        for element in os.listdir(dossier):             #on pique chaque élément du dossier
            chemin = dossier+"/"+element                #on reconstruit le chemin de l'élément à paritr du dossier
            if os.path.isdir(chemin):                   #et on vérifie si cela conduit à dun dossier ou un fichier
                cont_s_doc = get_contenu_dossier(chemin)#si il conduit à un sous-dossier, on récupère le contenu
                L_contenu.extend(cont_s_doc)            #et on étend avec la liste prinicpale
            else:                                       #sinon il s'agit alors d'un fichier et dans cas
                L_contenu.append(chemin)                #on l'ajout simplement à la liste princial
    
    return L_contenu                                    # et après avoir tout récupérer on retourne la liste


# ========================================================
def dossier_existe(chemin):
    return os.path.isdir(chemin)
    
def fichier_existe(chemin):
    return os.path.isfile(chemin)
    
def creer_dossier(chemin):
    os.makedirs(chemin)