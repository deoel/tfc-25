import random

def ajouter_dans_fichier(path,text):
    """ la fonction ajoute le texte à la fin du fichier et passe à la ligne """
    f= open(path,'a')
    f.write(text)
    f.close()

def supprimer_contenu_fichier(chemin):
    """ la fonction ouvre simplement le fichier le écriture """
    try:
        f= open(chemin,'w')
        f.close()
        return True
    except:
        return  False

def faire_presence_aleratoire(fichier,liste_etus):
    sep = ','
    str_presence = ""
    for etud in liste_etus:
        p = 'A'
        if random.randrange(1,9)%2==0:
            p = 'P'
        str_presence += etud[0] + sep +p + '\n'
    supprimer_contenu_fichier(fichier)
    ajouter_dans_fichier(fichier,str_presence)