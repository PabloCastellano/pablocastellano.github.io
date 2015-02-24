Title: Qué es libreBORME
Date: 2015-02-25 0:20
Category: LibreBORME
Tags: libreborme, opendata, registro mercantil, proyecto de fin de carrera, civio
Lang: es

LibreBORME es mi apuesta como Proyecto de Fin de Carrera y estará tutorizado por [Carlos Canal](http://www.lcc.uma.es/~canal/) de la Universidad de Málaga
y [David Cabo](https://twitter.com/dcabo) de la [Fundación Ciudadana Civio](http://www.civio.es/).

El progreso se puede ir viendo en el repositorio de GitHub: [libreborme](https://github.com/PabloCastellano/libreborme), aunque
ahora mismo el último commit es de octubre, de cuando ni siquiera me habían aprobado el anteproyecto. En los próximos días
subiré los últimos cambios para que reflejen el estado actual.

He presentado libreBORME a dos concursos de software libre: al [Concurso Universitario de Software Libre](http://www.concursosoftwarelibre.org/1415/)
y al [Certamen de Proyectos Libres](http://osl.ugr.es/2014/09/26/premios-a-proyectos-libres-de-la-ugr/) que celebra este año la Oficina de Software Libre
de la Universidad de Granada (UGR). ¡Espero tener una versión funcional y bonita para las fechas de entrega!

Y ahora sí, para saber de qué va, os dejo a continuación con el texto del anteproyecto que me fue aprobado el pasado mes de noviembre.

# Plataforma web para la consulta y el análisis del Boletín Oficial del Registro Mercantil

# Motivación

Durante los últimos años la transparencia es un tema en auge en el ámbito político-institucional. Sin embargo, el diablo está en los detalles y
muchas veces la palabra "transparencia" se usa de forma viciada por ser un tema que está de moda y suena bien, independientemente de si la institución
en cuestión es transparente o no. O quizás simplemente la definición de este término que manejan unas y otras partes es distinta.

Otro problema muy común es confundir "datos abiertos" con "transparencia", cuando la realidad es que lo primero puede usarse como una herramienta para
conseguir lo segundo, pero no necesariamente: publicar los horarios de autobuses como datos abiertos no mejora la transparencia (aunque tenga otros beneficios).[^1]

En el momento en el que se redacta este documento hace menos de un año que España ha aprobado su Ley de Transparencia[^2]. Hasta entonces era
el único país europeo con más de un millón de habitantes sin una.

La aprobación fue sin duda una noticia importante y esperada. Sin embargo, ya durante el periodo de debate empezaron a oírse voces desacordes con esta ley.

La *Open Knowledge Foundation*[^3], una de las organizaciones internacionales sin ánimo de lucro más importantes y referentes por su trayectoria en la
lucha por la transparencia, proporciona en su «*Manual de Datos Abiertos*» una definición, con una serie de condiciones que un conjunto de datos
(o en inglés, *dataset*) debe cumplir para poder ser considerado "Datos Abiertos".[^4][^5] La definición es extensa pero se puede resumir en:

- **Disponibilidad y acceso**. La información debe estar disponible como un todo y a un costo razonable de reproducción, preferiblemente descargándola
de Internet. Además, debe estar disponible en una forma conveniente y modificable.
- **Reutilización y redistribución**. Los datos deben ser proporcionados bajo términos que permitan reutilizarlos y redistribuirlos, e incluso
integrarlos con otros datos.
- **Participación universal**. Todos deben poder utilizar, reutilizar y redistribuir la información. No debe haber discriminación alguna en términos
de esfuerzo, personas o grupos. No están permitidas las restricciones "no comerciales" que prevendrían el uso comercial de los datos ni las
restricciones de uso para ciertos propósitos (por ejemplo sólo para educación).

En la actualidad no hay una apuesta seria por ello y son pocas las instituciones españolas que cumplen esta definición cuando hablan de datos abiertos.

Sin embargo, en los últimos años ha quedado demostrado que una de las fortalezas más claras de nuestro país es que a pesar del descontento generalizado
en la política institucional, en la sociedad civil surgen grupos que se organizan y especializan para trabajar de forma proactiva y cambiar las cosas.

En este caso, la sociedad civil lleva tiempo organizándose para exigir transparencia de verdad, poniendo como ejemplo la que existe en países de nuestro
entorno que se consideran referentes en cuestión de datos abiertos como Reino Unido, y está consiguiendo acelerar el proceso de la transparencia en las
instituciones haciendo el trabajo que ellas no hacen, creando conjuntos de datos abiertos de verdad.

Algunos ejemplos de estas organizaciones son *OpenKratio*[^6], *Fundación Ciudadana Civio*[^7], y *Qué Hacen Los Diputados*[^8] (la primera, con sede
en Sevilla y las dos últimas con sede en Madrid). A nivel internacional nos encontramos, entre otras, con *Sunlight Foundation*[^9], y *Open Knowledge
Foundation* (OKFN), ya citada anteriormente.

Su programa de actividades es público y en él encontramos reuniones con técnicos de gobiernos regionales para ofrecer asesoramiento y colaboración de
forma altruista; organización de conferencias sobre transparencia y datos abiertos en universidades con ponentes internacionales que explican la perspectiva
desde otros países; colaboración con administraciones públicas para liberar y visualizar datos; organización y participación en concursos y _hackatones_
para desarrollar nuevas APIs, aplicaciones de móvil, etc.

En este contexto se plantea el siguiente proyecto con el objetivo de abordar los datos públicos del Registro Mercantil de España para *abrirlos* de una
forma más cercana a la definición de la OKFN y ofrecerlos a cualquiera (sea persona o robot de Internet) que quiera hacer uso de ellos.

# El Boletin Oficial del Registro Mercantil (BORME)

El _Registro Mercantil Central_ (RMC) es el organismo encargado de la publicación del _BORME_, que por sus siglas responde al "Boletín Oficial del Registro Mercantil".  
El BORME es «el BOE de las empresas» y en él se publican las nuevas inscripciones, las bajas, y otra serie de actos que las sociedades están obligadas a comunicar.

Desde 2009 se publica en formato electrónico. Es un gran paso, pero el BORME contiene únicamente los cambios, es decir, que si leemos el BORME podemos
conocer que una sociedad se ha disuelto hoy, pero nos será muy difícil saber cuándo se constituyó, ya que la web no incorpora un buscador que nos
permita encontrarlo. Además, si la fecha de constitución fue anterior a 2009, sería aún más difícil, ya que no existe el documento en formato electrónico
y tendríamos que solicitar al RMC una fotocopia del documento en papel, indicándoles previamente el número de BORME, que también necesitaremos conocer.
Sin embargo esos datos están ya informatizados en algún sitio. Para acceder al historial de una empresa podemos acudir al servicio ofrecido del
_Colegio de Registradores de la Propiedad y Mercantiles de España_ (o simplemente _Colegio de Registradores_) y pagar en concepto de honorarios por él,
en función de las consultas que queramos realizar.

Este procedimiento no cumple la definición de datos abiertos de la OKFN y además es contradictorio y contraproducente por los siguientes motivos:

- No tiene sentido que sea un servicio cerrado, ya que la función primordial del Registro Mercantil es ser un instrumento de publicidad (hacer público)
de las empresas.[^10]
- El simple hecho de cobrar por él dificulta y contradice su propia función de publicidad.
- Es una forma de funcionamiento obsoleto que tendría que haber sido renovada hace más de una década. Entonces se precisaba pagar a una persona
encargada de buscar en miles de folios de cientos de tomos la información solicitada, pero hoy vivimos en la Sociedad de la Información, donde ya
existe Internet, donde esa información la tenemos en algún sitio ya informatizada y el coste de la consulta de estos datos tiene un coste real cercano a 0€.

Sin embargo, sí que sigue teniendo sentido que cobren por los servicios de expedición de certificados (otro de los servicios ofrecidos por el Colegio de Registradores) ya que en él precisan de un Registrador Mercantil que certifique los datos.

Desafortunadamente por otra parte,el buscador del BORME solo está activo para la sección II, que es en la que se publican "Anuncios y avisos legales",
cuando la realmente interesante es la sección I, donde se publican los actos de inscripción y otros actos relativos a las empresas. Por último, a
esto le sumamos que mientras que el BOE ya se publica en los formatos PDF y XML, el BORME se continua publicando únicamente en PDF (la sección II sí
que se publica en XML) y que antes de comenzar este proyecto el autor contactó con el webmaster del BORME, quien manifestó la voluntad de que esto no
iba a cambiar al menos a corto plazo _«por el convenio y legislación actual del Registro Mercantil»_.

# Objetivos y alcance del proyecto

El objetivo del presente PFC es crear una plataforma que de forma automatizada descargue los BORME desde el 2 de enero de 2009, que fue el día que se
comenzaron a publicar en formato electrónico, para procesarlos y generar una base de datos propia con los datos que estos contienen.

El procesado automático extraerá la información útil de los PDF, identificando entidades y acciones. Una vez se haya generado esta base de datos, el
potencial estará en la posibilidad de hacer consultas por campos o incluso semánticas.

Por ejemplo:  
¿Qué otras sociedades administran los administradores de esta otra empresa? ¿Cuántas empresas se crearon/destruyeron en 2011?

Para facilitar las consultas se desarrollará también una plataforma web alojada en la nube usando el framework Django con el lenguaje de programación Python.

La plataforma será compatible con OpenStack y Cloud Foundry, soluciones de computación de la nube IaaS y PaaS respectivamente. Se han escogido ambas
soluciones de entre todas las que coexisten actualmente por ser software libre y por las organizaciones que las respaldan como "estándar de la nube".

Otro objetivo es que el servicio siga online tras la finalización del proyecto. Para ello el autor contactó con la Fundación Ciudadana Civio, y ésta
mostró su conformidad en mantener y explotar el servicio de forma conjunta. El sistema será autónomo y quedará programado para buscar diariamente los
nuevos boletines publicados e incorporar esta información a la base de datos. De este modo las consultas se podrán realizar con la última información
disponible hasta el momento.

El código de la plataforma se publicará con una licencia de software libre, ya que la idea es que el proyecto se reutilice y se cree comunidad con él.

Por último se facilitarán a OpenCorporateslos datos recopilados. OpenCorporates es una iniciativa que pretende liberar datos de sociedades a nivel mundial
y "asignar una URL a cada empresa del mundo", ya que los datos sobre compañías y corporaciones españolas con los que cuenta actualmente son muy pobres
en comparación con los de otros países.[^11][^12][^13]

# Referencias

[^1]: The New Ambiguity of "Open Government", 2012: http://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2012489
[^2]: [http://www.20minutos.es/noticia/1991399/0/ley-de-transparencia/actitudes-politicas/congreso/](http://www.20minutos.es/noticia/1991399/0/ley-de-transparencia/actitudes-politicas/congreso/)
[^3]: [https://okfn.org/](https://okfn.org/)
[^4]: [http://opendatahandbook.org/en/what-is-open-data/](http://opendatahandbook.org/en/what-is-open-data/)
[^5]: Definición completa de "Abierto": [http://opendefinition.org/od/](http://opendefinition.org/od/)
[^6]: [http://openkratio.org/](http://openkratio.org/)
[^7]: [http://www.civio.es/](http://www.civio.es/)
[^8]: [http://quehacenlosdiputados.net/](http://quehacenlosdiputados.net/)
[^9]: [http://sunlightfoundation.com/](http://sunlightfoundation.com/)
[^10]: [http://www.mjusticia.gob.es/cs/Satellite/es/1215197983369/Estructura\_P/1215198328530/Detalle.html](http://www.mjusticia.gob.es/cs/Satellite/es/1215197983369/Estructura_P/1215198328530/Detalle.html)
[^11]: [http://registries.opencorporates.com/jurisdiction/es](http://registries.opencorporates.com/jurisdiction/es)
[^12]: Zara España SA: [https://opencorporates.com/companies/es/15022510](https://opencorporates.com/companies/es/15022510)
[^13]: Google Inc.: [https://opencorporates.com/companies/us\_ca/C2474131](https://opencorporates.com/companies/us_ca/C2474131)
