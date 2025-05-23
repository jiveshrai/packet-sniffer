from scapy.all import IP, TCP, UDP, ICMP

def parse_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        parsed_data = {
            'src_ip': ip_layer.src,
            'dst_ip': ip_layer.dst,
            'protocol': ip_layer.proto,
        }

        if TCP in packet:
            tcp_layer = packet[TCP]
            parsed_data.update({
                'type': 'TCP',
                'src_port': tcp_layer.sport,
                'dst_port': tcp_layer.dport
            })

        elif UDP in packet:
            udp_layer = packet[UDP]
            parsed_data.update({
                'type': 'UDP',
                'src_port': udp_layer.sport,
                'dst_port': udp_layer.dport
            })

        elif ICMP in packet:
            parsed_data['type'] = 'ICMP'

        else:
            parsed_data['type'] = 'Unknown'

        return parsed_data

    return None
