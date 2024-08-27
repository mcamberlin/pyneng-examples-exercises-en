# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
inp = input("Enter IP network: ")
network_ip, network_bits_nb = inp.split('/')
network_bits_nb = int(network_bits_nb)

network_ip_decimal = network_ip.split('.')

network_mask_bin = '1'*network_bits_nb + '0'*(32-network_bits_nb)

print(f"""
Network:
{network_ip_decimal[0]:<8}  {network_ip_decimal[1]:<8}  {network_ip_decimal[2]:<8}  {network_ip_decimal[3]:<8}
{int(network_ip_decimal[0]):08b}  {int(network_ip_decimal[1]):08b}  {int(network_ip_decimal[2]):08b}  {int(network_ip_decimal[3]):08b}

Mask:
/{network_bits_nb}
{int(network_mask_bin[0:8],2):<8} {int(network_mask_bin[8:16],2):<8} {int(network_mask_bin[16:24],2):<8} {int(network_mask_bin[24:32],2):<8}
""")