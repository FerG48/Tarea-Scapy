# Tarea-Scapy
Se compone de lo siguiente:
(1) El archivo AtacARP.py contiene la creación de ARP spoofing para atacar a otra máquina.
(2) El archivo DeteccionARP.py identifica si se ha infringido y modificado su tabla ARP.
Para su uso:
La máquina atacante es la de Kali Linux, la máquina atacada es la de Ubuntu
(1) Para el archivo AtacARP.py se ejecuta como super usuario en la máquina atacante y se solicitará que se ingresen la ip de destino y la ip de router y se imprimirá un mensaje indicando que se está iniciando el ARP spoofing.  	
(2) Para el archivo de DeteccionARP.py tambien se jecuta como super usuario en la máquina atacada y comenzará detectando automaticamente la IP y la MAC del router, después verificará periodicamente si ha detectado algún ataque o si la tabla arp del router ha cambiado.
