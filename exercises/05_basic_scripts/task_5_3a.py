# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
interface_mode = input("Enter interface mode (access/trunk): ")
if interface_mode == "access":
    interface_type_and_number = input("Enter interface type and number: ")
    vlan_number = input("Enter VLAN number: ")
    commands = ["", f"interface {interface_type_and_number}"]
    for cmd in access_template:
        if(cmd == "switchport access vlan {}"):
            commands.append(cmd.format(vlan_number))
        else:
            commands.append(cmd)
    print("\n".join(commands))

else:
    interface_type_and_number = input("Enter interface type and number: ")
    vlan_numbers = input("Enter the allowed VLANs: ")
    commands = ["", f"interface {interface_type_and_number}"]
    for cmd in trunk_template:
        if(cmd == "switchport trunk allowed vlan {}"):
            commands.append(cmd.format(vlan_numbers))
        else:
            commands.append(cmd)
    print("\n".join(commands))   
