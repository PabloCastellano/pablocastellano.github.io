+++
date = '2010-06-02T00:20:00+02:00'
title = 'Debugging flash in firefox'
categories = ['Development']
tags = ['linux', 'flash', 'debugging', 'firefox']
+++

Install [Adobe Flash Player Debugging Version](http://www.adobe.com/support/flashplayer/downloads.html) (first I recommend you to uninstall any flash version you have installed):

```bash
wget http://download.macromedia.com/pub/flashplayer/updaters/10/flash_player_10_linux_dev.tar.gz  
tar zxvf flash_player_10_linux_dev.tar.gz  
cd flash_player_10_linux_dev/plugin/debugger  
tar zxvf install_flash_player_10_linux.tar.gz  
cd install_flash_player_10_linux/  
./flashplayer-installer  
# Follow instructions.
```

Install the [Firebug](https://addons.mozilla.org/firefox/addon/1843/) and [Flashbug](https://addons.mozilla.org/firefox/addon/14465/) extensions.

I couldn't install extensions... it seems an Ubuntu 10.04 well-known issue. Workaround here: [disabling ipv6 dns in firefox.](http://ubuntuforums.org/showthread.php?t=1476706) Restart firefox.

Now in the Firebug panel, enable "Flash Console". Enter a page with flash and you will start to see the debug information :)

What is it useful to?

I know that there are extensions like FlashGot to do it, but I wanted to download the video embedded in a flash player that you can watch here: [Erasmus Paradiso (Repor)](http://www.rtve.es/television/20090227/erasmus-paradiso-repor/239192.shtml).

And in fact, the url pointing to the flv file was there! ;-)

[![](/img/debug_flash.png)](/img/debug_flash.png)

IDEAS:  

This mechanism saves a lot of time that you could have spent dissambling the flash player.

One of my ideas is creating a plugin to be able to watch in Totem last news as shown in RTVE (spanish radio television). Being able [search videos](http://www.rtve.es/buscador/GoogleServlet?q=sinde&modo=1&pagina=1) in their [archives](http://www.rtve.es/#mediateca-feat) or e.g. sorting last [news](http://www.rtve.es/noticias/telediario-en-4/) videos by [category](http://www.rtve.es/television/eurovision/). To sum up, the same that the current youtube plugin does in Totem.

**Updated June 2nd 2010:**

[I've found in a blog](http://gargadon.teufansub.net/2010/03/baja-videos-de-tve-a-la-carta-con-rtmpdump/) how to download RTVE videos using [RTMDump](http://rtmpdump.mplayerhq.hu/). 

Actually [it seems](https://bugzilla.gnome.org/show_bug.cgi?id=566604) that there're some people working to get rtmp support in GStreamer, that would be the optimum solution :)
