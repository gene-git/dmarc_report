# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 DMARC report generator:
   read aggregate dmarc reports files in current directory (RUA) and generate report.
   Files can be xml or zip or gzip xml.
"""
# pylint: disable=R0912,R0913,R0914,R0915

from .xml_tools import xml_pull_item
from .xml_tools import xml_pull_date_range


def dmarc_analyze(rpt, xml):
    """
    Analyze on dmarc report
      input - xml data from one report
    """

    if not xml:
        return

    #
    # Pull from report data
    #
    metadata = xml.find('report_metadata')
    org_name = xml_pull_item(metadata, 'org_name')
    _rpt_id = xml_pull_item(metadata, 'report_id')
    dmarc_policy = xml.find('policy_published')
    domain = xml_pull_item(dmarc_policy, 'domain')
    drange = xml_pull_date_range(metadata)


    org = rpt.get_org(org_name)
    org.add_drange(drange)
    rpt.add_drange(drange)

    #
    # set up report - org.domain :
    #
    dom_rpt = org.get_domain(domain)
    dom_rpt.add_drange(drange)

    nrec = 0
    for record in xml.findall('record'):
        nrec += 1
        ip = xml_pull_item(record,'row/source_ip')
        cnt = xml_pull_item(record,'row/count')
        cnt = int(cnt)

        ip_rpt = dom_rpt.get_ip_rpt(ip)

        ip_rpt.cnt += cnt
        org.total.cnt += cnt
        rpt.total.cnt += cnt

        policy = record.find('row/policy_evaluated')
        disp = xml_pull_item(policy, 'disposition')
        dkim = xml_pull_item(policy, 'dkim')
        spf = xml_pull_item(policy, 'spf')

        if spf == 'pass':
            ip_rpt.spf_policy_pass += cnt
            org.total.spf_policy_pass += cnt
            rpt.total.spf_policy_pass += cnt

        if dkim == 'pass':
            ip_rpt.dkim_policy_pass += cnt
            org.total.dkim_policy_pass += cnt
            rpt.total.dkim_policy_pass += cnt

        if disp == 'none':
            ip_rpt.dmarc_pass += cnt
            org.total.dmarc_pass += cnt
            rpt.total.dmarc_pass += cnt
        else:
            ip_rpt.dmarc_fail += cnt
            org.total.dmarc_fail += cnt
            rpt.total.dmarc_fail += cnt

        _hdr_from = xml_pull_item(record, 'identifiers/header_from')

        dkims = record.findall('auth_results/dkim')
        for dkim in dkims:
            res = xml_pull_item(dkim, 'result')
            _dom = xml_pull_item(dkim, 'domain')
            selector = xml_pull_item(dkim, 'selector')
            if res == 'pass':
                ip_rpt.dkim_auth_pass += cnt
                org.total.dkim_auth_pass += cnt
                rpt.total.dkim_auth_pass += cnt
            else:
                ip_rpt.dkim_auth_fail += cnt
                org.total.dkim_auth_fail += cnt
                rpt.total.dkim_auth_fail += cnt

            # selector
            sel = rpt.get_sel(domain, selector)
            if res == 'pass':
                sel.passes += cnt
            else:
                sel.fails += cnt

            ip_rpt.add_selector(sel.short)
            org.total.add_selector(sel.short)
            rpt.total.add_selector(sel.short)

        spf = record.find('auth_results/spf')
        spf_res = xml_pull_item(spf, 'result')
        _spf_dom = xml_pull_item(spf, 'domain')
        _spf_scope = xml_pull_item(spf, 'scope')

        if spf_res == 'pass':
            ip_rpt.spf_auth_pass += cnt
            org.total.spf_auth_pass += cnt
            rpt.total.spf_auth_pass += cnt
        else:
            ip_rpt.spf_auth_fail += cnt
            org.total.spf_auth_fail += cnt
            rpt.total.spf_auth_fail += cnt
