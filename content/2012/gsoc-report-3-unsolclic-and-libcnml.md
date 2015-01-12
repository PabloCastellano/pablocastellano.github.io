Title: GSOC Report #3: unsolclic and libcnml
Date: 2012-7-3
Category: TODO
Tags: guifi.net, gsoc2012

I'm back! No more exams for a while. I'm happy to have much more time to spend working on Guifi.net Studio.\
These are the improvements so far:

### Prettier GUI

Guifi.net Studio is prettier now, that's the first thing you can notice :)\
Now it has an user interface quite similar to [Emerillon](http://projects.gnome.org/emerillon/) which is very intuitive, well-though and
gives a good user experience.\
I basically copied their hide-able **sidebar** and included the search bar on the top:

[![](/pictures/guifinetstudio5.png)](http://lainconscienciadepablo.net/pictures/guifinetstudio5.png)

###  

### libcnml.py

The first prototype of a library to read, parse and query CNML files is ready. It's not finished and I'll rewrite to use classes for
entities (Zone, Node, Device...). At the moment the data structure is like a dictionary of dictionaries and it has its own limitations (lack
of pointers to: other nodes, parent zone, etc...).\
Here's an example of how to use it (notice again that the API will change after it's rewritten):

> from libcnml import CNMLParser\
> filename = 'test.cnml'\
> cnmlp = CNMLParser(filename)\
> \
> print cnmlp.nodes[99]['name'] \#name of node with id 99\
> print cnmlp.nodes[99]['lat'] \#latitude of node with id 99\
> print cnmlp.nodes[99]['lon'] \#longitude of node with id 99\
> print cnmlp.nodes[99]['devices'][77]['firmware'] \#firmware of device id 77 that belongs to node 99\
> \
> root = cnmlp.rootzone \# id of root zone of cnml file loaded\
> print cnmlp.zones[root]['title'] \# title of root zone\
> print cnmlp.zones[3996]['nlinks'] \# number of links between nodes in zone with id 3996\
> print cnmlp.zones[3996]['nservices'] \# number of services in zone with id 3996

###  

### Unsolclic

Unsolclic is almost usable. I should have finished it according to my schedule but having libcnml is a pre-requisite.\
I will finish it in the next days.\
There's a new User Interface to generate unsolclic configuration from the application (always off-line, remember it as is one of the top
features) ;-)

[![](/pictures/guifinetstudio3.png)](/pictures/guifinetstudio3.png)

[![](/pictures/guifinetstudio4.png)](/pictures/guifinetstudio4.png)\
 

### Meeting with my mentor

Roger and I met last week.\
One interesting things we talked about is a new use case:\
Let's say that somebody wants to deploy Guifi.net in a zone and he won't have access to the Internets during the work.\
He can download the CNML file of the zone before moving. What we decided to include a new feature so that he can create new nodes, edit its
properties and get also unsolclic **still off-line**.\
When he arrives home, he synchronizes the new nodes with the Guifi.net website.\
The problem to face is that during the deployment there could be someone that does changes in the same zone and there could be collisions of
data (ex. IP address auto-generated off-line that is already used in Guifi.net).\
Although this is quite unlikely to happen, in this case Guifi.net Studio would show a message box warning the user about this problem and
given him two solutions: getting the newest configurations or discard the changes. Ideally the installer would choose getting the newest
configurations and would re-run unsolclic in the nodes affected by the incoherence of data.

### Libchamplain

I [introduced myself](https://mail.gnome.org/archives/libchamplain-list/2012-June/msg00003.html) in their mailing list. I have also read
more than 50% of their archive.\
I reported the bug about [resizing points in a
*ChamplainMarkerLayer*](https://mail.gnome.org/archives/libchamplain-list/2012-June/msg00004.html) and it's already [fixed in the master
branch](http://git.gnome.org/browse/libchamplain/commit/?id=8c769a60905b7655ac5087ca0f63f6b6d8a4779e) :-D

### This week

I will start working on extending the CNML specification to support Optic Fiber links.\
I have another meeting with people from the Guifi.net Fundation.\
Midterm evaluation is next week.

[](http://lainconscienciadepablo.net/content/gsoc-report-3-unsolclic-and-libcnml)

[![Flattr
this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/732582/GSOC-Report-3-unsolclic-and-libcnml)
