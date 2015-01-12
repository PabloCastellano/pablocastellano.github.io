Title: GSOC Report #0: Documentation
Date: 2012-5-22
Category: TODO
Tags: guifi.net, gsoc2012

-Note: I forgot to say in my last post that all coming posts about GSOC will be in English-\
Well, the coding period started yesterday. Here is what I've been doing meanwhile during the documentation period:

 

Project name
------------

First, I decided to change the project name from "*CNML Explorer*" to "**Guifi.net Studio**".

Why? *CNML Explorer* was the main idea of creating an application to visualize CNML files offline. Now the project is more generic and has
more features apart from visualizing CNML files so I felt like the name wasn't accurate anymore. Guifi.net Studio aims to be a the Guifi.net
desktop tool, for example, it will also interact with the Guifi.net web API and will contain more features to make life easier to the
Guifi.net community ;)

I prefer this name, but let me know if you have an even better one! I'm still not 100% convinced about it so I'm open to new suggestions.

 

Rendering maps
--------------

There are several libraries to render Open Street Maps into GTK+. I had several candidates for this position and finally, the winner is
called **libchamplain**!

Libchamplain is written in C but it takes advantage of GNOME's **[GObject Introspection](https://live.gnome.org/GObjectIntrospection)** to
get the Python (and other languages) bindings for free! Cool tech :) (Generating Python bindings manually belongs to the past now).

 

I chose it because it's easy to install (it's included in the Debian/Ubuntu repostiories), it has the enough features that I need at the
moment and the development looks active.

Actually there are some [apps using libchamplain](https://live.gnome.org/libchamplain/applications) like
[emerillon](http://projects.gnome.org/emerillon/index.html) (map viewer,
[screenshots](http://projects.gnome.org/emerillon/screenshots.html)), which is also a good sign.

 

[Code example](http://projects.gnome.org/libchamplain/reference.html) (Python snippet are available [in the Git
repository](http://git.gnome.org/browse/libchamplain/tree/demos/launcher-gtk.py))
and [documentation](http://developer.gnome.org/libchamplain/) are also available.

 

Other utilities found in the way are:

-   [python-imposm-parser](http://dev.omniscale.net/imposm.parser/)
-   [libmemphis](http://trac.openstreetmap.ch/trac/memphis/wiki/LibMemphis)
-   [gosm](http://gosm.sourceforge.net/req.html) (webkit)
-   [python-osmgpsmap](http://nzjrs.github.com/osm-gps-map/docs/reference/html/OsmGpsMap.html)

Due to some [annoying bug in the Clutter version](https://bugs.launchpad.net/ubuntu/+source/cheese/+bug/890503), I had to upgrade to Ubuntu
12.04. If you use Ubuntu and you want to test Guifi.net Studio you will probably have to upgrade too.

 

Community
---------

I have [chatted](https://lists.funkfeuer.at/pipermail/interop-dev/2012-May/000096.html) and got in contact with people from other wireless
communities in Europe (FunkFeuer and Ninux this time) that are also interested in the interoperability subject. I got good impressions :-)

If you are interested in interoperability too, you should subscribe to the [interop-dev mailing
list](https://lists.funkfeuer.at/mailman/listinfo/interop-dev). We will meet there.

I will possibly meet some of them at the [Italian Hackmeeting 2012](http://it.hackmeeting.org/) (end of June) in
[L'Aquila](https://es.wikipedia.org/wiki/L'Aquila).

 

Status of Hybrid Nodes
----------------------

Hybrid nodes have become definitely more popular than old supernodes when you had to deal with miniPCI radios and routerboards.

This new prototype is easier to build and gives better performance. 

I didn't know exactly how they were technically configured, now I have understood :-)

Unsolclick configuration is not available for hybrid nodes at the moment. The work is done but the code isn't merged :(. I will also try to
push it forward.

Here there is some documentation about hybrid nodes that helped me to understand them:

-   in the [acacha wiki](http://acacha.org/mediawiki/index.php/Model_h%C3%ADbrid_guifi.net) (Catalan, but self-explainatory thanks to
    the screenshots)
-   [Guifi.net wiki](http://es.wiki.guifi.net/wiki/Modelo_h%C3%ADbrido_guifi.net) (same but translated into Spanish)
-   [Blackhold's blog](http://blackhold.nusepas.com/2011/04/nodos-hibridos-guifi-net/) (the best, Spanish)
-   And [this conference](http://blip.tv/guifimedia/9a-conferencia-sax-2011-wireless-battle-of-the-mesh-v4-5024864) during SAX 2011 (Catalan
    and Miquel specially speaks quite fast :-P):

 

API
---

I have familiarized myself with the Guifi.net API. Isidro is also a student that is doing a project that interacts with the API from
Android. He has done a great work too, testing it and [reporting a lot of bugs and
improvements](http://trac.guifi.net/query?status=!closed&component=Web+guifi.net+%3A+API).

Optic Fiber
-----------

Ramón Roca gave me access to the [Alfresco platform](http://workspaces.guifi.net), where there are a lot of interesting documents about
Guifi.net!\
I have seen how the optic fiber links are documented and I have some ideas to generate cute SVG graphs automatically from the data.\
According to my calendar, I will work on it in July.

 

Development
-----------

I have started a [new repository](https://gitorious.org/guifi-altres/guifinetstudio) in Gitorious, where all the Guifi.net development takes
place. At the moment there's only the code made during last summer as proof of concept.

You can get it by typing:

> git clone git://gitorious.org/guifi-altres/guifinetstudio.git

There's also a new component at [trac.guifi.net](http://trac.guifi.net%20), so the bug tracking will happen there.

 
-

This week
---------

I will be working in the user interface and unsolclick configuration for simple nodes. [Albert Sarlé](https://gitorious.org/~albertsarle)
(who I met two weeks ago) has done a great work about it during his final project in the university. He made the configuration possible
using templates (among other things).

Unfortunately my final exams are close and I won't be able to spend all the time I would like on it :(\
Have a good week!

[](http://lainconscienciadepablo.net/content/gsoc-report-0-documentation)

[![Flattr
this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/690146/Guifi-net-Studio-GSOC-Report-0-Documentation)
