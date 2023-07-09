# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 Analyze one mta-sts tls report
"""

def tls_analyze(rpt, one_json):
    """
    Analyze one MTA-STS tls report
     - input json data from one report
    """
    if not one_json:
        return

    org_name = one_json['organization-name']
    date_start = one_json['date-range']['start-datetime']
    date_end = one_json['date-range']['end-datetime']

    # TODO: Add drange support

    #
    # There is only 1 policy and 1 domain in eaech policy as far as I know
    #
    dom_name = one_json['policies'][0]['policy'].get('policy-domain')
    success = one_json['policies'][0]['summary']['total-successful-session-count']
    failure = one_json['policies'][0]['summary']['total-failure-session-count']
    success = int(success)
    failure = int(failure)

    org = rpt.get_org(org_name)
    dom = org.get_dom(dom_name)

    if failure > 0:
        failure_details_list = one_json['policies'][0]['failure-details']
        dom.merge_failure_details_list(failure_details_list)


    dom.success += success
    dom.failure += failure

    org.success += success
    org.failure += failure

    rpt.success += success
    rpt.failure += failure
