Title: Debugging flash in firefox
Date: 2010-6-2
Category: TODO
Tags: TODO, linux, flash, debugging

Install [Adobe Flash Player Debugging Version](http://www.adobe.com/support/flashplayer/downloads.html):\
(first I recommend you to uninstall any flash version you have installed)

> wget http://download.macromedia.com/pub/flashplayer/updaters/10/flash\_player\_10\_linux\_dev.tar.gz\
> tar zxvf flash\_player\_10\_linux\_dev.tar.gz\
> cd flash\_player\_10\_linux\_dev/plugin/debugger\
> tar zxvf install\_flash\_player\_10\_linux.tar.gz\
> cd install\_flash\_player\_10\_linux/\
> ./flashplayer-installer\
> Follow instructions.

Install the [Firebug](https://addons.mozilla.org/firefox/addon/1843/) and [Flashbug](https://addons.mozilla.org/firefox/addon/14465/)
extensions.

I couldn't install extensions... it seems an Ubuntu 10.04 well-known issue. Workaround here: [disabling ipv6 dns in
firefox.](http://ubuntuforums.org/showthread.php?t=1476706) Restart firefox.

Now in the Firebug panel, enable "Flash Console".\
Enter a page with flash and you will start to see the debug information :)

What is it useful to?\
I know that there are extensions like FlashGot to do it, but I wanted to download the video embedded in a flash player that you can watch
here: [Erasmus Paradiso (Repor)](http://www.rtve.es/television/20090227/erasmus-paradiso-repor/239192.shtml).

And in fact, the url pointing to the flv file was there! ;-)

[![](/pictures/debug_flash.png)](/pictures/debug_flash.png)

IDEAS:\
This mechanism saves a lot of time that you could have spent dissambling the flash player.

One of my ideas is creating a plugin to be able to watch in Totem last news as shown in RTVE (spanish radio television). Being able [search
videos](http://www.rtve.es/buscador/GoogleServlet?q=sinde&modo=1&pagina=1) in their [archives](http://www.rtve.es/#mediateca-feat) or e.g.
sorting last [news](http://www.rtve.es/noticias/telediario-en-4/) videos by [category](http://www.rtve.es/television/eurovision/). To sum
up, the same that the current youtube plugin does in Totem.

**Updated 2/Jun/2010:**\
[I've found in a blog](http://gargadon.teufansub.net/2010/03/baja-videos-de-tve-a-la-carta-con-rtmpdump/) how to download RTVE videos using
[RTMDump](http://rtmpdump.mplayerhq.hu/).\
Actually [it seems](https://bugzilla.gnome.org/show_bug.cgi?id=566604) that there're some people working to get rtmp support in GStreamer,
that would be the optimum solution :)
