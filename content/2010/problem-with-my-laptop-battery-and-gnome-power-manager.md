Title: Problem with my laptop battery and gnome-power-manager
Date: 2010-6-22
Category: Free software
Tags: linux, gnome, laptop, battery, gnome-power-manager

My laptop battery is faulty, when I connect my laptop to the AC adapter, the battery starts to get charged but after some minutes (random)
the battery LED light becomes orange and that means that, even if the computer is being supplied by the AC adapter, the battery is not
getting recharged.  
 The solution is unplug and plug again the AC adapter.

But I had also a very annoying issue.  
 When I was disconnecting the AC adapter, the battery value read wasn't correct and gnome-power-manager detected immediately that the
battery was critical, showing me the next message and my laptop got suspended without any choice. But in the meantime, I could see that the
applet said something that the battery still had charge to remain 30 minutes. O_o!? And it was truth.

[![](/img/pantallazo.png)](/img/pantallazo.png)

Today, touching gconf I have discovered that there is a workaround and it is disabling the gconf key
/apps/gnome-power-manager/general/use_time_for_policy which by default is enabled. It makes gnome-power-manager (since now g-p-m) to have
really into account the battery percentage instead of the time that SHOULD remain, according to your previous battery statistics.  
 Run gconf-editor:

[![](/img/pantallazo-editordeconfiguracic3b3n-general.png)](/img/pantallazo-editordeconfiguracic3b3n-general.png)

You can tune up a bit more this behaviour with the keys located in */apps/gnome-power-manager/thresholds/*.

[![](/img/pantallazo-editordeconfiguracic3b3n-thresholds.png)](/img/pantallazo-editordeconfiguracic3b3n-thresholds.png)

The screenshots are in Spanish but there's not to much to understand.  
In any case, you can do the same with the command line tool running:

> gconftool-2 -s /apps/gnome-network-manager/general/use_time_for_policy --type bool False

Note that G-P-M has [migrated from GConf to GSettings](http://live.gnome.org/GnomeGoals/GSettingsMigration) recently. I'm not used to
gsettings but there should be similar editors.

**UPDATE 2011-11-25:**

For gsettings use:

> gsettings set org.gnome.settings-daemon.plugins.power use-time-for-policy false
