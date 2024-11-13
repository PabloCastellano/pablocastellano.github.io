+++
date = '2012-08-22T00:00:00+02:00'
title = 'GSOC Final Report'
categories = ['Google Summer of Code']
series = ['Google Summer of Code']
tags = ['guifi.net', 'GSoC2012']
+++

And this is a summary of the features implemented during this summer into Guifi.net Studio.

I have taken the list of features that I wrote when I was doing the proposal for the GSoC. You can have a look at this list [here](http://en.wiki.guifi.net/wiki/Guifi.net_Studio).

# Filtering options

Implementation status: 75%

Filtering by node title is possible. However, advanced filtering is not available but will be (filtering by node/supernode, number of links, links length, type of devices...)

# View nodes in map

Implementation status: 90%

Guifi.net Studio uses an external library called libchamplain to render an OSM layer overlay layers on it. At the moment it uses two layers: one for nodes (points) and another one for node titles (labels).

Links between nodes are not shown because this type of layer (drawing separated lines) is not supported by libchamplain. I want to implement this kind of layers in libchamplain.

# Unsolclic

Implementation status: 60%

Guifi.net can generate Unsolclic configurations using the same templates system that are being used in the website recently. So, we can say that both generated unsolclic's are "compatible". At the moment, it's only working for Ubiquity AirOS firmware.

I will continue the work to do so that templates are dynamically loaded and so, adding and configure a new template is as simple as moving it to a specific folder.

# Export subzone to another file

Implementation status: 0%

Undone. It turned out to be useless because you can download those same subzones from the website.

# Export to other formats like .gml or .kml (Google Earth)

Implementation status: 50%

Export to KML works fine thanks to an external library but exporting to GML is not possible at the moment. I couldn't find an API to deal with GML files so at the moment this is feature is blocked until I find some way to generate them.

# Cache OSM data (I don't know if any library already does it)

Implementation status: 100%

Done! Luckily libchamplain does it internally.

In the future, I will do some tunning to the internals so that it uses the cached files unless they are older than 10 days or so... This way, Guifi.net Studio won't download the maps every time it runs.

# Different ways to visualize nodes in the map. The user can change the color, thickness and type of the line that links two nodes; show supernodes only; show supernodes with >=N links...

Implementation status: 30%

Libchamplain is quite limited in this aspect... Before, it's necessary to extend the library and add these features.  A good place to extend it is the GtkGuifinetMap widget.

# The main window can have two modes of visualization: 1) Map (default) 2) Node list

Implementation status: 100%

It's working. Besides that, a new idea came up which is placing a third button for "Services". This is in a new TODO list.

# Check CNML integrity twice / Check wrong MAC address, zones, ip ranges...

Implementation status: 80%

CNML is checked using DTD validation and adding a second validation for attribute values wasn't really a priority. It would also show a lot of invalid data because e.g. there are a lot of people that has entered invalid or duplicated MAC addresses like 11:11:11:11:11:11

# Improve integration with drupal-guifi

I have submitted some patches to fix bugs in the Drupal Guifi.net module.

There's still some work to be done, specially in the server side API, which is not fully completed. I will assume this task too but more relaxed.

# Integrate with map profile

Implementation status: 0%

It wasn't a priority neither. I also have to ask what is the status of the [heywhatsthat](http://www.heywhatsthat.com/) service in the website. As far as I know, Guifi.net got banned from using their API because of its huge traffic of requests.

# Generate HTML report of any zone/node

Implementation status: 0%

This is a cool feature, but unluckily I didn't have time to start it. Luckily, it can be done in a few hours ;)

# Add new radios/devices and save to a new CNML

Implementation status: 0%

Saving changes to local CNML is not possible, but instead it's possible to do the changes in the website using the API

# Guifi.net API / If Drupal API existed, user could log in with its guifi.net username and upload changes made locally to CNML

Implementation status: 70%

This is a huge work that I hadn't considered at all. Drupal API exists and Guifi.net Studio uses it.

At the moment it is possible to create nodes/zones/devices/radios but interfaces and links are not working properly due to some bugs in the server side API and because it's kind of unfinished. Updating nodes/zones/devices... is not possible at the moment but the user interface dialogs are ready (they will be the same that are used to create nodes/devices... but the fields are already filled, that's the only difference).

On the other hand, removing nodes/zones/devices/radios/interfaces/links is possible :D

# Ncurses and command line interface.

All the implemented actions can be done using the command line interface. There are some scripts in the tests directory.

No ncurses interface so far.

# I will help to move forward the CNML specification

I have worked on it and have some little proposals but it needs to be discussed deeply with more people interested in this aspect. I met some of the CONFINE crew and they seem to be the right people :D

# I will send patches to Guifi.net if necessary.

I have sent some patches to drupal-guifi and some others to libchamplain

# Gephi

I added this lately. [Gephi](http://gephi.org/) is a great software to deal with graphs and visualization.

I haven't had time to investigate it but it's on my TODO list. It would be very useful for people doing their thesis or other studies.

... and I must say that I'm happy with the result :-)
