# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 MTA-STS TLS Report Class
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
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods

class TlsFailSummary:
    """ what we use in report """
    def __init__(self, result_type):
        self.result_type = result_type
        self.count = 0

class TlsFailureDetails:
    """ failure details """
    def __init__(self):
        self.result_type = None
        self.sending_mta_ip = None
        self.receiving_mx_hostname = None
        self.receiving_mx_helo = None
        self.receiving_ip = None
        self.failed_session_count = 0
        self.additional_information = None
        self.failure_reason_code = None

class TlsPolicy:
    """ result of one policy (tlsa, sts, no-policy) """
    def __init__(self, policy_type:str):
        self.type = policy_type
        self.domain = None
        self.org_name = None
        self.string = []
        self.mx_host_pattern = []

        self.success = 0
        self.failure = 0

        self.failure_details = []       # [TlsFailureDetails]
        self.failure_summary = {}       # {result_type  : TlsFailSummary}

class TlsOneRpt:
    """ One report from one org"""
    def __init__(self, org_name):
        self.org_name = org_name
        self.date_start = None
        self.date_end = None

        # policy_types = ('tlsa', 'sts', 'no_policy')
        #
        self.policies = {}        # 'tlsa' : TlsPolicy

class TlsOrgReport:
    """ All reports from one org """
    def __init__(self, org_name):
        self.org_name = org_name

        # summary
        self.date_start = None
        self.date_end = None
        self.success = 0
        self.failure = 0

        # policy_types = ('tlsa', 'sts', 'no_policy')
        # policies {'tlsa' : {'domain' : tls_policy, 'domain2' :  tls_policy2, ...}
        self.policies = {}

class TlsDomainReport:
    """ All reports from one org """
    def __init__(self, domain):
        self.domain = domain

        # summary
        self.date_start = None
        self.date_end = None
        self.success = 0
        self.failure = 0

        # policy_types = ('tlsa', 'sts', 'no_policy')
        # for each type : {org:tls_policy dict]
        #                 {'org': tls_pol, 'org': tls_pol, ... }
        self.policies = {}

class TlsReports:
    """ all reports """
    def __init__(self):
        self.reports = []
        self.domain_rpts = {}
        self.org_rpts = {}

        # summary
        self.date_start = None
        self.date_end = None
        self.success = 0
        self.failure = 0
