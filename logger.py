from utils import current_timestamp

def log_packet(data):
    print(f"\n[{current_timestamp()}] Packet Captured:")
    print(f"  Source IP      : {data['src_ip']}")
    print(f"  Destination IP : {data['dst_ip']}")
    print(f"  Protocol       : {data.get('type', 'Unknown')}")
    
    if 'src_port' in data:
        print(f"  Source Port    : {data['src_port']}")
    if 'dst_port' in data:
        print(f"  Destination Port: {data['dst_port']}")

    # Optional: Log to file
    with open("captured_packets.log", "a") as f:
        f.write(f"{current_timestamp()} | {data}\n")
