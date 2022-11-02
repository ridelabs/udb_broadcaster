from udp.networking import UDPBroadcaster


def boring_send_main():
    broadcaster = UDPBroadcaster()
    broadcaster.send_message("Hello folks!")
    print("I just sent a message!")


if __name__ == '__main__':
    boring_send_main()

