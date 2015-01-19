Title: Email to Realtek about issues in their sound driver
Date: 2010-4-12
Category: TODO
Tags: realtek, linux

This is the email I sent to Realtek related email addresses on 3/December/2009. I sent it to: kailang@realtek.com.tw, shou@realtek.com.tw,
and from their Contact section in their webpage. I hope that posting it here in public, they feel a bit more ashamed. I haven't received a
minimal answer 5 months later. I wonder how important are users for them once that they have bought their product. Do they care a minimum?

> Hello, my name is Pablo and I own a tablet PC "HP TX2000es" (spanish version of HP TX2000). My cause of my email is that the current linux
> driver for the realtek model of sound card I own isn't optimum. And I think it would be the same for the others, not only in the spanish
> model. Currently I'm using Ubuntu 9.10 which runs 2.6.31-15-generic and today I have downloaded 2.6.32 to see the changes but it seems
> that there were not improves on it. The troubles I have found so far are: - By default, when you connect your headphones the sound
> continues being played through the speakers. I solved it by loading snd-hda-intel with the parameter model=hp. But instead, when I load
> snd-hda-intel like that, the microphone stops working (is not detected, none of both). So the current scenario is to choose between using
> microphone or hearing the speakers with headsets. I have also tried with other model parameters like model=6stack-digout or model=3stack
> but it's like by default (speakers continue playing). According to lspci, my device is: 00:10.1 Audio device: nVidia Corporation MCP51
> High Definition Audio (rev a2) 00:10.1 0403: 10de:026c (rev a2)     Subsystem: 103c:30e5     Control: I/O- Mem+ BusMaster+ SpecCycle-
> MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-     Status: Cap+ 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=fast \>TAbort- SERR-
>     Latency: 0 (500ns min, 1250ns max)     Interrupt: pin B routed to IRQ 17     Region 0: Memory at 80020000 (32-bit, non-prefetchable)
> [size=16K]    Capabilities:     Kernel driver in use: HDA Intel     Kernel modules: snd-hda-intel I have seen there is a macro
> SND_PCI_QUIRK in /usr/src/linux-source-2.6.31/sound/pci/hda/patch_realtek.c that is used with specific models of this laptop:
> patch_realtek.c:12526:    SND_PCI_QUIRK_MASK(0x103c, 0xff00, 0x3000, "HP TX25xx series", ALC268_TOSHIBA), patch_realtek.c:15171:   
> SND_PCI_QUIRK(0x103c, 0x30bf, "HP TX1000", ALC861VD_HP), But there's no QUIRK for 103c:30e5 (my model) I hope I explained well myself
> and you could understand my problem (well, the problem of all owners of this model) and you can now help us to solve it. I have no
> experience with the kernel. Please contact me if you need to test new patches or you need more information. Thanks in advance. Regards,
>     Pablo. 
