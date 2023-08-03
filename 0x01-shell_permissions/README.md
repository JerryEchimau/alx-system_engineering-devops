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
11. chmod --reference-olleh - checks the permissions in file olleh and referes them to the file indicated, in this case, hello
12.    
