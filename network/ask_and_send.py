from udp.networking import UDPBroadcaster


def ask_and_send_main():
    broadcaster = UDPBroadcaster()
    print("what to say? ")
    to_say = input()
    broadcaster.send_message(to_say)
    print("I just sent a message!")


if __name__ == '__main__':
    ask_and_send_main()

