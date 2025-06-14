# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 Analyze one TLS-RPT dane/mta-sts report
 Per
 https://datatracker.ietf.org/doc/draft-ietf-uta-smtp-tlsrpt/16/
 Report is of the form:

 {
   "organization-name": organization-name,
   "date-range": {
     "start-datetime": date-time,
     "end-datetime": date-time
   },
   "contact-info": email-address,
   "report-id": report-id,
   "policies": [{
     "policy": {
       "policy-type": policy-type,
       "policy-string": policy-string,
       "policy-domain": domain,
       "mx-host": mx-host-pattern
     },
     "summary": {
       "total-successful-session-count": total-successful-session-count,
       "total-failure-session-count": total-failure-session-count
     },
     "failure-details": [
       {
         "result-type": result-type,
         "sending-mta-ip": ip-address,
         "receiving-mx-hostname": receiving-mx-hostname,
         "receiving-mx-helo": receiving-mx-helo,
         "receiving-ip": receiving-ip,
         "failed-session-count": failed-session-count,
         "additional-information": additional-info-uri,
         "failure-reason-code": failure-reason-code
         }
       ]
     }
   ]
 }
"""
# pylint: disable=too-many-locals

from datetime import datetime
from dateutil import tz, parser
from .class_tlsrpt import TlsOneRpt
from .class_tlsrpt import TlsPolicy
from .class_tlsrpt import TlsFailureDetails


def _date_from_string(date_str: str) -> datetime:
    """ try parse date """
    local_zone = tz.tzlocal()
    date = parser.parse(date_str)
    date = date.astimezone(local_zone)

    return date


def tls_analyze_one(json_rpt: dict) -> TlsOneRpt:
    """
    Analyze one tls report
     - may conttain MTA-STS, DANE,
     - input one json data string
    returns TlsOneRpt
    """
    # if not json_rpt:
    #     return None

    #
    # organization-name
    #
    org_name = json_rpt['organization-name']
    rpt = TlsOneRpt(org_name)

    #
    # date-range
    #
    date_range = json_rpt['date-range']
    date_start = date_range['start-datetime']
    date_end = date_range['end-datetime']
    if date_start:
        rpt.date_start = _date_from_string(date_start)
    if date_end:
        rpt.date_end = _date_from_string(date_end)

    #
    # policies
    #   - can be up to 3 policies of types:
    #     tlsa, sts, no-policy-found
    #
    policies = json_rpt['policies']

    for pol_item in policies:
        # policy
        policy = pol_item['policy']
        ptype = policy.get('policy-type')
        if not ptype:
            ptype = 'no-policy-found'
        domain = policy.get('policy-domain')
        string = policy.get('policy-string')
        mx_host_pattern = policy.get('mx-host-pattern')

        # summary
        summary = pol_item.get('summary')
        success = summary.get('total-successful-session-count')
        failure = summary.get('total-failure-session-count')

        this_policy = TlsPolicy(ptype)
        this_policy.org_name = org_name
        this_policy.string = string
        this_policy.domain = domain
        this_policy.mx_host_pattern = mx_host_pattern
        if not success:
            success = 0
        if not failure:
            failure = 0
        this_policy.success += int(success)
        this_policy.failure += int(failure)

        # failure-details
        failure_details = pol_item.get("failure-details")
        if failure_details:
            for fail in failure_details:
                this_fail = TlsFailureDetails()
                this_fail.result_type = fail.get('result-type')
                this_fail.sending_mta_ip = fail.get('sending-mta-ip')
                this_fail.receiving_mx_hostname = \
                    fail.get('receiving-mx-hostname')
                this_fail.receiving_mx_helo = fail.get('receiving-mx-helo')
                this_fail.receiving_ip = fail.get('receiving-ip')
                failed_session_count = fail.get('failed-session-count')
                if failed_session_count:
                    failed_session_count = int(failed_session_count)
                    this_fail.failed_session_count += failed_session_count

                this_fail.additional_information = \
                    fail.get('additional-information')
                this_fail.failure_reason_code = fail.get('failure-reason-code')

                this_policy.failure_details.append(this_fail)

        rpt.policies[ptype] = this_policy

    return rpt
