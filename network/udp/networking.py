import socket

BROADCAST_PORT = 9999
MAX_PACKET_SIZE = 1024


class UDPBroadcaster:
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.conn.settimeout(0.2)

    def send_message(self, message):
        self.conn.sendto(bytes(message, 'utf-8'), ('<broadcast>', BROADCAST_PORT))


class UDPListener:
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.conn.bind(("", BROADCAST_PORT))

    def pick_up_message(self):
        data, addr = self.conn.recvfrom(MAX_PACKET_SIZE)

        return data, addr