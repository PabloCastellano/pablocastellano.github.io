Title: GSOC Report #1: Maps
Date: 2012-5-27
Category: TODO
Tags: guifi.net, gsoc2012

Today I have finished adding the libchamplain support to the old interface. Here I leave a screenshot:

[![](/img/guifinetstudio1.png)](/img/guifinetstudio1.png)

There you can appreciate that there's a bold point and a label for every node. I still have to draw the lines representing the links between
nodes and improve the style and the logic of the labels so that they don't become a
[*smudge*](http://www.wordreference.com/es/translation.asp?tranword=smudge) when the nodes are close (like it happens in the above picture).

I know it crashes a lot (for example if you change the view before the map is fully loaded). I will fix these little bugs in the next days.

At the end of the study of the libchamplain API I have sent some patches to the project (two to improve the documentation and another one to
fix the Python example) :-)

-   [Typo in documentation](https://bugzilla.gnome.org/show_bug.cgi?id=676892) (bug \#676892, already merged
    into [*master*](http://git.gnome.org/browse/libchamplain/commit/?id=ba3e573539939ae02ec686901b452c466b0c4e4e)) 
-   [Improvements in documentation](https://bugzilla.gnome.org/show_bug.cgi?id=676908) (bug \#676908)
-   [launcher-gtk.py: get\_coords() method doesn't exist](https://bugzilla.gnome.org/show_bug.cgi?id=676893) (bug \#676893)

I really like the libchamplain API design.

# How to try it

If you want to try it, all you have to do is getting the code from the Git repository and installing the dependences. You can find the
necessary steps in the [README](https://gitorious.org/guifi-altres/guifinetstudio/blobs/master/README) file. These are steps for Ubuntu
12.04 users:

> sudo apt-get install python2.7 gir1.2-gtkchamplain-0.12 git  
> git clone git://gitorious.org/guifi-altres/guifinetstudio.git  
> cd guifinetstudio  
> ./guifinet\_studio.py  
>  

# Next week

I will start implementing unsolclic. I will take advantage of the work done by Albert Sarlé :). Until today I planned to use the django
template engine (he used Twig for PHP which has a similar syntax) but I have discovered [**Jinja2**](http://jinja.pocoo.org/docs/) which is
a stand-alone template engine with the same syntax as well, faster and you don't need to install the whole Django libraries.

[![Flattr this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/699059/GSOC-Report-1-Maps)
