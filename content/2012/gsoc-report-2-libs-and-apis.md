Title: GSOC Report #2: libs and APIs
Date: 2012-6-5
Category: TODO
Tags: gsoc2012, guifi.net

I have added some checkbuttons that allow you to show and hide the labels and the points of the nodes. Apart from that, there aren't more
features this week.

### Libchamplain

I have subscribed to [their mailing list](https://mail.gnome.org/archives/libchamplain-list/) and I have the pending task of reading its
archive.

The other patches I sent, were merged into master as well :)

Other things that I had not considered are:

-   There's a [ChamplainPathLayer](http://developer.gnome.org/libchamplain/unstable/ChamplainPathLayer.html) layer type to draw paths. I
    thought that it would work to draw links between nodes but what it really does is drawing just one path, that is, lines that pass by the
    points you want but they are all together. It means that I cannot use just one PathLayer to draw the links between different nodes. It's
    like drawing the lines with a pencil without raising the hand.
-   I think I found another bug because I cannot directly change the size of the points even when there's a specific [method for
    that](http://developer.gnome.org/libchamplain/unstable/ChamplainPoint.html#champlain-point-set-size). I have to remove the marker from
    the layer and then create a new point with a different size and finally re-adding it to the same layer.

For the first issue I have two solutions in mind:

1.  Using a layer for each link and all of group them in a list of layers.
2.  Creating a new layer type that allows you to have lines that link points instead of just one path.

Libchamplain uses [Clutter](http://www.clutter-project.org/) to draw widgets on the map. I'm getting familiarized with it too. A good widget
to implement would be a smaller world map that allowed you to click on it and move quickly through the map, as a magnifying glass.

### APIs and GObject

I've started drawing some UML diagrams to design an API that deals with CNML files without having to deal with XML at the same time. I will
also do the same for the API to interact with the Guifi.net website.

I want the code I write to be as much reutilizable as possible by other people. For this purpose, I'm still fascinated about GObject. I
would like to write these API libraries using Vala/GObject so that the bindings for other languages can be easily and dynamically generated.
It will be harder as I don't have any real previous experience with GObject but it will be worth I think :)

I found a talk given by [**Tal Liron**](http://emblemparade.net/) in December 2011 during a Chicago Python User Group
([**ChiPy**](http://chipy.org/)) conference. He gives a good explanation of GObject Introspection.

\
[**GObject and Vala**](https://www.youtube.com/watch?v=6QrGmA_RR4E)

By the way, the current version of GObject Introspection doesn't support default parameters in languages that are allowed (like Python).

For this reason at the moment you cannot write:

> self.embedBox.pack\_start(self.embed)

because it will complain about the number of parameters. You have to specify all of them:

> self.embedBox.pack\_start(self.embed, True, True, 0)

 

It's already reported, see [bug 558620](https://bugzilla.gnome.org/show_bug.cgi?id=558620).

 

### Useful links

 

More about GObject and Introspection in the GNOME Wiki:

-   [PyGObject](https://live.gnome.org/PyGObject)
-   [PyGObject/IntrospectionPorting](https://live.gnome.org/PyGObject/IntrospectionPorting)
-   [GObjectIntrospection](https://live.gnome.org/GObjectIntrospection)
-   [GObjectIntrospection/Annotations](https://live.gnome.org/GObjectIntrospection/Annotations)
-   [GObjectIntrospection/Architecture](http://live.gnome.org/GObjectIntrospection/Architecture)
-   [GnomeGoals/AddGObjectIntrospectionSupport](https://live.gnome.org/GnomeGoals/AddGObjectIntrospectionSupport)

Others:

-   [Genie](https://live.gnome.org/Genie), like Vala but with Pythonic syntax
-   [https://github.com/antono/vala-object](https://github.com/antono/vala-object)

### Next week

To be honest I won't do so much, I start my exams in two days from now. I will continue with the diagrams and thinking about the APIs.

[](http://lainconscienciadepablo.net/content/gsoc-report-2-libs-and-apis)

[![Flattr
this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/712478/GSOC-Report-2-libs-and-APIs)
