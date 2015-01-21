Title: Vista de mensajes en Evolution
Date: 2010-7-22
Category: TODO
Tags: gnome, evolution

Desde que me pasé a leer el correo con Evolution echaba de menos una cosa de Thunderbird que me parecía un bug en Evolution. Y por lo visto
[no era](http://www.mail-archive.com/evolution-list@gnome.org/msg05439.html) [el único](http://osdir.com/ml/evolution-list/2009-07/msg00011.html).

Cuando ordenaba los correos de una lista de correo por threads, me salían
mal ordenados. Evolution me los ordenaba usando la fecha del primer mensaje enviado en ese hilo en vez del último mensaje. De esta manera,
la gente en los hilos continuaba escribiendo pero como también había recibido más mensajes, la barra de desplazamiento se había movido y al
final me perdía entre los mensajes intentando ver si habían contestado a los hilos de hace 3 días.

No es un bug, es que simplemente lo había configurado mal.

En Evolution puedes definir varias formas de ver y ordenar los correos. En el menú **View**->**Current View** hay unas cuantas
predefinidas, y luego también puedes hacerte las tuyas personalizadas.

Los cambios que he hecho han sido:

1. Cambiar la posición de la columna Subject por la columna From.
2. Pinchar en Date hasta que sale la flechita hacia abajo para que queden ordenados (esto es lo que me faltaba, **¡EL BOTÓN TIENE 3 ESTADOS!**).
3. Con Ctrl+T los agrupas en threads (hilos). Para que sea la predeterminada he borrado la carpeta *~/.evolution/mail/views* y ahora te vas 
   a **View**->**Current View**->**Save Custom View** y reemplazas "**Messages**" que es la que abre por defecto.
