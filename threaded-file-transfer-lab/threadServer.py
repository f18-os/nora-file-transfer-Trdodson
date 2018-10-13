#! /usr/bin/env python3
import sys, os, socket, params, time
from threading import Thread
from framedSock import FramedStreamSock

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "threadServer"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

class ServerThread(Thread):
    requestCount = 0            # one instance / class
    def __init__(self, sock, debug):
        Thread.__init__(self, daemon=True)
        self.fsock, self.debug = FramedStreamSock(sock, debug), debug
        self.start()
        
    def run(self):

        fileName = "default"
        msg = self.fsock.receivemsg()  # First receive gets file name.
        
        while(msg != b""):             # Recieve filename and stop when client sends an empty array.
            fileName = msg.decode("utf-8")
            msg = self.fsock.receivemsg()
            
        filePath = os.getcwd() + "/server/" + fileName #Build path for file.
        
        myFile = open(filePath, 'wb')
        
        while True:                    # Write to file until there is nothing to recieve!
            msg = self.fsock.receivemsg()
            if not msg:
                if self.debug: print(self.fsock, "server thread done")
                myFile.close()
                return
            myFile.write(msg)
            
            requestNum = ServerThread.requestCount
            time.sleep(0.001)
            ServerThread.requestCount = requestNum + 1
            msg = ("%s! (%d)" % (msg, requestNum)).encode()


while True:
    sock, addr = lsock.accept()
    print("Connection recieved from:", addr)
    ServerThread(sock, debug)
