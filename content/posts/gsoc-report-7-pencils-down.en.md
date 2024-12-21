+++
date = '2012-08-19T00:00:00+02:00'
title = 'GSOC Report #7: Pencils down!'
categories = ['Google Summer of Code']
series = ['Google Summer of Code']
tags = ['guifi.net', 'GSoC2012']
+++

This week has been the suggested 'Pencils down period'.

I haven't done big changes but I have taken advantage of this time to test Guifi.net Studio deeply to detect and fix crashes and complete some easy features.

But there have been big changes, especially those done two weeks ago.

The most important thing is that Guifi.net Studio is now usable :D. The User Experience is definitely better. One example is that now there's no need to manually download CNML files to visualize its content. Instead, you can use the CNML Download dialog which will download it for you to the specific folder.

You have a new option in the File menu bar called 'Change zone' which will automatically detect which zones you have downloaded and allows you to change between them quickly.

I must admit that I'm really proud of the final result :D

Here is a summary of all the changes done during these two weeks:

# GtkGuifinetMap

I refactored a bit more the code. Now it was the turn for the Guifi.net map. I have put together everything related to the map in a new class called GtkGuifinetMap. This way, you can embed a GtkGuifinetMap in any GTK application and it will manage everything related to a 'Guifi.net Map'.

In the future you will be able to set its internals up and change thing like nodes color.

# Guifi.net API

I have worked on it a little bit. The most valuable part is that there are more tests now. I did some minor changes and now it's less verbose (e.g. it won't print your password in the terminal when you login ;))

# LibCNML

LibCNML supports now [DTD](https://en.wikipedia.org/wiki/Document_Type_Definition) validation :)

[I wrote a DTD](https://gitorious.org/guifi-altres/guifinetstudio/blobs/master/tests/cnml.dtd) for it and libCNML will use this file to validate CNML files against it. LibCNML will also print errors, if found.

Thanks to this method I found two bugs in the Guifi.net World detailed CNML:

The first one is that the node with id 1647 ([Vic Jaume I](http://test.guifi.net/node/1647)) doesn't contain the attribute called 'created' which should be mandatory.

The second one is that one of the links in the device with id 29880 ([VicVITST1](http://test.guifi.net/es/guifi/device/29880)) doesn't contain the attribute 'id'.

Both things are curious and weird at the same time... inconsistency in the database maybe?

# User Interface

- Nodes are now colorful depending on their status (working, planned, building...) :D
- Added Wireless link calculator. I liked [this one](http://guifi.net/files/guificalculator.html) and I have implemented the same in Guifi.net Studio.
- Dialog to download zones is now working and finally it turned to be useful :)
- New dialog to change zones between downloaded ones
- Edit interface and edit link dialogs work but the server side of the API doesn't :( So it's unfinished.

Other cool features are:

- **View in website** - When you right-click a node in the Nodes view, a menu pops up and this option will open the node in the Guifi.net website
- **View in map** - In the same popup menu, this option will take you to the selected node in the Map view
- **Export to KML** - KML is the format used by Google (although it was designed by a different company that was then acquired by Google). You can export CNML to KML and open it in Google's Earth for example.
- **Node filtering** - The side panel in the Map view allows you to filter nodes as simple as typing
- **Full screen** - You can run Guifi.net Studio in full screen.

# Configuration manager

- Added support for GNOME Keyring. Now your secrets are safe! :)
- Fixed invalid name for section "default". Now it's called "general"

# Others

- I fixed a lot of crashes when there are no cnml files available.
- Removed unused stuff: files and imports

# Internationalization

The last but one of the most important things at this point is that I made the strings translatable and [you can help](https://lists.guifi.net/pipermail/guifi-gtra/2012-August/000073.html) now to translate Guifi.net Studio into your language!

I have created a new project in the transifex.com translation platform: [Transifex](https://www.transifex.com/projects/p/guifinetstudio/)

Some people have already joined the project to help translating and the Galician translation is the first one that looks finished (99%). Kudos to the translators! :-D

# What's next

The coding period is over! :O I have started to write a final report to explain what I have done during this period, what still needs to be done, what will be done, what won't be done...

Some tasks that I want to finish in the next days:

- Translate Guifi.net Studio at least into 5 languages in August
- Create an user manual
- Improve documentation
- Spreading Guifi.net Studio
  - Create packages for the most typical GNU/Linux distributions and get them included in the main repositories.
  - Prepare a talk for the new SAX (Guifi.net community annual event) which will take place at
    [Tortosa](https://en.wikipedia.org/wiki/Tortosa) (Tarragona) during 28-29 September. [More info here](https://lists.guifi.net/pipermail/guifi-usuaris/2012-August/018762.html).
