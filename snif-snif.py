from scapy.all import sniff, IP, TCP, UDP
import logging

# Configure logging to output to a file
logging.basicConfig(filename='detailed_packet_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        if proto == 6:  # TCP
            proto_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif proto == 17:  # UDP
            proto_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            proto_name = "OTHER"
            src_port = "N/A"
            dst_port = "N/A"

        packet_info = f"IP: {ip_src} -> {ip_dst} | Protocol: {proto_name} | Src Port: {src_port} | Dst Port: {dst_port}"
        print(packet_info)
        logging.info(packet_info)

# Sniff packets on a specific interface (replace "eth0" with your network interface)
sniff(prn=packet_callback, iface="eth0", store=0)
