## PACKET SNIFFER

This program filters intercepted data and has the potential to show usernames, passwords, visited links, etc.
(Please note you will need to bypass HTTPS to achieve this.)

### Requirements

* Become MITM. You may use ARP SPOOFER program in this suite of tools to achieve this.
* I strongly recommend bypassing HTTPS to get the most results out of this program. 

`packet_sniffer.py` currently uses a sample list of basic keywords to fetch Login informatiom from the packets sent.
You might want to add words to this list. Use `cat packet_sniffer.py` to see the program. 
You also need to change the **NIC** to the interface you will be sniffing from. 
