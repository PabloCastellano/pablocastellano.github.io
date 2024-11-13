+++
date = '2010-08-06T00:20:00+02:00'
title = 'TP-LINK TL-WN722N (o cualquier ath9k_htc) en Ubuntu 10.04'
categories = ['Linux']
tags = ['ubuntu', 'howto']
+++

![](/img/tlwn722g200x150.jpg)

El adaptador wifi usb [TP-LINK TL-WN722N](http://www.tp-link.com/products/productDetails.asp?pmodel=TL-WN722N) usa un chipset llamado AR9271 y requiere un nuevo controlador de Atheros llamado [ath9k_htc](http://linuxwireless.org/en/users/Drivers/ath9k_htc). Dicho controlador ha sido incluído en la reciente versión del kernel 2.6.35. Si tenemos un adaptador que trabaje con este módulo podemos hacer que funcione en Ubuntu con los siguientes pasos.

1. Descarga un kernel 2.6.35
   1. En el caso de Ubuntu, aún no está en el repositorio oficial. Puedes usar el repositorio kernel-ppa o descargarlo directamente desde
      [aquí](http://ppa.launchpad.net/kernel-ppa/ppa/ubuntu/pool/main/l/linux-maverick/linux-image-2.6.35-14-generic_2.6.35-14.19%7Elucid1_i386.deb)
      ([aquí](http://ppa.launchpad.net/kernel-ppa/ppa/ubuntu/pool/main/l/linux-maverick/linux-image-2.6.35-14-generic_2.6.35-14.19%7Elucid1_amd64.deb)
      para amd64)
   2. Otra opción es bajártelo desde kernel.org y compilarlo tú mismo...
2. Instálalo (doble click en el archivo .deb o `sudo dpkg -i nombre`)
3. Descarga el firmware de tu adaptador (`ar9271.fw` [aquí](http://git.kernel.org/?p=linux/kernel/git/dwmw2/linux-firmware.git;a=blob_plain;f=ar9271.fw;hb=HEAD))
4. Copia el archivo `ar9271.fw` a `/lib/firmware/`
5. Reinicia con el nuevo kernel

Para otras distribuciones, ajustar simplemente los pasos 1 y 2 con sus respectivos métodos para descargar e instalar el kernel 2.6.35.

**Actualización 14 de agosto de 2010:**

Me ha sucedido de repente que el rendimiento ha bajado drásticamente. Al principio he pensado que era porque el bitrate estaba a 1M pero no es cierto. Resulta que del manejo del bitrate se encarga el firmware y no hay ninguna manera de obtener el bitrate actual del dispositivo así que está fijado a 1M y cuando intentas cambiarlo:

```bash
iwconfig wlan0 rate 54M
```

te dice que la operación no está soportada. Reiniciando se ha solucionado.

Al parecer [hay gente](http://sourceforge.net/apps/mediawiki/ndiswrapper/index.php?title=TP-Link_TL-WN722N) que ha conseguido hacerlo funcionar con ndiswrapper pero no he encontrado ningún driver que fuera fino y todos petaban.
