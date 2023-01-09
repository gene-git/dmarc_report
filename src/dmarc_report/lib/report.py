# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 DMARC report generator:
   Report Print
"""
# pylint: disable=R0913,R0914,C0301

from .utils import sort_by_ip
from .utils import string_is_ip
from .utils import drange_summary
from .report_colors import dmarc_colors
from .report_colors import dkim_colors
from .report_colors import spf_colors

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
    line = (105-ldr)*'─'

    # row 1
    col1 = f'{"":{wip}s} {"":{wvol}s}'
    col2 = f'{"":{cw1}s} {"dmarc":^{cw2}s} {"":{cw3}s}'
    col3 = f'{"":{cw1}s} {"dkim":^{cw2}s} {"":{cw3}s}'
    col4 = f'{"":{cw1}s} {"spf":^{cw2}s} {"":{cw3}s}'
    #print(f'{col1} | {col2} | {col3} | {col4}')
    print(f'{col1} │ {col2} │ {col3} │ {col4}')

    # row 2
    col1 = f'{"IP":>{wip}s} {"Vol":>{wvol}s}'
    col2 = f'{"Pass":>{cw1}s} {"Fail":>{cw2}s} {"%":>{cw3}s}'
    col3 = f'{"Pass":>{cw3}s} {"Fail":>{cw3}s} {"align":>{cw3}s}'
    col4 = 'Sel'
    #print(f'{col1} | {col2} | {col3} | {col3} | {col4}')
    print(f'{col1} │ {col2} │ {col3} │ {col3} │ {col4}')

    # line
    print(f'{"":{ldr}s} {line}')

def print_total(rpt, name, tot, cols, do_dashes=True):
    """
    print total for 'name'
    """
    dashes = int(cols.wip/2)*'─'
    line = f'{dashes:>{cols.wip}s}'

    if do_dashes:
        print(f'{line}')
    if tot.cnt > 1 or not do_dashes:        # summary has no dashes
        print_ip_row(rpt, name, tot, cols)
        if do_dashes:
            print(f'{line}')

def _format_item(prnt, width, color, txt):
    """
    Colorize text - hanbdle widht adjustments from additiinal
    ascii color codes in output string
    """
    (txt_fmt, cdel) = prnt.colorize(txt, fg_col=color)
    wid = width + cdel
    txt_fmt = f'{txt_fmt:>{wid}s}'
    return txt_fmt

def print_ip_row(rpt, name, iprpt, cols):
    """
    print 1 row of report per IP address
     - name is IP for ip report line, or org/grand total name for totals
    """
    # pylint: disable=R0915
    opts = rpt.opts
    prnt = rpt.prnt

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

    printit = False
    if not (opts.dmarc_fails or opts.dkim_fails or opts.spf_fails):
        printit = True

    elif opts.dmarc_fails and iprpt.dmarc_fail > 0 :
        printit = True

    elif opts.dkim_fails and iprpt.dkim_auth_fail > 0:
        printit = True

    elif opts.spf_fails and iprpt.spf_auth_fail > 0:
        printit = True

    #
    # IP column
    #
    wid = cols.wip
    if string_is_ip(name) and rpt.ip_in_dom_ips(name):
        (name, cdel) = prnt.colorize(name, fg_col='dom')
        wid = cols.wip + cdel
    col_ip = f'{name:>{wid}s} {cnt:{cols.wvol},d}'

    #
    # DMARC column
    #
    color = dmarc_colors(cnt, dmarc_pass, dmarc_fail, dmarc_pct)

    pass_s = f'{dmarc_pass:,d}'
    pass_s = _format_item(prnt, cols.cw1, color, pass_s)

    fail_s = f'{dmarc_fail:,d}'
    fail_s = _format_item(prnt, cols.cw2, color, fail_s)

    pct_s = f'{dmarc_pct:3.0f}'
    pct_s = _format_item(prnt, cols.cw3, color, pct_s)

    col_dmarc = f'{pass_s} {fail_s} {pct_s}'

    #
    # DKIM column
    #
    (color_pass, color_fail, color_align) = dkim_colors(cnt, dkim_auth_pass, dkim_auth_fail, dkim_policy_pass)

    pass_s = f'{dkim_auth_pass:,d}'
    pass_s = _format_item(prnt, cols.cw1, color_pass, pass_s)

    fail_s = f'{dkim_auth_fail:,d}'
    fail_s = _format_item(prnt, cols.cw2, color_fail, fail_s)

    align_s = f'{dkim_policy_pass:,d}'
    align_s = _format_item(prnt, cols.cw3, color_align, align_s)

    col_dkim = f'{pass_s} {fail_s} {align_s}'

    #
    # SPF column
    #
    (color_pass, color_fail, color_align) = spf_colors(cnt, spf_auth_pass, spf_auth_fail, spf_policy_pass)

    pass_s = f'{spf_auth_pass:,d}'
    pass_s = _format_item(prnt, cols.cw1, color_pass, pass_s)

    fail_s = f'{spf_auth_fail:,d}'
    fail_s = _format_item(prnt, cols.cw2, color_fail, fail_s)

    align_s = f'{spf_policy_pass:,d}'
    align_s = _format_item(prnt, cols.cw3, color_align, align_s)

    col_spf = f'{pass_s} {fail_s} {align_s}'

    #
    # Selectors seen
    #
    selectors = '' 
    if iprpt.dkim_selectors:
        sel_sorted = sorted(iprpt.dkim_selectors)
        selectors = ' '.join(sel_sorted)

    if printit:
        #print(f'{col_ip} | {col_dmarc} | {col_dkim} | {col_spf} | {selectors}')
        print(f'{col_ip} │ {col_dmarc} │ {col_dkim} │ {col_spf} │ {selectors}')


def print_domain_report(rpt, org, dom, cols):
    """
    Server -> Domain
                  |   dmarc         | spf              | dkim
    n_ip   n_cnt  |   % good        | auth       polic | auth      polic
    IP     Count  |   pass fail %   | pass fail  pass  | pass fail pass
          25      |   25              25                 25
    """
    prnt = rpt.prnt

    (start, end, contig) = drange_summary(dom.drange)

    org_name = org.name
    dom_name = dom.domain

    print('')
    (org_name, cdel_org) = prnt.colorize(org.name, fg_col='org')
    (dom_name, _cdel_dom)  = prnt.colorize(dom.domain, fg_col='dom')
    wip = cols.wip + cdel_org

    date_range = f'{start} - {end} {contig}'
    (date_range, _cdel)  = prnt.colorize(date_range, fg_col='org')

    print(f' {org_name:{wip}s} {"":5s} {date_range}')
    print(f' {"":3s} ↪ {dom_name}')

    #
    # sort by IP
    #
    iplist = []
    for (ip, _ip_rpt) in dom.ip_rpt.items():
        iplist.append(ip)
    iplist_sorted = sort_by_ip(iplist)

    for ip in iplist_sorted:
        iprpt = dom.ip_rpt[ip]
        print_ip_row(rpt, ip, iprpt, cols)

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
    prnt = rpt.prnt

    print(f' Report data directory: {rpt.opts.dir}')
    print_report_header(cols)

    for org in rpt.org:
        for dom in org.domain:
            print_domain_report(rpt, org, dom, cols)

        # if more than one IP entry then show total
        num_ips = org.get_num_ips()
        if num_ips > 1:
            print_total(rpt, org.name, org.total, cols)

    #
    # print selector map
    #
    print(f'\n{"":13s}DKIM Selector Map')
    dash6 = 6*'─'
    dash20 = 20 *'─'
    sel_map = rpt.sel_map

    print(f'{"":5s} {"Short":^6s} {"Selector":20s} {"Pass":>6s} {"Fail":>6s}   {"domain":20s}')
    print(f'{"":5s} {dash6:^6s} {dash20:20s} {dash6:>6s} {dash6:>6s}   {dash20:20s}')
    for sel in sel_map.selectors:
        if sel.fails == 0:
            color = 'okay'
        elif sel.passes == 0:
            color = 'error'
        else:
            color = 'warn'
        pass_s = f'{sel.passes:>d}'
        (pass_s, cdel)  = prnt.colorize(pass_s, fg_col=color)
        wid = 6 + cdel
        pass_s = f'{pass_s:>{wid}s}'

        fail_s = f'{sel.fails:>6,d}'
        (fail_s, cdel)  = prnt.colorize(fail_s, fg_col=color)
        wid = 6 + cdel
        fail_s = f'{fail_s:{wid}s}'

        print(f'{"":5s} {sel.short:^6s} {sel.name:20s} {pass_s} {fail_s}   {sel.domain}')

    #
    # If more than 1 org processed then add grand total
    #
    num_orgs = rpt.get_num_orgs()
    if num_orgs > 1:
        ldr = 10
        line = (105-ldr)*'─'
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
            #if num_ips > 1:
            print_total(rpt, org.name, org.total, cols, do_dashes=False)
        if total_num_ips > 1:
            print_total(rpt, 'Grand Total', rpt.total, cols)
