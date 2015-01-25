Title: GSOC Report #4: libcnml ready
Date: 2012-7-9
Category: GSoC2012
Tags: guifi.net, gsoc2012

Not so many changes but important advances:

-   Libcnml is rewritten and uses classes. Now you can do things like managing a *CNMLLink* object and get the two *CNMLNode* objects
    linked:

> *from libcnml import *  
> c = CNMLParser('tests/detail.3')  
> node = c.getNode(888)  
> print node  
> <libcnml.CNMLNode instance at 0xb75082ac\>  
> dir(node)  
> ['\_\_doc\_\_', '\_\_init\_\_', '\_\_module\_\_', 'addDevice', 'devices', 'getDevices', 'id', 'latitude', 'longitude', 'parse', 'status',
> 'title', 'totalLinks']  
> link = c.getLink(8787)  
> print link  
> <libcnml.CNMLLink instance at 0x8c296cc\>  
> link.getLinkedNodes()  
> [<libcnml.CNMLNode instance at 0x8c29a6c\>, <libcnml.CNMLNode instance at 0x8c294ac\>]

-   Thanks to the new libcnml, unsolclic for AirOSv3 is now working! Other templates are not working, they still need some adaptation.
-   I [fixed a bug](https://gitorious.org/guifi/drupal-guifi/commit/07134ed5f303afa4a69257db64bf222d64dd863f) in the CNML generation in the
    Guifi.net website.  
    It was the typical bug that nobody had ever realized before because there has never been a real use of CNML :-)
-   I had another meeting with Ramón and Roger. We talked about the Optic Fiber specification. This is something that needs to be very well
    though and cannot be finished spending many hours consecutive. So I will continue working in other things and keeping in mind how to
    improve it. Luckily at the end of the summer there will be something good.
-   GUI has now zoom in and zoom out buttons, hehe

[![Flattr
this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/735158/GSOC-Report-4-libcnml-ready)
