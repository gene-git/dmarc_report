# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
Update Org and Domain reports
"""
# pylint: disable=too-many-locals
from datetime import datetime
from .class_tlsrpt import TlsOneRpt
from .class_tlsrpt import TlsReports
from .class_tlsrpt import TlsPolicy
from .class_tlsrpt import TlsOrgReport
from .class_tlsrpt import TlsDomainReport
from .class_tlsrpt import TlsFailSummary


# -------------------------------------------------------------
def _earlier_date(new_date: datetime, curr_date: datetime) -> datetime:
    """ earlier start dates"""
    if not curr_date or (new_date and new_date < curr_date):
        return new_date
    return curr_date


def _later_date(new_date: datetime, curr_date: datetime) -> datetime:
    """ earlier start dates"""
    if not curr_date or (new_date and new_date > curr_date):
        return new_date
    return curr_date
# -------------------------------------------------------------


def _merge_policy(new_pol: TlsPolicy, policy: TlsPolicy):
    """
    Merge new policy into existing.
    """
    policy.success += new_pol.success
    policy.failure += new_pol.failure

    policy.failure_details += new_pol.failure_details

    if new_pol.string:
        policy.string += new_pol.string

    if new_pol.mx_host_pattern:
        policy.mx_host_pattern += new_pol.mx_host_pattern

    #
    # Failure details
    # May change once I see DANE reports but for now
    # only fields updated are result_type and count
    # So we just aggregate
    #
    for fail in new_pol.failure_details:
        count = fail.failed_session_count
        res_type = fail.result_type

        if res_type not in policy.failure_summary:
            policy.failure_summary[res_type] = TlsFailSummary(res_type)
        policy.failure_summary[res_type].count += count


def tls_update_reports(new_rpt: TlsOneRpt, rpts: TlsReports):
    """
     - Add new_rpt to all report list
     - merge new_rpt into domain report
     - merge new_rpt into org report
    """
    rpts.reports.append(new_rpt)
    org_name = new_rpt.org_name

    #
    # Update org report
    #
    if org_name not in rpts.org_rpts:
        rpts.org_rpts[org_name] = TlsOrgReport(org_name)
    org_rpt_dom = rpts.org_rpts[org_name]

    for (ptype, policy) in new_rpt.policies.items():

        #
        # Gather new data
        #
        new_domain = policy.domain
        new_success = policy.success
        new_failure = policy.failure

        #
        # Org report
        #
        if ptype not in org_rpt_dom.policies:
            org_rpt_dom.policies[ptype] = {}        # key by domain

        org_rpt_dom_ptype = org_rpt_dom.policies[ptype]
        if new_domain not in org_rpt_dom_ptype:
            org_rpt_dom_ptype[new_domain] = TlsPolicy(ptype)

        this_pol = org_rpt_dom_ptype[new_domain]

        _merge_policy(policy, this_pol)

        org_rpt_dom.success += new_success
        org_rpt_dom.failure += new_failure

        org_rpt_dom.date_start = _earlier_date(new_rpt.date_start,
                                               org_rpt_dom.date_start)

        org_rpt_dom.date_end = _later_date(new_rpt.date_end,
                                           org_rpt_dom.date_end)

        #
        # Domain report
        #
        if new_domain not in rpts.domain_rpts:
            rpts.domain_rpts[new_domain] = TlsDomainReport(new_domain)
        dom_rpt = rpts.domain_rpts[new_domain]

        if ptype not in dom_rpt.policies:
            dom_rpt.policies[ptype] = {}        # key by org

        dom_rpt_ptype = dom_rpt.policies[ptype]
        if org_name not in dom_rpt_ptype:
            dom_rpt_ptype[org_name] = TlsPolicy(ptype)

        this_pol = dom_rpt_ptype[org_name]
        this_pol.org_name = org_name
        _merge_policy(policy, this_pol)

        dom_rpt.success += new_success
        dom_rpt.failure += new_failure

        dom_rpt.date_start = _earlier_date(new_rpt.date_start,
                                           dom_rpt.date_start)

        dom_rpt.date_end = _later_date(new_rpt.date_end, dom_rpt.date_end)

        #
        # totals
        #
        rpts.success += policy.success
        rpts.failure += policy.failure

    # overall date range
    rpts.date_start = _earlier_date(new_rpt.date_start, rpts.date_start)
    rpts.date_end = _later_date(new_rpt.date_end, rpts.date_end)
