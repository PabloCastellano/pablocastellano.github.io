+++
date = '2010-08-20T00:00:00+02:00'
title = 'Estadísticas sobre los dispositivos más usados para nodos y supernodos en guifi.net'
categories = ['Guifi.net']
tags = ['estadísticas']
+++

Esta mañana he hecho un pequeño script Python que usando el [cnml de guifi world](http://guifi.net/es/guifi/cnml/3671) para sacar estadísticas y saber qué tipo de dipositivos/trastos son los más usados sin distinguir nodos de supernodos.

Este es el resultado:

1 Alix1
1 Prestige 650HW-31E
1 USR5410
1 USR8054
2 Avila GW2348-4
2 C54c
2 DWL-2100AP
2 USR5450
3 DWL-2000AP+
3 Prestige 650W
4 Supertrasto RB112 guifi.net
4 WAP54G
5 AirMaxM2 Rocket/Nano/Loco
6 Supertrasto guifiBUS guifi.net
8 Asus WL-500xx
10 Meraki/Fonera
11 Alix3
14 Bullet5
15 AirMaxM5 Bullet/PwBrg/AirGrd/NanoBr
15 Supertrasto RB153 guifi.net
16 WRT54GSv1-2
17 LiteStation5
19 Alix2
19 RouterStation
22 Supertrasto RB800 guifi.net
25 Supertrasto RB333 guifi.net
31 Bullet2
42 LiteStation2
45 WRT54GSv4
53 AirMaxM5 Rocket/Nano/Loco
87 Supertrasto RB133 guifi.net
141 Other
189 Supertrasto RB411 guifi.net
277 NanoStation Loco5
299 Supertrasto RB433 guifi.net
304 Supertrasto RB532 guifi.net
321 Supertrasto RB600 guifi.net
368 Supertrasto RB133C guifi.net
604 WRT54Gv1-4
657 NanoStation Loco2
1197 NanoStation5
1622 WHR-HP-G54, WHR-G54S
2516 WRT54GL
3902 NanoStation2

Se podría convertir en un conjunto de scripts y hacerlo mucho más jugoso extrayendo toda la información útil que proporcionan los archivos CNML y hacer gráficas. Así a bote pronto se me ocurre que se podría saber:

- Cuántos radios de media suelen tener los routers montados con una RB433.
- Tendencias: los modelos de supernodos que se montaban hace 2 años y los de ahora.
- Distancia media de los enlaces con una routerboard X y antena Z de Y dbi.
- ...

Vía | [guifi.net](http://guifi.net/es/node/32143)
