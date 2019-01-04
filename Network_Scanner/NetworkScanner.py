import scapy.all as scapy


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    final_packet = broadcast/arp_req
    # answered, not_answered = scapy.srp(final_packet, timeout=1)
    answered = scapy.srp(final_packet, timeout=1, verbose=False)[0]

    template = "{0:8}  |  {1:10}"  # column widths:
    print (template.format("IP", "MAC Address"))  # header
    print("------------------------------")
    for element in answered:
        print(template.format(element[1].psrc,element[1].hwsrc))

    # to get the summary of a packet use : packet.summary() or packet.show()
    # to get more info use : scapy.ls(type)

scan("10.0.2.1/24")
