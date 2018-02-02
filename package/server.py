import socket
import threading
from package.demandes_distantes import *

class ClientThread(threading.Thread):

    def __init__(self, clientsocket):

        threading.Thread.__init__(self)
        self.clientsocket = clientsocket

    def run(self):
        cmd_str = self.clientsocket.recv(2048)
        reponse = analyser_demande_distante(cmd_str)
        # print(reponse)
        self.clientsocket.send(reponse.encode() )
# ================= Fin de la class ================================

