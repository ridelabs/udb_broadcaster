from udp.networking import UDPListener, UDPBroadcaster


def listener_main():
    listener = UDPListener()

    while True:
        data, addr = listener.pick_up_message()
        print(f"incoming message: {data} from {addr}")


if __name__ == '__main__':
    listener_main()

