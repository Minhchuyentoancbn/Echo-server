import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create a socket object, using it without calling s.close()
# AF_INET is the Internet address family for IPv4
# SOCKET_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.bind((HOST, PORT))  # Associate the socket with a specific network interface and port number
    s.listen()  # Enables server to accept connections
    conn, addr = s.accept() # Block execution and wait for an incoming connecton
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # Read whatever data the client send
            if not data:
                break
            conn.sendall(data)  # Echo back