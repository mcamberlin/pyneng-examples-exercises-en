# -*- coding: utf-8 -*-
"""
Task 4.6

Process the ospf_route string and print the information to the stdout as follows:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d20h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d20h, FastEthernet0/0"
tab = ospf_route.strip().replace(',','').split()

s = "{:<20} {}\n{:<20} {}\n{:<20} {}\n{:<20} {}\n{:<20} {}".format(
    "Prefix", tab[0],
    "AD/Metric", tab[1].replace('[','').replace(']',''),
    "Next-Hop", tab[3],
    "Last Update", tab[4],
    "Outbound Interface", tab[5])
print(s)