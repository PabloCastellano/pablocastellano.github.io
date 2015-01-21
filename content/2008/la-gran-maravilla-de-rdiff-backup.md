Title: La gran maravilla de rdiff-backup
Date: 2008-11-5
Category: TODO
Tags: Linux

Nadie hace copias de seguridad de sus datos hasta que pasa lo que pasa.

Un conocido me habló de backupninja (desarrollado por los chicos
italianos de [autistici.org](http://autistici.org)), me lo instalé e hice un par de backups de prueba (son incrementales :)). El plan era
hacer backup de mi home e instalar la nueva Ubuntu 8.10 Intrepid, modificando también el tamaño de las particiones / y /home.

Dejo aquí un par de comandos de ejemplo que me han sigo útiles.  
Recuperan la carpeta con la configuración para pidgin:

Ver cuántos cambios han habido:

> rdiff-backup --list-increment-sizes .purple  
> Time                       Size        Cumulative size  
> -----------------------------------------------------------------------------  
> Tue Nov  4 01:00:03 2008         36.3 KB           36.3 KB  (current mirror)  
> Mon Nov  3 01:00:04 2008         0 bytes           36.3 KB  
> Sat Nov  1 17:32:46 2008          752 KB            788 KB  
> Fri Oct 31 19:19:57 2008         2.00 KB            790 KB

Elegir el archivo de incremento deseado y restaurarlo:

> rdiff-backup .purple.2008-10-31T19:19:57+01:00.dir ~/.purple

Finito!
