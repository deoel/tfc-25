from package.server import *
# ============== lancement du service =================
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "Service lancé, Serveur en écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread( clientsocket)
    newthread.start()