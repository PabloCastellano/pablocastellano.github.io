Title: Sheevaplug (git server and lighttpd) (unpublished)
Date: 2010-1-20
Category: TODO
Tags: sheevaplug, linux, lighttpd, git

This post should have come before [this one...](http://pablogubuntu.blogspot.com/2010/01/adding-new-git-repository.html)  
Anyways, here it is and that's the important.  
  
The day before I started writing this post, I received my [Sheeva plug computer](http://en.wikipedia.org/wiki/SheevaPlug) (the dream of
every geek) and the next evening I started to set up some things like wordpress running on lighttpd and a git server (which will replace my
desktop computer git server).  
  
  
Sheevaplug by default runs on Ubuntu 9.04 Jaunty.  
- You  cannot upgrade it  
  
Here's how I set up the git server. Currently, there are some mistakes in the documention that made the setup harder :(. I still have to
report them.  
  
\# apt-get install gitosis  
\# ssh-keygen  
\# sudo -H -u gitosis gitosis-init &lt; .ssh/id_rsa.pub  
\# cd /tmp  
  
\# git clone ssh://gitosis@localhost:PortIfNot22/gitosis-admin.git  
  
Here, README.Debian is incorrect. It said to use:  
\# git clone gitosis@localhost:gitosis-admin.git  
But it may not work under some circumstances and is not the right way to do it. According to the man page:  
1- You must specify the protocol (git://, ssh://, http://, ...).  
2- ssh syntax uses colon (":") to specify the port so you cannot use it as separator  
  
Changes to your git server configuration are made using git commits (how geek!). So, once you are have cloned the gitosis-admin repository,
you need to add the sshkeys of people that will have access to the git server.  
  
\$ scp \~/.ssh/id_rsa.pub root@sheeva:/tmp/gitosis-admin/keydir/pablo@tabasco.pub  
  
Y una vez copiada, añadir, hacer commit y push (no olvidar nunca el push o no se salvan los cambios!)  
\# git add keydir/pablo@tabasco.pub \<b\>(double-check it's the public key!!)\</b\>  
\# git commit -a  
\# git push  
\<i\>\# git config push.default matching\</i\>  
  
README.rst.gz is also wrong, because it says that you must copy your public sshkeys to the keys/ directory instead of keydir/, but that was
easier...  
  
Now you can add repositories as explained in the post I mentioned above in the first line.  
  
What else?  
Well, you can install a git-daemon-run in order to allow also anonymous people download git projects. This way you don't need to create a
ssh for everyone :).  
Git public server runs on port 9418 by default.  
  
  
- Movidon con el puto wordpress q al final era ejecutar setup-mysql...  
  
If someone wants a git account even if you know that you are never going to use it, just write me  
Useful links:  
http://scie.nti.st/2007/11/14/hosting-git-repositories-the-easy-and-secure-way  
READMEs are your friend. Well, not in the case of wordpress and gitosis... :S  
Bug reports
