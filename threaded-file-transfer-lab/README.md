# Threaded File Transfer Lab

This directory contains a version of the file transfer lab that utilizes
threading to handle multiple clients.

To transfer a file:
* Start the server. This is done by typing ./threadServer into the terminal.
* Start the client upload. To upload a certain file, enter "./threadClient.py -f
FILENAME" into the terminal. In order for the upload to commence, the file
must already exist.
~~~
* To change the socket, use -s addr:socket
* The client should still be able to upload through the given stammer proxy.
* To terminate the server, enter Ctr-C Ctrl-C into the server's terminal.
~~~
* The file will be uploaded to the /server folder by the server.

## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources
is clearly documented.

This README is tailored for grading anonymity. For full attributions, see
COLLABORATORS.md.

