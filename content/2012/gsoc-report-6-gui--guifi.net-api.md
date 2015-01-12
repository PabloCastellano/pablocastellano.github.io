Title: GSOC Report #6: GUI + Guifi.net API
Date: 2012-8-6
Category: TODO
Tags: guifi.net, gsoc2012

Another report for the last 2 weeks.\
\
The most of the work has been the **Graphic User Interface**.\
So far it's possible to create nodes, zones, devices and radios in the remote host (test.guifi.net in this case) from the application.\
You will also have the chance to create it locally, that is, modifying your own CNML file and keeping the changes without pushing them to
the server but this is not working at the moment.\
The dialogs to create new entities will inform you about the success or failure of the operation with message dialogs. I think they are
quite intuitive\
I have beautified the dialogs a lot. Some examples here:

[![](/pictures/pantallazos/guifinetstudio/dialog_createdevice.png)](/pictures/pantallazos/guifinetstudio/dialog_createdevice.png)[![](/pictures/pantallazos/guifinetstudio/dialog_createdevice2.png)](/pictures/pantallazos/guifinetstudio/dialog_createdevice2.png)

[![](/pictures/pantallazos/guifinetstudio/dialog_createnode.png)](/pictures/pantallazos/guifinetstudio/dialog_createnode.png)[![](/pictures/pantallazos/guifinetstudio/dialog_createnode2.png)](/pictures/pantallazos/guifinetstudio/dialog_createnode2.png)

[![](/pictures/pantallazos/guifinetstudio/dialog_createzone.png)](/pictures/pantallazos/guifinetstudio/dialog_createzone.png)[![](/pictures/pantallazos/guifinetstudio/dialog_createzone2.png)](/pictures/pantallazos/guifinetstudio/dialog_createzone2.png)

I'm trying a new widget that allows the enduser picking up a zone from all of them without having to use the huge combobox.\
It's a GtkEntry widget that uses autocompletion and so, you get suggestions as you type. You can see it in the "create zone" dialog.

Configuration Manager
---------------------

Now there's a cache directory where CNML files are saved.\
My initial idea is that you can download the CNML file for the zone/node you want through a dialog window. Then you can change between those
that you have downloaded previously and so, you can visualize different zones without having to load the whole Guifi.net World.\
It's almost working although I'm not sure if it will be really useful... we will see :D

[![](/pictures/pantallazos/guifinetstudio/dialog_cnml.png)](/pictures/pantallazos/guifinetstudio/dialog_cnml.png)

Preferences
-----------

The Preferences dialog works now and the changes you make get saved to the config file when you close the dialog window.\
I have also added new settings to be saved like zone\_type, token and token\_date, Guifi.net host...\
Now you can also define which is your **default zone** and the application will autoload it when it's launched.

Guifi.net API
-------------

I have added more methods to the API and more examples-snippets: getFirmwares.py, getModels.py, getChannels.py, getProtocols.py,
addRadio.py, removeRadio.py, addDevice.py, removeDevice.py.

They are easy to read and understand and so, the Guifi.net community could start now creating useful scripts to maintain their nodes/zones
:)

Code structure
--------------

The code of Guifi·net Studio was becoming [Spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) and I did a lot of refactoring.\
For example I separated the main .ui file with all the glade interfaces into different files (each one is one dialog) and now there's a
class for each dialog.

I have not pushed these last changes because I don't know how the heck can I configure git to push the changes through a SOCKS proxy
server.\
I have read different solutions but none of those worked to me :-(. I hope to be able to push them this evening.

[](http://lainconscienciadepablo.net/content/gsoc-report-6-gui-guifinet-api)

[![Flattr
this](http://api.flattr.com/button/flattr-badge-large.png "Flattr this")](http://flattr.com/thing/814187/GSOC-Report-6-GUI-Guifi-net-API)
