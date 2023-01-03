"""
Helper tools for dmarc report generator
"""
import os
import glob
from operator import itemgetter
import netaddr


def ips_to_ipset(cidr_list):
    """
    Take list of IPs, cidrs and return IPSet
    """
    if not cidr_list:
        return None
    ipset = None
    for cidr in cidr_list:
        net = netaddr.IPNetwork(cidr)
        if ipset:
            ipset.add(net)
        else:
            ipset = netaddr.IPSet(net)

    return ipset

def ip_in_ipset(ip_str, ipset):
    """
    Checks if ip is member of ipset
    """
    if not ip_str or not ipset:
        return False
    ip = netaddr.IPAddress(ip_str)
    is_member = ip in ipset
    return is_member

def string_is_ip(ip_str):
    """ check if is an IP address """
    isip = netaddr.valid_ipv4(ip_str) or netaddr.valid_ipv6(ip_str)
    return isip

def sort_by_ip(iplist_str):
    """
    sort a list of IP addresses (str)
    return sorted list
    """
    iplist = [netaddr.IPAddress(ip) for ip in iplist_str]
    sorted_list =  sorted(iplist, key=netaddr.IPAddress.sort_key)
    sorted_list = [str(ip) for ip in sorted_list]
    return sorted_list

def drange_summary(drange_list):
    """
    takes list of [start, end]
    returns earliest start and last end and whether range is continuous by date.
    """
    start = '?'
    end = '?'
    contig = False

    if not drange_list:
        return (start, end, contig)

    # start
    num = len(drange_list)
    #dts = sorted (drange_list, key lambda x: x[0])
    dts = sorted (drange_list, key=itemgetter(0))
    dstart = dts[0][0]
    dend = dts[num-1][1]

    fmt = '%y/%m/%d %H:%M'
    start = dstart.strftime(fmt)
    end = dend.strftime(fmt)
    # contig - we ignore time
    contig = True
    prev = dts[0]
    for idx in range(1, num):
        this = dts[idx]
        if this[0].date() == prev[1].date():
            prev = this
        else:
            contig = False
            break

    contig_flag = ''
    if not contig :
        contig_flag = '*'

    return (start, end, contig_flag)

def get_glob_file_list(topdir, pattern, withpath=False):
    """
    gets list of files in topdir/pattern
      - returns filenames without topdir unless withpath=True
    """
    if topdir.endswith('/'):
        gpat = f'{topdir}{pattern}'
    else:
        gpat = f'{topdir}/{pattern}'

    flist = glob.glob(gpat)
    if not withpath:
        fnames = []
        for fpath in flist:
            file = os.path.basename(fpath)
            fnames.append(file)
        flist = fnames
    return flist

def open_file(path, mode):
    """
     Open a file and return file object
    """
    # pylint: disable=W1514,R1732
    try:
        fobj = open(path, mode)
    except OSError as err:
        print(f'Error opening file {path} : {err}')
        fobj = None
    return fobj

def merge_dict(dic1, dic2):
    """
    Merge dic2 over dic1
    """
    merged = dic1.copy()
    for (key,val) in dic2.items():
        merged[key] = val
    return merged
