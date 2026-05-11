import socket

# Create raw socket
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

host = socket.gethostbyname(socket.gethostname())
print(f"Listening on {host}")

sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("Capturing packets... Press Ctrl+C to stop.\n")

while True:
    raw_data, addr = sniffer.recvfrom(65535)
    print(f"Packet captured from: {addr}")