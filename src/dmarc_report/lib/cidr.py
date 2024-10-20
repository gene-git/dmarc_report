# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Gene C
'''
Network Address Tools
'''
import re
import ipaddress
from ipaddress import (AddressValueError, NetmaskValueError)
from ipaddress import (IPv4Network, IPv6Network, IPv4Address, IPv6Address)

def cidr_to_net(cidr:str, strict:bool=False) -> IPv4Network | IPv6Network | None:
    '''
    Returns the network associated with the cidr string
     - if strict is True then invalid if host bits are set.
     - see ipaddress docs
    '''
    if not cidr:
        return None

    return ipaddress.ip_network(cidr, strict=strict)

def cidrs_to_nets(cidrs:[str], strict:bool=False) -> [IPv4Network | IPv6Network]:
    '''
    For list of cidr strings return list of ip_network
    '''
    nets = [ipaddress.ip_network(cidr, strict=strict) for cidr in cidrs]
    return nets

def ip_to_address(ip:str) -> IPv4Address|IPv6Address|None:
    '''
    Return ip address of given ip.
    If ip has prefix and host bits set, we strip the prefix first
    '''
    if not ip:
        return None

    ipin = ip
    if '/' in ip:
        ipin = re.sub(r'/.*$', '',  ip)

    addr = ipaddress.ip_address(ipin)
    return addr

def ips_to_addresses(ips:[str]) -> [IPv4Address | IPv6Address]:
    '''
    For list of ip strings return list of ip addresses
    '''
    addresses = [ip_to_address(ip) for ip in ips]
    return addresses

def addresses_to_ips(addresses:[IPv4Address | IPv6Address]) -> [str]:
    '''
    For list of ip addresses return list of ip as strings
    '''
    ips = [str(address) for address in addresses]
    return ips

def nets_to_cidrs(nets:[IPv4Network | IPv6Network]) -> [str]:
    '''
    List of nets to list of cidr strings
    '''
    cidrs = [str(net) for net in nets]
    return cidrs

def cidr_is_subnet(cidr:str, ipa_nets:[IPv4Network | IPv6Network]) -> bool:
    '''
    Checks if cidr (string) is a subnet in any of the nets in ipa_nets
    '''
    if not cidr or not ipa_nets:
        return False

    this_net = cidr_to_net(cidr)
    if not this_net:
        return False

    this_ipt = cidr_iptype(this_net)
    for net in ipa_nets:
        net_ipt = cidr_iptype(net)
        if net_ipt != this_ipt:
            return False
        if this_net.subnet_of(net):
            return True

    return False

def is_valid_ip4(address) -> bool:
    ''' check if valid address or cidr '''
    try:
        _check = ipaddress.IPv4Network(address, strict=False)
        return True
    except (AddressValueError, NetmaskValueError, TypeError):
        return False

def is_valid_ip6(address) -> bool:
    ''' check if valid address or cidr '''
    try:
        _check = ipaddress.IPv6Network(address, strict=False)
        return True
    except (AddressValueError, NetmaskValueError, TypeError):
        return False

def is_valid_cidr(address) -> bool:
    '''
    check if valid ip address
     - returns True/False
    '''
    if not address:
        return False
    if is_valid_ip4(address) or is_valid_ip6(address):
        return True
    return False

def cidr_iptype(address) -> str|None :
    '''
    check if valid ip address
     - returns iptype of 'ip4' or 'ip6' or None
    '''
    if not address:
        return None
    if is_valid_ip4(address) :
        return 'ip4'
    if is_valid_ip6(address):
        return 'ip6'
    return None

def sort_cidrs(cidrs:[str]) -> [str]:
    '''
    Sort the list of cidr strings
    '''
    nets = cidrs_to_nets(cidrs)
    nets_sorted = sorted(nets, key=ipaddress.get_mixed_type_key)
    cidrs_sorted = nets_to_cidrs(nets_sorted)
    return cidrs_sorted

def sort_ips(ips:[str]) -> [str]:
    '''
    Sort the list of cidr strings
    '''
    addresses = ips_to_addresses(ips)
    addresses_sorted = sorted(addresses, key=ipaddress.get_mixed_type_key)
    addresses_sorted = addresses_to_ips(addresses_sorted)
    return addresses_sorted
