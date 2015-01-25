Title: Educación informática I (verificando certificados digitales)
Date: 2010-9-10
Category: Informática
Tags: seguridad, certificados digitales, muface

Ayer, dando vueltas por la página de [muface](http://muface.es), veo que puedes [hacer
solicitudes](http://www.mpr.es/muface/oficina_virtual/solicitudes_por_internet/solicitudes_por_internet-ides-idweb.html) por Internet, bien
sea con certificado digital o sin él.  
 Aceptan los certificados digitales: DNIe, FNMT, Camerfirma, ACCV, CatCert e IZENPE.

Pero centrémonos en las solicitudes sin certificado digital.  
Podemos pulsar en [ENTRAR](https://oval.muface.es/mut_sc/) directamente o [descargar un
PDF](www.mpr.es/muface/oficina_virtual/common/ReqTecAccesoSC_EXT.pdf) con los requisitos técnicos. Me entra curiosidad y me descargo el PDF.

Básicamente te cuenta que lo normal es que te salga una excepción de seguridad por no tener el certificado raíz de Camerfirma instalado en
tu navegador. Te muestra capturas de pantalla de Firefox hasta el punto en que haces click en el botón de "Obtener certificado" y luego cito
textualmente:

> *Pulse "Ver..." para ver el certificado y, luego, confirme que quiere añadir la excepción de seguridad (pulsando Confirmar excepción de
> seguridad) para que le deje acceder a este servicio de Muface.*

¿¿Cómoooorll?? ¿Y para qué se cree el que ha hecho este tutorial que sirven los certificados?

# El problema

El paso importante de añadir una excepción de seguridad es comprobar que el certificado es el original y que no ha sido falsificado con un
[ataque MITM](http://es.wikipedia.org/wiki/Ataque_Man-in-the-middle). Además te dice "pulse ver para ver el certificado y luego confirme..."
¡y se queda tan ancho! ¿Para qué quiere ver un usuario corriente el certificado?

Los certificados digitales tienen una firma digital y una "huella digital" (del inglés fingerprint).  
 Esta huella digital nos sirve para decidir si un certificado es verdadero o falso. Si al menos hubieran incluído una captura de pantalla de
la ventana donde se ve la información del certificado podríamos validar la huella, pero tal como está, el usuario va a aceptar el
certificado sea el que sea. **ESTO ES MUY GRAVE**, ya que no nos aseguramos de asegurar la página web y por lo tanto de que la conexión
directamente con muface sea segura y esté cifrada, sino que podría haber algún "intermediario".

De las secciones Linux y Macintosh mejor ni hablamos porque están vacías. Al menos se han dignado a nombrarlas.

Para lo que valga, esta es la captura de pantalla perdida y tal como se puede ver, los fingerprints (los míos... porque no hay manera de
asegurar que sean los reales, así que no te fíes) son:  

> SHA1: C9:8D:FC:49:15:BA:FB:53:C7:12:74:0E:81:EB:06:50:9D:7B:4C:7B  
> MD5: DE:7A:37:C9:97:36:78:BC:3B:1D:45:AD:25:34:A3:8D

![firefox certificado muface](/img/Screenshot-Certificate%20Viewer:"oval.muface.es".png)   

¿Sería muy descabellado pedir que este tipo de cosas las enseñaran en las asignaturas de informática de bachillerato? ¿Es más importante
aprender a manejar una suite informática que entender esto?  
La sociedad española actual no está preparada para esto y ni la misma unidad informática de Muface te ayuda.  
Y la tecnología, si no se saber usar, es inútil y puede ser peligrosa.
