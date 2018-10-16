# Threaded File Transfer Lab

This directory contains a version of the file transfer lab that utilizes
threading to handle multiple clients. Locks are used to prevent complications
when two clients try to upload a file of the same name; namely, the lock is
placed so only one client can open a file on the server at a time. It's "first
come, first serve"; the server will not upload a file from the client if it
already exists on the server.

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

* Test sending two files at once using '&' (ex: ./threadClient.py -f foo.txt &
  ./threadClient.py -f goo.txt

* To terminate the server, enter Ctr-C Ctrl-C into the server's terminal.
~~~
* The file will be uploaded to the /server folder by the server.

## Bugs & Problems

* There is a bug in this program when using the stammer proxy to upload files
that already exist on the server: sometimes, the connection will break with an
unbound local error reading "local variable 'b' refrenced before assignment"
on the stammer proxy and an attribute error reading "NoneType opbject has no
attribute 'decode'" on the server.

The fact that the client does not get notified when file already exists (and
therefore keeps sending even if the server will not recieve input properly)
may be a big part of this problem, but this is only a guess - the true problem
is unclear.


* Attempts to send messages from the server to the client turn out strangely:
  all messages sent out turn into "None" and never seem to make it out of the
  framed send and recieve methods in its proper form.

## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources
is clearly documented.

This README is tailored for grading anonymity. For full attributions, see
COLLABORATORS.md.

