Title: Scripts starcraft
Date: 2007-11-8
Category: TODO
Tags: Linux, Starcraft

Dejo aquí un par de scripts, útiles si juegas a Starcraft desde linux.

Con este primero te puedes desconectar de la partida sin que te cuente como partida perdida.  

    #!/bin/sh
    #Disconnect! scdisc.sh
    #by pablog (25-Mayo-2007)
    iptables -A INPUT -p tcp --dport 6112 -j DROP
    iptables -A OUTPUT -p > tcp --dport 6112 -j DROP
    iptables -A INPUT -p udp --dport 6112 -j DROP
    iptables -A OUTPUT -p udp --dport 6112 -j DROP
    echo "Press any key when time is out"
    read A
    iptables -F

Y con este segundo puedes ser muy molesto...

    #!/bin/sh
    #Lag! sclagger.sh
    #by pablog (10-Mayo-2007)
    # Juega con los parametros A y B.
    #####
    A=2
    B=1
    echo "Press Ctrl+C to cancel attack"
    while :
    do {
    iptables -A INPUT -p tcp --dport 6112 -j DROP
    iptables -A OUTPUT -p tcp --dport 6112 -j DROP
    iptables -A > INPUT -p udp --dport 6112 -j DROP
    iptables -A OUTPUT -p udp --dport 6112 -j DROP
    sleep $A
    iptables -F
    sleep $B
    }
    done

Algunas combinaciones son:

A=2, B=1: prácticamente injugable. La pantalla de lag parpadea y no muestra tu nick.  
A=2, B=4: jugable pero como cuando hay un listo con el P2P puesto.

Como es lógico, no me responsabilizo de los malos usos ;-)  
Fair Play!
