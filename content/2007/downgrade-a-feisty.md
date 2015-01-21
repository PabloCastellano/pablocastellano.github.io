Title: Downgrade a feisty
Date: 2007-8-7
Category: TODO
Tags: Linux

Te levantas un día con *versionitis*, decides actualizar a gutsy. Media hora bajando paquetes y otra media instalándolos... y ahora firefox
[peta](https://bugs.launchpad.net/ubuntu/+source/hunspell/+bug/111940). Puedes esperarte hasta que lo arreglen, arreglarlo tú mismo [...], o
volverte a feisty. ¿Que cómo?:

1. Reemplaza en tu /etc/apt/sources.list todos los *gutsy* por *feisty*
2. Crea /etc/apt/preferences con el siguiente contenido:

> Package: \*  
> Pin: release a=feisty  
> Pin-Priority: 1001  
> Package: \*  
> Pin: release a=gutsy  
> Pin-Priority: 50  

3. *apt-get update && apt-get dist-upgrade*

No todo estaba perdido... :þ
