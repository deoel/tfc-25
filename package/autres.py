

def ajouter_dans_fichier(path,text):
    """ la fonction ajoute le texte à la fin du fichier et passe à la ligne """
    f= open(path,'a')
    f.write(text)
    f.close()