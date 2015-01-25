Title: Universal Subtitles
Date: 2010-10-11
Category: Free software
Tags: projects, guifi.net

[![universal subtitles globe](/img/universal_subtitles_globe.jpg)](/pics/universal_subtitles_globe.jpg)

Hoy, buscando sobre *"editores de subtítulos colaborativos"* (algo así como un programa para poder traducir un vídeo entre mucha gente a la
vez conectada a Internet desde distintas partes del mundo y todo de manera colaborativa) he conocido el proyecto Universal Subtitles.

# ¿Qué es Universal Subtitles? (traducción libre de su FAQ)

La meta de Universal Subtitles es facilitar a todo el mundo la tarea de añadir subtítulos y traducir cualquier vídeo en la web. Estamos
construyendo herramientas colaborativas y esperamos atraer a un gran número de contribuidores para ayudar en la tarea del subtitulado. El
software que estamos haciendo es libre y de código abierto y puede ser usado y mejorado por cualquiera.

El proyecto cuenta con el apoyo tanto de la organización sin ánimo de lucro "Participatory Culture Foundation" como de "Mozilla Drumbeat".
PCF es, entre otras cosas, fundador de la coalición "Open Video Alliance". Drumbeat me ha gustado cómo se autodefine: 

> "Drumbeat es un movimiento para mantener la web abierta durante los próximos 100 años"

En definitiva, suena bien eso de imaginar que todos los vídeos disponibles en Internet estén subtitulados en tu idioma, ¿no? Sin duda es uno
de los gran avances del html5 y su etiqueta de vídeo. :)

La herramienta que han desarrollado se encuentra en versión alpha pero he hecho una prueba y es totalmente usable y no me ha dado ningún
fallo. Mejor que algunas betas :P

# ¿Cómo funciona?

Bueno, pues primero elegimos un video para traducir. Para hacer una prueba yo he elegido uno de youtube muy corto (unos 10 segundos y con 3
frases).

Una vez elegido el vídeo vamos a [http://universalsubtitles.org/videos/create/](http://universalsubtitles.org/videos/create/) y le decimos
dónde se encuentra el vídeo y pulsamos empezar. Por el momento acepta vídeos en ogg, webm, flv y de los sitios youtube, blip y vimeo. ¡No
está nada mal!

Veremos un minitutorial con los tres pasos.

-   Transcribir el vídeo.
-   Sincronizar las frases.
-   Revisar como quedan los subtítulos y darles un último retoque.

Todo de forma facilísima y super intuitiva.

Una vez hecha esa parte el resto es aún más fácil. Los traductores se encargan de traducir las frases al idioma deseado.

Luego, nos da un código javascript con el que podemos incluir en nuestro blog por ejemplo el vídeo con una pestaña debajo para seleccionar
el idioma de los subtítulos. El código es algo así:

    <script type="text/javascript" src="http://s3.www.universalsubtitles.org/embed.js"> 
    (
      {'video_url': 'http://webmademovies.etherworks.ca/guillermo.ogv'}
    )
    </script>

Y se ve así (necesitas un navegador que soporte html5):

<script type="text/javascript" src="http://s3.www.universalsubtitles.org/embed.js"> 
(
  {'video_url': 'http://webmademovies.etherworks.ca/guillermo.ogv'}
)
</script>

Ahora pensemos que:
-   Youtube tiene en fase de pruebas un sistema para transcribir vídeos en inglés de forma automágica.
-   Youtube además, te permite traducir al vuelo la transcripción de un vídeo en inglés.
-   Disponemos de herramientas de traducción automáticas (más o menos buenas...)
-   Disponemos además, de sistemas de sintetización de voz.
-   Hemos visto los primeros grandes avances en temas realidad aumentada.

No me parece muy descabellado decir que en 5 años o menos podríamos tener sistemas que tradujeran automáticamente vídeos a muchos idiomas. O
tener unas gafas futuristas para ver los subtítulos de alguien que te habla a la vez que por los auriculares lo escuchas traducido a tu
idioma... uy, me estoy flipando ya demasiado.

Recomiendo usar la web de desarrollo [http://dev.universalsubtitles.org/](http://dev.universalsubtitles.org/), ya que incorpora las últimas
mejoras y fallos corregidos.

Lo del editor de subtítulos colaborativo queda pendiente... ¿o alguien conoce alguno que ya exista?

# Enlaces relacionados
- [http://universalsubtitles.org/about](http://universalsubtitles.org/about)  
- [http://dev.universalsubtitles.org/faq](http://dev.universalsubtitles.org/faq)
- [https://www.drumbeat.org/project/universal-subtitles](https://www.drumbeat.org/project/universal-subtitles) (de donde he tomado prestada la primera imagen)
