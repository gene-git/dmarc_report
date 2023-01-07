# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 Print the actual report
"""

def _format_item(prnt, width, color, txt):
    """
    Colorize text - hanbdle widht adjustments from additiinal
    ascii color codes in output string
    """
    (txt_fmt, cdel) = prnt.colorize(txt, fg_col=color)
    wid = width + cdel
    txt_fmt = f'{txt_fmt:>{wid}s}'
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

def print_tls_report(rpt):
    """ Print final report """

    prnt = rpt.prnt
    cw1 = 30
    cw2 = 15
    # Header
    print('')
    print(f'{"Org":>{cw1}} {"success":>15s} {"failure":>15s}')

    for org in rpt.org:
        org_name = _format_item(prnt, cw1, 'org', org.name)
        #print(f'{org_name}')

        for dom in org.dom:
            dom_name = _format_item(prnt, cw2, 'dom', dom.name)
            (succ_s, fail_s) = _format_succ_fail(prnt, cw2, dom.success, dom.failure)

            print(f'{org_name} {succ_s} {fail_s} {"":3s} ↪ {dom_name}')

    #
    # Grand total
    #
    (succ_s, fail_s) = _format_succ_fail(prnt, cw2, rpt.success, rpt.failure)

    line = (cw1+2*cw2 + 3) * '─'
    print(f' {line}')
    print(f'{"Total":>{cw1}s} {succ_s} {fail_s}')
