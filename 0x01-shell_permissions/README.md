# 0x01. Shell, permissions
This directory containts the 0x01. Shell, permissions project with its tasks. <br>
Here, we learnt about all the permissions of a file in shell <br>

Here are the tasks in this project:<br>
## Tasks
### 0. My name is Betty
- Learnt how to use ``su`` (switch user) to switch between users
- when `su`` is used without a command after, it resorts to the super user
- switching to specific user requires that you include the name of the user after

### 1. Who am I
- ``whoami`` command mentions the name of the current user

### 2. Groups
- ``id`` is used to display the user and group information of the current user

### 3. New owner
- ``chown`` changes the file owner
- syntax is ``chown [user] [file]``

### 4. Empty!
- ``touch`` command creates a new empty file

### 5. Execute
- ``chmod`` (change mode) changes the read(r), write(w), and execute(x) permissions of a file to different users

### 6. Multiple permissions
- ``chmod`` can be used to change multiple modes for multiple users if each is separated by a comma, i.e ``chmod u+x,g+r,o+w [filename]``

### 7. Everybody!
- you can also combine users if the mode changed is the same i.e ``chmod ugo+x [filename]`` to make the file executable for the user(u), group owner(g), and other users(o)

### 8. James Bond
- Chmod can also be used with octal numbers i.e 007 ``chmod 007 [filename]``

### 9. John Doe
- This was a custom assignment to change a file's permissions to ``-rwxr-x-wx``
- This is best handled using octal numbers (where rwx are represented by 1, 2, 4 respectively) but letters could also work
- In this case, it is 753 which would be ``chmod 753 [filename]``

### 10. Look in the mirror
- This was similar to the previous task but with these permission ``-rw-rw-r--`` translating to 664
- However, since it was a reference file that already exist, chmod also allows to copy permissions from  references using ``chmod --reference=[reference_filename] [filename]``

### 11. Directories
- Chmod also allows to change permission recursively to all files in directories
- For this, we use the ``-R`` (recursive)

### 12. More directories
- This is a ``mkdir`` feature with ``-m`` as the permission feature

### 13. Change group
- we use ``chgrp`` to change the group owner to a certain individual like ``school`` of a file

### 14. Owner and group
- ``chown`` (change owner) changes the owner of a file(s) or directory(s) in this syntax and order: ``chown new_owner:new_group/new_group_owner [filename]`` with a "-R" command after chown when using [directory] instead of [filename]; and the ":" can be ignored when only changing the "new_owner."
- in this case chown is used with '-R' argument since it is directories (all) that are changing (technically all files in the directories)
- then the ":" has to be used since we are changing both ``new_owner`` and ``new_group``


## ADvanced Tasks
### 15. Symbolic links
- Symbolic links are simply files that contain the PATH (Symbols to) another file or a directory (Remember, everything in a computer is either a file or a directory)
- changing a file through the link does not affect the original file but changing the original file affects the file in the link.
- a link allows you to view and manipulate the contents of a file in another different place, from where you are in the whole file system
- in older systems (and others today), a link would simply take you to that directory where the file is, or simply open or execute the file

- in our case, we treat the link as a file and assume we are changing the owner and group owner of the file using ``chown``

### 16. If only
- ``chown`` has the ability to accept arguments like ``--from`` and ``reference`` and so many others.
- in this case, ``chown --from=[owner_of_reference_file(s)] [new_owner] [file_to_change_ownership]`` would be best appropriate reference, eve though there are other more tedious methods

### 17. Star Wars
- The ``telnet command`` is a network protocol used for remote terminal access to a server or another computer over a network. It allows users to interact with a remote system's command-line interface as if they were physically present at that machine.
- In the case of playing Star Wars in the terminal, the telnet command is used to connect to a specific server(technically a computer), towel.blinkenlights.nl. When you run the ``command telnet towel.blinkenlights.nl``, your terminal establishes a connection with this server.
- The Star Wars ASCII art is not a pre-stored file but is generated dynamically by a program running on the server. As characters are sent over the network from the server to your terminal, they create the visual representation of the Star Wars movie through ASCII art.
- While ``telnet`` provides a basic form of remote access to a server's command-line interface, it lacks the advanced features, security, and graphical user interfaces offered by modern remote desktop applications like AnyDesk. These applications provide a more comprehensive and user-friendly experience for remote access and control.
