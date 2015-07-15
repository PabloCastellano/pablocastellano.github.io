Title: LibreBORME tercer premio en el I Certamen de Proyectos Libres de la UGR
Date: 2015-07-15 14:31
Category: LibreBORME
Tags: libreborme, concurso

<a href="/img/libreborme/trofeo_oslugr.gif"><img src="/img/libreborme/thumbnails/200x_/trofeo_oslugr.gif"/></a>

El jurado del [I Certamen de Proyectos Libres de la UGR 2014-2015](http://osl.ugr.es/2014/09/26/premios-a-proyectos-libres-de-la-ugr/) decidió otorgar al proyecto LibreBORME el [tercer premio](http://osl.ugr.es/2015/06/17/ganadores-del-certamen-de-proyectos-libres-de-la-ugr-2014-2015/) y la semana semana aproveché un hueco para ir a recoger mi trofeo a la ETSII de la Universidad de Granada :-D

Este premio ha sido toda una sorpresa para mí y me anima a seguir dándole caña al proyecto en verano, cuando las fuerzas flaquean.

Si tenéis curiosidad, podéis echarle un ojo a los otros proyectos ganadores:

- 1er premio: [Evenge](http://evenge.github.io/) \[[Repositorio](https://github.com/evenge/EVENGE)\]
- 2º premio: [Don't Crush My Castle](http://demiurgosoft.github.io/dont-crush-my-castle/) \[[Repositorio](https://github.com/demiurgosoft/dont-crush-my-castle)\]

Aprovecho para dar las gracias a los organizadores, al jurado, a los patrocinadores y a todos los que han hecho posible esta primera edición del certamen. La organización ha sido excelente. ¡Hasta han [publicado](https://twitter.com/OSLUGR/status/610496501329096704) la [Memoria de Evaluación](https://drive.google.com/file/d/0B8DW9UWKXYAocjMtRWtpQ2x1eUE/view) donde detallan cómo han evaluado los 24 proyectos que hemos participado!  
Simplemente genial. Esto **SÍ** es transparencia y tener voluntad por hacer bien las cosas.

Ni punto de comparación con mis andanzas por el Concurso de aplicaciones Android de la UMA del que [ya escribí por aquí](/blog/2015/01/tongo-en-el-concurso-android-de-la-uma/) en otra ocasión. No puedo evitar acordarme de ellos. Publicar la memoria de evaluación debería ser obligatorio en todo concurso.

<a href="/img/libreborme/evaluacion_libreborme_oslugr.png"><img src="/img/libreborme/thumbnails/750x_/evaluacion_libreborme_oslugr.png" /></a>

# Últimos avances de LibreBORME

De paso aprovecho también esta entrada para comentar mis últimos avances en LibreBORME:

- He escrito desde cero una nueva librería de Python llamada [bormeparser](https://github.com/PabloCastellano/bormeparser), que a partir de ahora es la que se encarga de todo lo relacionado con obtener información de los BORMEs y agrupa todas las funciones necesarias (como generar URL de descarga de un día, descargar el PDF, parsearlo...). Además, la nueva versión del parser es mucho más precisa.
- He eliminado de LibreBORME el código para extraer información de los BORMEs y ahora uso bormeparser en su lugar.
- Sistema de tests e integración continua de bormeparser usando [Travis CI](https://travis-ci.org/PabloCastellano/bormeparser/).
- Documentación en readthedocs: tanto para [bormeparser](http://bormeparser.readthedocs.org/) como para [libreborme](http://libreborme.readthedocs.org/).
- Creación de un *Playbook* para Ansible para desplegar LibreBORME de forma automática: repositorio [libreborme-ansible](https://github.com/PabloCastellano/libreborme-ansible) y [documentación](http://libreborme.readthedocs.org/es/latest/install_production_automated/).

Tenía pensado presentar el proyecto en septiembre y estoy un poco agobiado porque veo que aún faltan muchas cosas por hacer. Veremos qué tengo para entonces... ¡Buen verano!
