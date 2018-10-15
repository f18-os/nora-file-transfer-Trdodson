#! /usr/bin/env python3

# Client file transfer program. Based on emphaticDemo: see COLLABORATIONS for details.
import socket, sys, re
import params
from framedSock import FramedStreamSock
from threading import Thread
import time

switchesVarDefaults = (
    (('-s', '--server'), 'server', "localhost:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False),
    (('-f', '--file'), 'file', "default.txt"), # File parameter.
    )

progname = "threadClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug, fileName = paramMap["server"], paramMap["usage"], paramMap["debug"], paramMap["file"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

class ClientThread(Thread):
    def __init__(self, serverHost, serverPort, debug):
        Thread.__init__(self, daemon=False)
        self.serverHost, self.serverPort, self.debug = serverHost, serverPort, debug
        self.start()
    def run(self):
       s = None
       for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
           af, socktype, proto, canonname, sa = res
           try:
               print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
               s = socket.socket(af, socktype, proto)
           except socket.error as msg:
               print(" error: %s" % msg)
               s = None
               continue
           try:
               print(" attempting to connect to %s" % repr(sa))
               s.connect(sa)
           except socket.error as msg:
               print(" error: %s" % msg)
               s.close()
               s = None
               continue
           break

       if s is None:
           print('could not open socket')
           sys.exit(1)

       print("Success! Trying to open %s" % fileName)
       
       try:
           fs = FramedStreamSock(s, debug=debug)  #Use framedSock class.
           try:
               myFile = open(fileName, 'rb')
           except FileNotFoundError:
               print("ERROR: File doesn't exist. Stopping...")
               fs.sendmsg(b"error") # Send Error if file doesn't exist.
               s.close()
               exit()

           fs.sendmsg(b"accept")    # Send an accept if everything is fine!
        
           fs.sendmsg(fileName.encode()) # Send file name.
           fs.sendmsg(b"") # Send this so they know they got it all!
           
           print("sending %s" % fileName)
           
           line = myFile.read(100)  # Start reading from the file.
           while(line):
               fs.sendmsg(line)    # Send file line by line.
               line = myFile.read(100)
           myFile.close()
           print("%s sent." % fileName)
       except:
           print("ERROR: Broke connection. Exiting...")
           exit()

for i in range(1):
    ClientThread(serverHost, serverPort, debug)
