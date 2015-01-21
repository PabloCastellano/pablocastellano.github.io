Title: Bringing buoh back to life
Date: 2009-12-23
Category: TODO
Tags: gnome, git, debian, cvs, buoh

![](/img/buoh.png) Buoh is a simple but practical project. Its web page defines buoh as "The online comic reader application for GNOME"

I don't know how I discovered it but I looked at the screenshots I liked it. Minutes later I discovered that the buoh package had been
removed from the Debian repositories and therefore from the Ubuntu repositories too. The reason is in [this debian bug
report](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=523534).

I checked that the bug report was true... there hadn't been movement in their mailing list for a long time, commits neither in their CVS.  
I decided to bring the project to life and I contacted the authors (three spanish guys) of buoh as I could (their specified emails didn't
belong to them anymore, except the one from Carlos). They told me it had started as a project to learn programming in GTK/GNOME and then
they didn't have any time to maintain it, but that they would feel very happy if someone else took the maintaining responsibility. We would
also move it to git.gnome.org.

Migrating from CVS to Git was a little odyssey too. I tried with the cvs2git script but I couldn't because certain "*,v" files were missing
and also the directory tree wasn't correct at all. Boh. I also tried with "git cvsimport" without much more luck, but then I don't know what
I changed in the parameters and it worked :). See one of the links in the bottom of this post.

I ported it to libsoup2.4 and fixed some other things.

The final result is that buoh satisfied all the rules to be uploaded to git.gnome.org and after a little clean up of unused branches I
finally did it.

I will keep working on it in the next days taking advantage of the moment because I feel excited now and I have free time :)

I have also plans in 2010 to become a [Debian New Maintainer](https://nm.debian.org/) and buoh is a perfect candidate package to maintain :)

Related links:

- [http://git.gnome.org/browse/buoh/](http://git.gnome.org/browse/buoh/)
- [http://buoh.steve-o.org/screenshots.html](http://buoh.steve-o.org/screenshots.html)
- [http://issaris.blogspot.com/2005/11/cvs-to-git-and-back.html](http://issaris.blogspot.com/2005/11/cvs-to-git-and-back.html)
- [http://joaquin.axai.mx/cvs-desde-git-y-como-mantenerlos-sincronizados](http://joaquin.axai.mx/cvs-desde-git-y-como-mantenerlos-sincronizados) (Spanish)
