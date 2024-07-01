from scapy.all import ARP, sr1, Ether
import os
import time
#********************************Obtener automaticamente la dirección IP******************************
def get_router_ip():
    
    result = os.popen("ip route | grep default").read().strip()
    if result:
        router_ip = result.split()[2]
        print(f"IP del router detectada automáticamente: {router_ip}")
        return router_ip
    else:
        print("No se pudo detectar la IP del router automáticamente.")
        return input("Ingrese manualmente la IP del router: ")
    

#****************************Solicitud ARP para obtener dirección MAC*************************
def get_router_mac(ip):
    
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = sr1(arp_request_broadcast, timeout=2, verbose=False)
    if answered_list:
        return answered_list.hwsrc
    return None

def get_current_router_mac(ip):
    arp_request = ARP(pdst=ip)
    arp_response = sr1(arp_request, timeout=2, verbose=False)
    if arp_response:
        return arp_response.hwsrc
    return None
#*******************************Detección del ataque ARP spoofing*********************
def check_arp_spoofing():
    current_router_mac = get_current_router_mac(router_ip)
    if current_router_mac is None:
        print(f"No se pudo encontrar la IP del router {router_ip} en la tabla ARP.")
    elif current_router_mac.lower() != original_router_mac.lower():
        print("SE HA DETECTADO UN POSIBLE ATAQUE DE ARP")
        print(f"MAC actual del router: {current_router_mac}")
        print(f"MAC original del router: {original_router_mac}")
    else:
        print("No ha sufrido algún cambio la tabla ARP")

if __name__ == "__main__":
    router_ip = get_router_ip()
    original_router_mac = get_router_mac(router_ip)
    
    if original_router_mac is None:
        print(f"No se pudo detectar la MAC del router {router_ip}.")
    else:
        print(f"MAC del router detectada automáticamente: {original_router_mac}")
        while True:
            check_arp_spoofing()
            time.sleep(8) 
