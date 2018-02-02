import socket
import threading
import time

class ClientThread(threading.Thread):
    def __init__(self, ip_server="127.0.0.1", port=1111):
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip_server, 1111))
        self.reponses_serv = []
        # self.s.send("chado.txt")

    def run(self): 
        rep_serv = self.s.recv(9999999)
        # print(rep_serv)
        hr = time.localtime()
        ficher_rep = "rep_serveur/%s-%s-%s.txt" % (hr.tm_hour,hr.tm_min,hr.tm_sec,)
        with open(ficher_rep,'wb') as _file:
            _file.write(rep_serv)
        
        beeper_lutilisateur()

    def envoyer_requete(self,req):
        self.s.send(req.encode())
    
    def fermer_connexion():
        self.s.close()

def beeper_lutilisateur(frequence= 2500,duree= 1000):   # Set Frequency To 2500 Hertz 
    import winsound                                     # Set Duration To 1000 ms == 1 second  
    winsound.Beep(frequence , duree)


