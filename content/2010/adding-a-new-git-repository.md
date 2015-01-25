Title: Adding a new git repository
Date: 2010-1-4
Category: Linux
Tags: LPR, howto, git

Some time ago I set up a git server (gitosis) in my desktop computer. I use to commit in my laptop and then push the changes to my desktop
and I really like it.

Today to add a new repository I did:  
In my desktop:  

> cd /tmp  
> git clone gitosis@localhost:gitosis-admin.git  
> cd gitosis-admin  
> (Added Ants_Client to writable, in group developers where I [well, my sshkey] belongs)  
> git commit -a  
> git push

Then in my laptop:

> cd ~/workspace/Ants_Client  
> git init  
> git remote add origin ssh://gitosis@myhomeip/Ants_Client.git  
> git push origin master:refs/heads/master

Useful files:  
/usr/share/doc/gitosis/README.Debian  
/usr/share/doc/gitosis/README.rst.gz
