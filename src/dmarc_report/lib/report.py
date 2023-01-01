#!/usr/bin/python
"""
 DMARC report generator:
   Report Print
"""
# pylint: disable=R0913,R0914,C0301

from .utils import sort_by_ip
from .utils import drange_summary

def print_report_header(cols):
    """
    rpt column header (printed once for all reporting domains)
    """
    cw1 = cols.cw1
    cw2 = cols.cw2
    cw3 = cols.cw3
    wip = cols.wip
    wvol = cols.wvol

    ldr = 10
    line = (105-ldr)*'-'

    # row 1
    col1 = f'{"":{wip}s} {"":{wvol}s}'
    col2 = f'{"":{cw1}s} {"dmarc":^{cw2}s} {"":{cw3}s}'
    col3 = f'{"":{cw1}s} {"dkim":^{cw2}s} {"":{cw3}s}'
    col4 = f'{"":{cw1}s} {"spf":^{cw2}s} {"":{cw3}s}'
    print(f'{col1} | {col2} | {col3} | {col4}')

    # row 2
    col1 = f'{"IP":>{wip}s} {"Vol":>{wvol}s}'
    col2 = f'{"Pass":>{cw1}s} {"Fail":>{cw2}s} {"%":>{cw3}s}'
    col3 = f'{"Pass":>{cw3}s} {"Fail":>{cw3}s} {"align":>{cw3}s}'
    col4 = 'Sel'
    print(f'{col1} | {col2} | {col3} | {col3} | {col4}')

    # line
    print(f'{"":{ldr}s} {line}')

def print_total(opts, name, tot, cols, do_dashes=True):
    """
    print total for 'name'
    """
    dashes = int(cols.wip/2)*'-'
    line = f'{dashes:>{cols.wip}s}'

    if do_dashes:
        print(f'{line}')
    if tot.cnt > 1:
        print_ip_row(opts, name, tot, cols)
        if do_dashes:
            print(f'{line}')

def print_ip_row(opts, name, iprpt, cols):
    """
    print 1 row of report per IP address
     - name is IP for ip report line, or org/grand total name for totals
    """

    cw1 = cols.cw1
    cw2 = cols.cw2
    cw3 = cols.cw3
    wip = cols.wip
    wvol = cols.wvol

    cnt = iprpt.cnt
    dmarc_pass = iprpt.dmarc_pass
    dmarc_fail = iprpt.dmarc_fail

    dmarc_pct = 0
    if dmarc_pass > 0:
        total = dmarc_pass + dmarc_fail
        dmarc_pct = 100.0 * dmarc_pass / total

    dkim_policy_pass = iprpt.dkim_policy_pass
    spf_policy_pass = iprpt.spf_policy_pass
    spf_auth_pass = iprpt.spf_auth_pass
    spf_auth_fail = iprpt.spf_auth_fail
    dkim_auth_pass = iprpt.dkim_auth_pass
    dkim_auth_fail = iprpt.dkim_auth_fail

    has_fails = False
    if dmarc_fail + dkim_auth_fail + spf_auth_fail > 0:
        has_fails = True

    printit = False
    if not (opts.dmarc_fails or opts.dkim_fails or opts.spf_fails):
        printit = True

    elif opts.dmarc_fails and iprpt.dmarc_fail > 0 :
        printit = True

    elif opts.dkim_fails and iprpt.dkim_auth_fail > 0:
        printit = True

    elif opts.spf_fails and iprpt.spf_auth_fail > 0:
        printit = True

    col1 = f'{name:>{wip}s} {cnt:{wvol},d}'
    col2 = f'{dmarc_pass:{cw1},d} {dmarc_fail:{cw2},d} {dmarc_pct:{cw3}.0f}'
    col3 = f'{dkim_auth_pass:{cw1},d} {dkim_auth_fail:{cw2},d} {dkim_policy_pass:{cw3},d}'
    col4 = f'{spf_auth_pass:{cw1},d} {spf_auth_fail:{cw2},d} {spf_policy_pass:{cw3},d}'

    selectors = ' '.join(iprpt.dkim_selectors)

    if printit:
        print(f'{col1} | {col2} | {col3} | {col4} | {selectors}')


def print_domain_report(opts, org, dom, cols):
    """
    Server -> Domain
                  |   dmarc         | spf              | dkim
    n_ip   n_cnt  |   % good        | auth       polic | auth      polic
    IP     Count  |   pass fail %   | pass fail  pass  | pass fail pass
          25      |   25              25                 25
    """
    (start, end, contig) = drange_summary(dom.drange)

    org_name = org.name
    dom_name = dom.domain

    print('')
    print(f'{org_name} {"":2s} ({dom_name}) {"":10s} {start} - {end} {contig}')

    #
    # sort by IP
    #
    iplist = []
    for (ip, _ip_rpt) in dom.ip_rpt.items():
        iplist.append(ip)
    iplist_sorted = sort_by_ip(iplist)

    for ip in iplist_sorted:
        iprpt = dom.ip_rpt[ip]
        print_ip_row(opts, ip, iprpt, cols)

class ColWidth:
    """ Column Widths """
    # pylint: disable=R0903
    def __init__(self):
        self.cw1 = 5
        self.cw2 = 5
        self.cw3 = 5
        self.wip = 30
        self.wvol = 5

def print_report(rpt):
    """
    Print out dmarc report from all reporting domains
    """
    cols = ColWidth()

    print_report_header(cols)

    for org in rpt.org:
        for dom in org.domain:
            print_domain_report(rpt.opts, org, dom, cols)

        # if more than one IP entry then show total
        num_ips = org.get_num_ips()
        if num_ips > 1:
            print_total(rpt.opts, org.name, org.total, cols)

    #
    # print selector map
    #
    print('\nSelector Map:')
    dash6 = 6*'-'
    dash20 = 20 *'-'
    sel_map = rpt.sel_map

    print(f'{"":5s} {"Short":^6s} {"Selector":20s} {"Pass":>6s} {"Fail":>6s}   {"domain":20s}')
    print(f'{"":5s} {dash6:^6s} {dash20:20s} {dash6:>6s} {dash6:>6s}   {dash20:20s}')
    for sel in sel_map.selectors:
        print(f'{"":5s} {sel.short:^6s} {sel.name:20s} {sel.passes:>6,d} {sel.fails:>6,d}   {sel.domain}')

    #
    # If more than 1 org processed then add grand total
    #
    num_orgs = rpt.get_num_orgs()
    if num_orgs > 1:
        ldr = 10
        line = (105-ldr)*'-'
        print(f'{"":{ldr}s} {line}')

        print_report_header(cols)

        (start, end, contig) = drange_summary(rpt.drange)

        wip = cols.wip
        print(f'{"Period":>{wip}s} {"":10s} {start} - {end} {contig}')
        print(f'{"":{ldr}s} {line}')

        # totals for each org
        total_num_ips = 0
        for org in rpt.org:
            num_ips = org.get_num_ips()
            total_num_ips += num_ips
            if num_ips > 1:
                print_total(rpt.opts, org.name, org.total, cols, do_dashes=False)
        if total_num_ips > 1:
            print_total(rpt.opts, 'Grand Total', rpt.total, cols)
