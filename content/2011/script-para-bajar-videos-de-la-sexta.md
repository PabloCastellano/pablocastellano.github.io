Title: Script para bajar vídeos de La Sexta
Date: 2011-11-1
Category: Development
Tags: la sexta, script

Por motivos de **compatibilidad operativa**, he tenido que buscar otro método para descargar los vídeos de la web de [La
Sexta](http://www.lasexta.com/). Para ello he hecho un script en Python que dada una URL te devuelve la dirección del RTMP para bajarla con
rtmpdump por ejemplo.

Resumiendo... la URL original está codificada únicamente con el algoritmo [RC4](https://secure.wikimedia.org/wikipedia/es/wiki/RC4) en el
enlace al reproductor Flash mediante el parámetro *_urlVideo*:

[![](/img/lasexta_urlvideo.gif)](/img/lasexta_urlvideo.gif)

Como RC4 es un cifrado simétrico, si tenemos la clave (**<strike>sd4sdfkvm234</strike>**) lo tenemos todo. Durante el desarrollo he descubierto que
usan la librería [as3crypto](http://code.google.com/p/as3crypto/), que a su vez tiene una [demo muy
chula](http://crypto.hurlant.com/demo/) de sus posibilidades :)

El script también te devuelve la cadena descifrada si se la pasas como parámetro.

> $ ./lasexta_video_downloader.py
> http://www.lasexta.com/sextatv/veranodirecto/macrobotellon_en_madrid_mientras_el_papa_duerme/260233/6563  
> LaSexta video downloader  
> Copyright (C) 2011 Pablo Castellano  
> This program comes with ABSOLUTELY NO WARRANTY.  
> This is free software, and you are welcome to redistribute it under certain conditions.
>
> rtmp://vod.lasexta.com/vod/_definst_/veranodirecto/sd/XPD0002901003001_VERANO_DIRECTO___EP_30_19_08_2011_18_14_52_flash.flv?start=198.96&end=632.218
>
> Use rtmpdump to download:  
> rtmpdump -o download.flv -r
> "rtmp://vod.lasexta.com/vod/_definst_/veranodirecto/sd/XPD0002901003001_VERANO_DIRECTO___EP_30_19_08_2011_18_14_52_flash.flv?start=198.96&end=632.218"

Un ejemplo con la cadena cifrada:

> $ python lasexta_video_downloader.py
> 7077f50772d8144c167bb20ea37c7899d9950d2f935d7cf288a5112b7cbf31a7e43e09deb5798a0fb1c18475d12ab29efc1a27284575a51b0abcf4377cbeebf20e03ae12a89d4ffa44bbafbc797093d0ebb190457b98f1c54e1f8018255addab3c59f1d35b371166f403e652d2c96724d38018d08e125a706db0c7081d91bf63b670971e1c2c1fef2e60ec7957df5a5b585f7e58
>
> LaSexta video downloader
>
> Copyright (C) 2011 Pablo Castellano
>
> This program comes with ABSOLUTELY NO WARRANTY.
>
> This is free software, and you are welcome to redistribute it under certain conditions.
>
>  
>
> rtmp://vod.lasexta.com/vod/_definst_/veranodirecto/sd/XPD0002901003001_VERANO_DIRECTO___EP_30_19_08_2011_18_14_52_flash.flv?start=198.96&end=632.218
>
>  
>
> Use rtmpdump to download:
>
> rtmpdump -o download.flv -r
> "rtmp://vod.lasexta.com/vod/_definst_/veranodirecto/sd/XPD0002901003001_VERANO_DIRECTO___EP_30_19_08_2011_18_14_52_flash.flv?start=198.96&end=632.218"
>
>  

El ejercicio de ingeniería inversa queda indicado como ejercicio para el lector.  
Algunas utilidades para ello:

-   Desensamblador AS3:  
    RABCDAsm: [https://github.com/CyberShadow/RABCDAsm](https://github.com/CyberShadow/RABCDAsm)  
    Hay otro llamado Nemo 440 pero no parece que sea libre. [http://www.docsultant.com/nemo440/](http://www.docsultant.com/nemo440/)

-   Instrucciones AVM2:  
    [http://learn.adobe.com/wiki/display/AVM2/callpropvoid](http://learn.adobe.com/wiki/display/AVM2/callpropvoid)  
    [http://learn.adobe.com/wiki/display/AVM2/findpropstrict](http://learn.adobe.com/wiki/display/AVM2/findpropstrict)  
    [http://learn.adobe.com/wiki/display/AVM2/getlex](http://learn.adobe.com/wiki/display/AVM2/getlex)  
    [http://learn.adobe.com/wiki/display/AVM2/callproperty](http://learn.adobe.com/wiki/display/AVM2/callproperty)

## Cosas pendientes y bugs

1.  Descargar el fragmento de vídeo que corresponde al vídeo que ves en la web.  
    Algunos vídeos son fragmentos de otro vídeo más largo. En la misma URL decodificada se puede apreciar el segundo en el que empieza y el
    segundo en que acaba dentro de ese vídeo más largo (la URL tiene los parámetros *start* y *end*). Rtmpdump acepta los parámetros -A y -B
    para indicarle estos datos y obtener solo esa parte. Con las pruebas que he hecho no me ha convencido del todo el resultado pero tampoco
    he investigado mucho más, así que de momento bajas el vídeo entero.
2.  Listas de reproducción  
    Hay otros otras URLs de La Sexta (como
    [esta](http://www.lasexta.com/sextatv/salvados/completos/salvados__domingo__25_de_septiembre/501473/1) por ejemplo), en las que el
    parámetro cambia a *_url_list* y tienes varias versiones del mismo vídeo para descargar, como la versión en HD. En la próxima versión
    lo arreglo.
3.  ¿Aumentar tiempo de espera?  
    <strike>Me ha pasado varias veces que bajando el archivo se corta. He aumentado el timeout añadiéndole los parámetros **-m 300**. Haré más
    pruebas y si veo que así no falla definitivamente, incluyo los parámetros en el comando que te facilita el script.</strike> **FIXED!**

El código, en mi repositorio de GitHub:  
[https://raw.github.com/PabloCastellano/pablog-scripts/master/lasexta_video_downloader.py](https://raw.github.com/PabloCastellano/pablog-scripts/master/lasexta_video_downloader.py)

Espero que os sea de utilidad. ¡Saludos!
