Shell permissions exercise

1. su betty - switches the current user to user betty using the su command
2. whoami - this gets the effective username of the current user
3. id -Gn - this prints all groups that the current user is part of
4. chown betty hello - changes the owner of the file called hello to user betty
5. touch hello - creates an empty file called hello
6. chmod u+x - is a command that gives the owner of the file permission to execute
7. chmod u+x,g+x,o+r - gives the owner (u) and group (g) the permission to execute (x) and other (o) users the permission to only read (r)
8. chmod ugo+x - gives all users (u,g, and o) permission to eecute (x)
9. chmod 007 - gives only the other users all permissions (7)
10. chmod 753 - translates to (rwx - r-x - -wx) permissions for all three category of users
11. chmod --referenc=olleh - checks the permissions in file olleh and referes them to the file indicated, in this case, hello
12. chmod -R +X . - this use recursive command to change the permission of a directory and the +X gives eecute permissions to these files and directories
13. mkdir -m 751 - creates a directory and the -m creates the permission of the created directory as 751 in this case
14. chgrp - command that changes group owner
15. chown -R vincent:staff . - changes the owner and group owner of all files and directories in the cwd recursively
16. chown -h - changes the owner while specifying that it's a symbolic link
17. chown —from=guillaume Betty hello - conditionally changes the owner of a file if it is woned by the specified user
18. 
