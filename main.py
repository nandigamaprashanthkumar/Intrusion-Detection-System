from scapy.all import sniff, IP, TCP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Example: Detect potential port scanning
        if TCP in packet:
            flags = packet[TCP].flags
            if flags == 2:  # SYN packet
                print(f"Potential Port Scanning Detected from {ip_src} to {ip_dst}")

        # Example: Detect ICMP Echo Request (Ping) flood
        elif ICMP in packet and packet[ICMP].type == 8:
            print(f"Ping Flood Detected from {ip_src} to {ip_dst}")

# Start packet capture
sniff(prn=packet_callback, store=0, iface="Wi-Fi", filter="tcp or icmp")
