from sniffer import start_sniffing

def main():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    packet_count = int(input("Enter number of packets to capture (0 for infinite): "))

    print(f"\nStarting packet sniffing on {interface}...\n")
    start_sniffing(interface, packet_count)

if __name__ == "__main__":
    main()
