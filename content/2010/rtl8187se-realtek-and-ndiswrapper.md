Title: rtl8187se, realtek and ndiswrapper
Date: 2010-4-12
Category: TODO
Tags: realtek, linux

My new netbook uses the
[rtl8187se](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=drivers/staging/rtl8187se;hb=HEAD) wireless driver and
this is another post complaining about Realtek support to linux users.

It would be a nice piece of news that it works out-of-the-box if the driver wasn't so unstable in WPA protected networks. I suffer
from *drops in throughput* every 5-10 minutes, sometimes even less, that make the connection unusable.  
In [this](https://bugs.launchpad.net/bugs/246141) ubuntu bugreport there are also users that claims that they have the same issue (2 years
ago). Unfortunately, I lost all my hopes with Realtek in things related to fixing drivers. My experience *[(in this
post)](/2010/04/email-to-realtek-about-issues-in-their.html)* is that I wrote them 5 months ago about the sound driver issue in my HP
Pavilion Tx2000 and they haven't even replied a *"Thanks for the report. We will have a look at this issue"*. It's also worth to mention the
shoddy piece of work that they did with the rt3070 driver [*(see this other post)*](/2010/01/rt3070.html). At the moment, I'm using
ndiswrapper with the winXP drivers. It works like a charm and I recommend it to everyone having this issue. You can download the Windows
drivers [here](http://www.realtek.com/downloads/downloadsView.aspx?Langid=1&PNid=21&PFid=40&Level=5&Conn=4&ProdID=172&DownTypeID=3&GetDown=false&Downloads=true).
[Direct link](ftp://WebUser:Ds8MtJ3@202.134.71.22/cn/wlan/8187SE_WindowsDriver_5_6.9109.1029.2009.zip).

I also discovered that there's a pyGTK GUI for ndiswrapper very suitable for your granma who wants to connect to her WPA wireless at home,
but she can't do it out-of-the-box because Realtek didn't care about providing a decent driver. It's called
[ndisgtk](http://packages.ubuntu.com/lucid/ndisgtk) and looks like this:

[![](/img/pantallazo-controladoresderedesinalc3a1mbricas1.png)](/img/pantallazo-controladoresderedesinalc3a1mbricas1.png)
