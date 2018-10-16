# Threaded File Transfer Lab

This directory contains a version of the file transfer lab that utilizes
threading to handle multiple clients. Locks are used to prevent complications
when two clients try to upload a file of the same name; namely, the lock is
placed so only one client can open a file on the server at a time. It's "first
come, first serve".

To transfer a file:
* Start the server. This is done by typing ./threadServer into the terminal.
* Start the client upload. To upload a certain file, enter "./threadClient.py -f
FILENAME" into the terminal. In order for the upload to commence, the file
must already exist.
~~~
* To change the socket, use -s addr:socket
* The client should still be able to upload through the given stammer proxy listening on
port 50000.
* You can specify a new file name for the chosen file to have on the server: use
-dst to do this (example: ./threadClient.py -f README.md -dst foo.txt. The
README file will be uploaded as 'foo.txt'.)
* To terminate the server, enter Ctr-C Ctrl-C into the server's terminal.
~~~
* The file will be uploaded to the /server folder by the server.

## Bugs
* There is a bug in this program when using the stammer proxy to upload
two of the same file with two different clients: sometimes, the connection will break with an unbound
local error reading "local variable 'b' refrenced before assignment. The fact
that the client does not get notified when file already exists (and therefore
the server will not recieve any input) may be part of this problem.


## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources
is clearly documented.

This README is tailored for grading anonymity. For full attributions, see
COLLABORATORS.md.

