"""
Helper tools for dmarc report generator
"""
from operator import itemgetter
import netaddr

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

    fmt = '%Y-%m-%d %H:%M'
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
