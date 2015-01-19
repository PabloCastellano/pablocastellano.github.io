Title: Primer parche [entrada no acabada]
Date: 2008-11-12
Category: TODO
Tags: TODO, linux, español

Realmente no es el primer, pero lo considero 100% mío :-). **default mmap_min_addr breaks dosemu**
https://bugs.launchpad.net/ubuntu/+source/dosemu/+bug/216398 En este parche me tuve que enfrentar a varios desconocidos. Hablaremos de
debian/{install,rules}, patchs y diffs entre otros. Bajar el código fuente e instalar sus build-dep's. apt-get source dosemu Problema 2: La
misión del parche es tan simple como crear el archivo /etc/sysctl.d/90-dosemu.conf con una línea. Ahora bien, el paquete tiene una
estructura, y lo primero que dices es ¿dónde meto el archivo 90-dosemu.conf y en qué parte le digo que lo mueva a /etc/sysctl.d ? En cuanto
a dónde meterlo, yo elegí etc/ porque iba a ir a /etc [mal] Y luego elegí src/arch/linux/Makefile.main, un archivo con las reglas necesarias
para crear el paquete (y donde falla el unpatch!), añadiendo simplemente dos líneas con el comando 'install'. Tampoco fue el correcto. [mal]
Solución 2: Mi intuición me falló y al final había que meterlo en debian/. En cuanto a decirle que lo mueva a un sitio exacto, esto se hace
utilizando debian/install y al final es mucho más sencillo. Simplemente conteniendo:

    "debian/90-dosemu.conf etc/sysctl.d/"

ya apt se encarga de moverlo adonde dice cuando se instala el paquete. Problema 2,5: Al hacer debuild, crea el paquete sin problema pero al
hacer 'debuild clean' aunque no muestra error aparente, hay algo que no hace bien: unpatch. Es decir, no invierte los parches aplicados a la
hora de construir el paquete. Y esto luego es un problema, porque al siguiente 'debuild' se nos queja diciendo que los parches "parece" que
ya estan aplicados. Solucón 2,5: Estuve un buen rato intentando arreglar la fase de unpatch pero no lo conseguí. En la fase de patch se
crean en debian/ unos archivos que empiezan por "stamp=" y que significan que se han aplicado así como otros archivos acabados en
"-level.y.log" que no son más que la salida al aplicar patch -py \< . Bien, pues cuando llega la fase de unpatch ¡ya se han borrado esos
archivos! de manera que el script cree que esos parches nunca fueron aplicados y por lo tanto no se invierten. Esto lo muestra en pantalla
"\*not applied\*". Intuyo que el problema está en debian/rules. Así que ninguna solución por el momento. [TOREPORT&FIX] Problema 3:
Readaptando parches. Si intentamos construir (debuild) nos daremos cuenta de que ahora no se construye, sino que da un error aplicando
"debian/patches/01_debianize.diff". Es normal ya que hemos modificado src/arch/linux/Makefile.main Ya que Solución 3: Si ejecutamos
what-patch en el directorio donde hemos descomprimido nos dice que dosemu usa el gestor de parches 'cdbs'. Me ha gustado bastante su forma
de uso, es bastante facilita. Simplemente cdbs-edit-patch debian/patches/01_debianize.diff para editar ese parche. Esto copia en /tmp el
directorio descomprimido de dosemu y aplica todos los parches (incluido el que vas a modificar!!) ahí ya modificas lo que tú quieras y
cuando termines pulsas Ctrl+D. Ahora el parche que también contendrá tu último cambio. Al final mi parche y el que se aplicó se parecían en
poco, pero sirve de lección (más en el sentido de estudio que de amonestación). Aquí están los dos en cuestión: [El
mío.](http://launchpadlibrarian.net/19551464/02_mmap_min_addr.patch) [El que adaptó
Kees.](http://launchpadlibrarian.net/19553189/dosemu_1.4.0%2Bsvn.1828-2ubuntu1_1.4.0%2Bsvn.1828-2ubuntu2.diff.gz) Problema 4: purge Problema
5: cdbs-edit-patch Problema 6: Como problema 6 está que ahora la versión estable es Intrepid. El parche fue aplicado a Jaunty apenas a la
hora después de yo publicarlo =). Si consideramos que el parche es necesario para Intrepid también, debemos de proponerlo y tiene que ser
aprobado. Como esto no lo he hecho aún porque no me lo he encontrado nunca, lo dejo para otra entrada posterior. pablog.
