Title: freedesktop & XDG
Date: 2010-1-24
Category: Free software
Tags: linux, nouveau, portland

freedesktop.org (abreviado como "fd.o") apareció en el año 2000, aunque también es conocido como XDG ("X Desktop Group"). Es un proyecto que
surgió cuando se empezó a "popularizar" el utilizar linux para los ordenadores personales, y con el objetivo de hacer unos estándares para
los escritorios que funcionan sobre las X, ya que para entonces no existía ninguno y cada escritorio con su grupo de desarrolladores hacía
las cosas de la forma que le parecía más adecuada o simplemente que le parecía. Actualmente participan en fd.o entre otros, miembros de KDE,
GNOME y Xfce, que podríamos decir que son los escritorios más populares a día de hoy.

En su [repositorio git](http://cgit.freedesktop.org/)
se puede ver todo el [software](http://freedesktop.org/wiki/Software) que aloja. Algunos proyectos un poco desconocidos pero otros bastante
populares y usados como:

-   avahi
-   cairo
-   dbus
-   gstreamer
-   HAL
-   PackageKit
-   ...

Entre ellos se encuentran también [Portland](http://portland.freedesktop.org/wiki/) y [Nouveau](http://nouveau.freedesktop.org/).

El primero, Portland, se encarga de crear una serie de utilidades (scripts) para hacer una serie de tareas, independientemente de si estás
usando en ese momento KDE o GNOME. Todos son comandos que empiezan por "xdg-" y los hay para interactuar con el salvapantallas, abrir
archivos con la aplicación por defecto, instalar archivos .desktop...  
He sabido de este proyecto por [este bug](http://bugs.freedesktop.org/show_bug.cgi?id=15828), que me estaba volviendo loco con xdg-mime.
Creo que me lo apunto también a la lista de proyectos a seguir y colaborar (me gusta la *"estandarización"*). Entre ayer por la tarde y
hoy por la mañana he puesto un poco de orden en el bugzilla!

Su última *release* fue en 2007, pero hablando con Fabo (uno de los desarrolladores) me ha dicho que planean hacer otra cuanto antes,
y a continuación migrar a Git, ya que es de los pocos proyectos que quedan en fd.o aún usando CVS.

El segundo es un driver open source para las tarjetas nVidia y con aceleración 3D. Tengo la suerte de
conocer mi coetáneo *Francisco Jerez (curro)*, quien participó en el [Google Summer of Code 2009](http://code.google.com/soc) y es ahora
unos de sus desarrolladores de Nouveau. Su función, tal como se explica
[aquí](http://socghop.appspot.com/gsoc/student_project/show/google/gsoc2009/xorg/t124025016929) era implementar la función de salida
de TV previa ingeniería inversa:

---
<table>
<tbody>
<tr>
<td>Title:  </td>
<td>Reverse engineering of Nvidia TV encoders.    </td>
</tr>
<tr>
<td>Abstract:  </td>
<td>The TV output present on several Nvidia graphics cards lacks support from the nv and nouveau open source device drivers. This forces most users wanting to use their TV out to stick with the proprietary Nvidia software.
<p>This project will aim to reverse engineer the operation of the TV encoder integrated on some recent Nvidia chips, and provide a RandR1.3 compliant implementation based on the nouveau driver. </p></td>
</tr>
</tbody>
</table>
---

La gente sin conocimientos técnicos puede colaborar [probando el driver (tester)](http://nouveau.freedesktop.org/wiki/TestersWanted) o
[donando tarjetas gráficas nvidia](http://nouveau.freedesktop.org/wiki/HardwareDonations). [Estado
actual](http://nouveau.freedesktop.org/wiki/FeatureMatrix) de Nouveau. Como curiosidades:

1.  *Curro* terminó la tarea en las primeras semanas y siguió con otras labores... :)
2.  Para asegurarse la plaza se dedicó a buscar tarjetas nVidia con distintos chipsets. También antiguas, no importaba pues la intención es
    que el driver funcione en todas y sustituya al oficial y privativo de nVidia. Un día quedamos para que probara los últimos avances con
    la gráfica de mi portátil.
3.  El proyecto sólo tiene un asalariado por parte de Red Hat, [Ben Skeggs](http://skeggsb.livejournal.com/), mientras que nVidia paga
    perfectamente a cientos de desarrolladores para el driver privativo.
4.  Para modificar su wiki en lugar de captchas hay preguntas sobre tarjetas gráficas al estilo trivial :D
5.  Tras no pocas discusiones, Nouveau vendrá incluido en el kernel 2.6.33.

## Enlaces relacionados

- [Portland points desktop Linux at $10 billion market.](http://desktoplinux.com/news/NS7435528984.html)
- [freedesktop.org interview in 2003.](http://www.osnews.com/story/5215/The_Big_freedesktop_org_Interview)
