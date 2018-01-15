from package.gerer_fichier import *
CHEMIN_FICHIER_ETUDIANT        = "donnees/G1/etudiants.txt"
CHEMIN_FICHIER_COURS           = "donnees/G1/cours.txt"
CHEMIN_DOSSIER_PRESENCE        = "donnees/G1/presences/"

def get_chemin_fichier_etudiant():
    return CHEMIN_FICHIER_ETUDIANT

def get_chemin_fichier_cours():
    return CHEMIN_FICHIER_COURS

def get_chemin_dossier_presence():
    return CHEMIN_DOSSIER_PRESENCE

def get_chemin_fichier_presence(acronyme_du_cours,date_presnce):
    if CHEMIN_DOSSIER_PRESENCE[-1]=="/":
        CHEMIN_DOSSIER_PRESENCE += "/"
    return CHEMIN_DOSSIER_PRESENCE + acronyme_du_cours + "/" + date_presnce + ".txt"
    # ou
    # return get_chemin_dossier_presence()+"{}/{}.txt".format(acronyme_du_cours,date_presnce)

def creer_fichiers_de_base():
    creer_dossier_puis_fichier(get_chemin_fichier_etudiant())
    creer_dossier_puis_fichier(get_chemin_fichier_cours())
    creer_dossier_puis_fichier(get_chemin_dossier_presence())

# la fonction importe la liste des étudiants et des cours se trouvant dans les fichiers .csv vers nos fichier .txt
def importer_donnee_source(fichier_source_etudiant,fichier_source_cours):
    #importer la liste des étudiants qui sont le fichier .csv vers notre fichier .txt
    f = open(fichier_source_etudiant,"r")
    contenu = f.read()
    f.close()
    #nous allons ouvrir notre fichier d'étudiant et y copier le contenu vernat du fichier_source
    f = open(get_chemin_fichier_etudiant(),"w")
    f.write(contenu)
    f.close()

    #importer la liste des cours
    f = open(fichier_source_cours,"r")
    contenu = f.read()
    f.close()
    #nous allons ouvrir notre fichier de cours et y copier le contenu vernat du fichier_source
    f = open(get_chemin_fichier_cours(),"w")
    f.write(contenu)
    f.close()

def reinitialiser_tout_le_system(csv_etudiant,csv_cours):
    creer_fichiers_de_base()
    importer_donnee_source(csv_etudiant,csv_cours)

