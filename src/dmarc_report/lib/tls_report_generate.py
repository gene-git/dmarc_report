# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 Print the actual report
"""
# pylint: disable=too-many-locals

def _format_item(prnt, width, color, txt, lcr='>'):
    """
    Colorize text - hanbdle widht adjustments from additiinal
    ascii color codes in output string
    """
    (txt_fmt, cdel) = prnt.colorize(txt, fg_col=color)
    wid = width + cdel
    txt_fmt = f'{txt_fmt:{lcr}{wid}s}'
    return txt_fmt

def _format_succ_fail(prnt, wid, succ, fail):
    """ format the success and failures columns """
    total = succ + fail

    color = 'okay'
    if succ == 0:
        color = 'error'
    elif succ < total:
        color = 'warn'

    succ_s = f'{succ:,d}'
    succ_s = _format_item(prnt, wid, color, succ_s)

    fail_s = f'{fail:,d}'
    fail_s = _format_item(prnt, wid, color, fail_s)

    return (succ_s, fail_s)

def _date_string(date):
    """ report date string """
    if not date:
        return ''
    fmt = '%y%m%d'
    date_str = date.strftime(fmt)
    return date_str

def generate_tls_report(tls_rpt:'TlsRpt'):
    """
    Print final report
    """
    reports = tls_rpt.reports
    prnt = tls_rpt.prnt
    dom_rpts = reports.domain_rpts

    cw1 = 32
    cw2 = 15
    line_len = (cw1+2*cw2 + 3) 
    line = line_len * '─'
    dash = line_len * '-'

    print(f' {line}')
    print(f'{"Domain"} {"Org":>{cw1-7}} {"success":>15s} {"failure":>15s}')
    for (dom, rpt) in dom_rpts.items():
        start = _date_string(rpt.date_start)
        end = _date_string(rpt.date_end)
        success = rpt.success
        failure = rpt.failure

        dom_s = _format_item(prnt, cw1, 'dom', dom, lcr='<')
        (succ_s, fail_s) = _format_succ_fail(prnt, cw2, rpt.success, rpt.failure)
        print(f'\n{dom_s} {succ_s} {fail_s} {"":3s} {start} ⟶  {end}')

        for (ptype, subreport) in rpt.policies.items():
            if ptype == 'no-policy-found':
                ptype = 'none'
            ptype = f'↪ {ptype}'
            len_ptype = 8
            ptype_s = _format_item(prnt, len_ptype, 'green', ptype)
            print(ptype_s, end='')

            for (org, policy) in subreport.items():
                org_name = policy.org_name
                if not org_name:
                    org_name = '???'
                success = policy.success
                failure = policy.failure

                wid = cw1 - len_ptype
                len_ptype = 0
                org_s = _format_item(prnt, wid, 'org', org_name)
                (succ_s, fail_s) = _format_succ_fail(prnt, cw2, success, failure)
                print(f'{org_s} {succ_s} {fail_s} {"":3s}', end='')

                lines = 0
                for (res_type, fail_summary) in policy.failure_summary.items() :
                    space = 0
                    if lines > 0:
                        spaec = cw1 + cw2 
                    lines += 1
                    count = fail_summary.count
                    res = f'{res_type} ({count:>4d})'
                    res_s = _format_item(prnt, cw1, 'org', res, lcr='<')
                    print(res_s)
                if lines == 0:
                    print('')

    #
    # Grand total
    #
    start = _date_string(reports.date_start)
    end = _date_string(reports.date_end)
    success = reports.success
    failure = reports.failure
    (succ_s, fail_s) = _format_succ_fail(prnt, cw2, success, failure)

    line = (cw1+2*cw2 + 3) * '─'
    print(f' {line}')
    print(f'{"Total":>{cw1}s} {succ_s} {fail_s} {"":3s} {start} ⟶  {end}')
