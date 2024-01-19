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
- chown 
