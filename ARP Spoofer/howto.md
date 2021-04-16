## ARP SPOOFER

This file contains two arp spoofer tools to run an arp spoofing attack and redirect the flow of packets
in the network. As a result, you will be able to intercept data and become MITM. 

Please note there is a difference between: `arp_spoofy_cmmdlineargs.py` and `arp_spoofy.py`:

* ```arp_spoofy_cmmdlineargs.py``` needs you to input **target_IP** **gateway_IP** commands directly in the terminal.
Example: `python3 arp_spoofy_cmmdlineargs.py -IPt 10.0.0.2 -IPg 10.0.0.1`

* ```arp_spoofy.py``` needs you to input the **target_ip** and **gateway_ip** in the code itself.
Use `cat arp_spoofy.py` to inspect the content of the program.

Once you have successfuly established a connection (and you are running the program in the terminal), you will
need to allow **PORT FORWARDING** so the victim machine can have regular access to the internet. There are several ways
to achieve this, I suggest typing in the terminal: `echo 1 > /proc/sys/net/ipv4/ip_forward`

 
## ARP SPOOFER DETECTOR

* `arp_spoofy_detector.py` can detect ARP spoofing attacks. You may need to input the **NIC** you'd like
to sniff directly into the program. 
Use `cat apr_spoofy_detector.py` to inspect the content of the program. 
