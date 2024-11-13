+++
date = '2012-07-23T00:00:00+02:00'
title = 'GSOC Report #5: pyGuifiAPI'
categories = ['Google Summer of Code']
series = ['Google Summer of Code']
tags = ['guifi.net', 'GSoC2012']
+++

Big changes during these 2 weeks :)

# Python Guifi.net API

I wrote a new library called [**pyGuifiApi**](http://gitorious.org/guifi-altres/guifinetstudio/blobs/master/lib/pyGuifiAPI/api.py). As you can guess by its name, it's used to communicate with the [API](http://es.wiki.guifi.net/wiki/API#API) in the side of the web server.

I have included some tests that show how to create, update and remove nodes from the command line. These are available in the [lib/pyGuifiAPi/tests directory](http://gitorious.org/guifi-altres/guifinetstudio/trees/master/lib/pyGuifiAPI/tests).

# Graphic User Interface

New dialog windows for editing preferences, nodes, zones, devices, radios, interfaces and links:

[![](/img/pantallazos/guifinetstudio/dialog_createdevice.png)](/img/pantallazos/guifinetstudio/dialog_createdevice.png) 
![](/img/pantallazos/guifinetstudio/dialog_createnode.png)

[![](/img/pantallazos/guifinetstudio/dialog_createradio.png)](/img/pantallazos/guifinetstudio/dialog_createradio.png) 
[![](/img/pantallazos/guifinetstudio/dialog_createzone.png)](/img/pantallazos/guifinetstudio/dialog_createzone.png)

[![](/img/pantallazos/guifinetstudio/dialog_createlink.png)](/img/pantallazos/guifinetstudio/dialog_createlink.png)[ 
![](/img/pantallazos/guifinetstudio/dialog_createinterface.png)](/img/pantallazos/guifinetstudio/dialog_createinterface.png)

[![](/img/pantallazos/guifinetstudio/dialog_preferences.png)](/img/pantallazos/guifinetstudio/dialog_preferences.png)

I still have to connect them to pyGuifiAPI. Some dialogs are really ugly as the one for creating nodes. After that I discovered that using *GtkGrid* instead of *GtkBox* the result is nicer. Anyways, suggestions (and patches) are welcome :P

![Dialog preferences](/img/pantallazos/guifinetstudio/dialog_preferences.png)

# Config Manager

Configuration (e.g. Guifi.net username and password) is now stored in a file. Now it's only plain text but I plan to support also other systems like the gnome-keyring to store them encrypted :)

Conventionally the configuration files will be stored at `~/.config/guifinetstudio/`

# Libcnml

I have added support for **[lxml](http://lxml.de/)** in libcnml. It's totally transparent (lxml will be used if it's available). This library is much faster and does a better memory management than the minidom library that is shipped by default with Python 2.7. If you want to manage big sets of nodes like Guifi.net World zone this definitely makes the difference.

For example, these are the results opening a Guifi.net World zone with more than 17.000 nodes:

* Minidom took ~23 seconds and 1,4GB RAM. Guifinetstudio window didn't even appear. I had to reboot my laptop.
* Lxml took ~4s and 284MB RAM. Guifinetstudio worked, moving through the map is difficult but possible.

You can test it by your own:

```python
# cnml1.py
from libcnml import *
c = CNMLParser('tests/detail')
```

```
$ time python cnml1.py
Using lxml which is more efficient
Loaded OK

real    0m3.974s
user    0m3.728s
sys     0m0.188s
```


```
$ time python cnml1.py
lxml module not found. Falling back to minidom
Loaded OK

real    0m22.984s
user    0m21.997s
sys     0m0.868s
```

# Unsolclic

I have adapted all the templates to jinja2 and now I can load them without errors. It doesn't mean that unsolclic works. There's still some work to do to have it. If you want more information about these changes, see [this commit](http://gitorious.org/guifi-altres/guifinetstudio/commit/fbc22b3b085dc6301d3d9d46fa76e87d1cbd6e2a) description.

# This week

* I will continue working with the API and the Optic Fiber specification.
* This evening I will participate in a videoconference with people involved in the European [CONFINE](http://es.wiki.guifi.net/wiki/CONFINE) project. We will talk about CNML :)
