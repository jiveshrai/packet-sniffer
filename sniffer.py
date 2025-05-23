from scapy.all import sniff
from packet_parser import parse_packet
from logger import log_packet

def packet_callback(packet):
    parsed_data = parse_packet(packet)
    if parsed_data:
        log_packet(parsed_data)

def start_sniffing(interface: str, packet_count: int):
    sniff(iface=interface, prn=packet_callback, store=False, count=packet_count)
