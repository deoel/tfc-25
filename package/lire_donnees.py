from package.config import *

def generer_liste(path):
    """la fonction génère une lite à partir des données lues dans un fichier dont le chemin est reçu en paramètre """
    donnees = lire_data(path)           #donnees est de la forme "...donnee1 \n donnee2 \n donnee3 \n ..."
    tab_lignes = donnees.split('\n')    #on découpe la chaine après chaque passage à la ligne càd ('\n') et on obtient un tableau
    sep = separateur(tab_lignes[0])     #on analyse le premier élément pour savoir le séparateur utilisé
    
    if tab_lignes[-1]=="":              #si le dernier élément est une chaine vide alors
        del tab_lignes[-1]              #on supprime l'élément
    
    Liste = []
    for ligne in tab_lignes:            #ligne est de la forme "... , ... , ..." ou "... ; ... ; ..." 
        tab = ligne.split(sep);         #on découpe la ligne en fonction du séparateur sep
        Liste.append(tab)               #on ajoute le tableau obtenu à la liste
        #print (tab)
    return Liste

def lire_data(path):
    """ la fonction lit un fichier de manière brute et renvoi son contenu """
    fichier = open(path, "r")           #ouverture en lecture seule
    data = fichier.read()               #lecture du contenu
    fichier.close()                     #fermeture du fichier
    return data                         #renvoi du contenu

def separateur(chaine):
    """ on veut juste savoir si le séparateur utilisé est la ',' ou le ';' """
    nbr_V = len(chaine.split(','))-1   #nombre de virgule qu'il y a dans la chiane
    nbr_PV = len(chaine.split(';'))-1  #nombre de point-virgule qu'il y a dans la chaine

    if nbr_V > nbr_PV:                 #s'il y plus de ',' que de ';' dans la chaine
        return ','                     #alors on renvoi ','
    return ';'                         #ou alors on renvoi ';'

def element_exist( liste,cle,indice):
    """ parcourt la liste et cherche l'élément ayant la valeur du paramètre cle à son indice indice """
    if len(liste[0:1])>indice:
        for el in liste:
            if el[indice] == cle:
                return el
    else:
        #print("Indice de recherche incorrect!")
        pass
    return False

def trouver_cours_si_acro_est(acro,return_list=False,message_si_no_exist="Erreur: acronyme incorrect!"):
    chemin_cours = get_chemin_fichier_cours()   #on demande le chemin qui mène au fichier des cours
    liste_cours = generer_liste(chemin_cours)   #on génère la liste des cours en lisant le fichier
    cours = element_exist( liste_cours,acro,0)  #on cherche dans la liste, le cours dont l'acronyme est celui indiqué dans la commande
    
    if cours == False:                          #si on a False dans cours, c'est qu'aucun cours ne porte l'acronyme indiqué dans la commande
        if message_si_no_exist:
            print(message_si_no_exist)          #alos on affiche le message d'erreur 
        return False                            #et on qui la fonction
    if return_list:
        return {"cr":cours,"list":liste_cours}
    return cours
