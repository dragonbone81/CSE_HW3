import socket


def tcp_socket_send(ip, port):
    data = ''
    tcp_message = "GET / HTTP/1.1\r\nhost: www.example.com\r\n\r\n"
    tcp_sessions = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sessions.settimeout(2)
    tcp_sessions.connect((ip, port))
    tcp_sessions.send(tcp_message.encode())
    while True:
        try:
            data += tcp_sessions.recv(4096).decode()
        except socket.timeout:
            break

    tcp_sessions.close()
    return data


if __name__ == "__main__":
    print(tcp_socket_send('www.andes.ucmerced.edu', 80))
