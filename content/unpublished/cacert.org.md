Title: CAcert.org (unpublished)
Date: 2010-2-13
Category: TODO
$SERVER["socket"] == "192.168.1.102:8070" {     server.document-root =  "/var/www/blog"     ssl.engine      =       "enable"    
ssl.pemfile     =       "/etc/lighttpd/ssl/blog_server.pem" #    ssl.ca-file            =       "/etc/lighttpd/ssl/cacert.crt" }
$HTTP["host"] =~ "\^blog\.lainconscienciadepablo\.net:8069$" {     $HTTP["scheme"] == "http" {         url.redirect = ( "\^/(.\*)" =\>
"https://blog.lainconscienciadepablo.net:8070/$1" )     } } http://svn.cacert.org/CAcert/Software/CSRGenerator/csr
http://www.cacert.org/index.php?id=3 class1 vs class3 fosdemX cat blog_privatekey.pem blog_server.pem \>blog1.pem
