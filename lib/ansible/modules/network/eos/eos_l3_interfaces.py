#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_l3_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network',
}

DOCUMENTATION = """
---
module: eos_l3_interfaces
version_added: 2.9
short_description: 'Manages L3 interface attributes of Arista EOS devices.'
description: 'This module provides declarative management of Layer 3 interfaces on Arista EOS devices.'
author: Nathaniel Case (@qalthos)
notes:
- 'Tested against vEOS v4.20.x'
- This module works with connection C(network_cli). See the
  L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: A dictionary of Layer 3 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface, i.e. Ethernet1.
        type: str
        required: True
      ipv4:
        description:
        - List of IPv4 addresses to be set for the Layer 3 interface mentioned in I(name) option.
        type: list
        elements: dict
        suboptions:
          address:
            description:
            - IPv4 address to be set in the format <ipv4 address>/<mask>
              eg. 192.0.2.1/24, or C(dhcp) to query DHCP for an IP address.
            type: str
          secondary:
            description:
            - Whether or not this address is a secondary address.
            type: bool
            default: False
      ipv6:
        description:
        - List of IPv6 addresses to be set for the Layer 3 interface mentioned in I(name) option.
        type: list
        elements: dict
        suboptions:
          address:
            description:
            - IPv6 address to be set in the address format is <ipv6 address>/<mask>
              eg. 2001:db8:2201:1::1/64 or C(auto-config) to use SLAAC to chose an address.
            type: str
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""

EXAMPLES = """
---

# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Delete L3 attributes of given interfaces.
  eos_l3_interfaces:
    config:
      - name: Ethernet1
      - name: Ethernet2
    state: deleted

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config


# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Merge provided configuration with device configuration.
  eos_l3_interfaces:
    config:
      - name: Ethernet1
        ipv4:
          address: 198.51.100.14/24
      - name: Ethernet2
    ipv4:
      address: 203.0.113.27/24
    state: merged

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config


# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Override device configuration of all L2 interfaces on device with provided configuration.
  eos_l3_interfaces:
    config:
      - name: Ethernet1
        ipv6:
          address: 2001:db8:feed::1/96
      - name: Management1
        ipv4:
          address: dhcp
    ipv6: auto-config
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config


# Using replaced

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  eos_l3_interfaces:
    config:
      - name: Ethernet2
        ipv4:
          address: 203.0.113.27/24
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Ethernet2', 'ip address 192.0.2.12/24']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.eos.argspec.l3_interfaces.l3_interfaces import L3_interfacesArgs
from ansible.module_utils.network.eos.config.l3_interfaces.l3_interfaces import L3_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=L3_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = L3_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
