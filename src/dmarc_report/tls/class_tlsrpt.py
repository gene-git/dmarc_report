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
from typing import (Dict, List)
from datetime import (datetime, timezone)


class TlsFailSummary:
    """ what we use in report """
    def __init__(self, result_type: str):
        self.result_type: str = result_type
        self.count: int = 0


class TlsFailureDetails:
    """ failure details """
    def __init__(self):
        self.result_type: str = ''
        self.sending_mta_ip: str = ''
        self.receiving_mx_hostname: str = ''
        self.receiving_mx_helo: str = ''
        self.receiving_ip: str = ''
        self.failed_session_count: int = 0
        self.additional_information: str = ''
        self.failure_reason_code: str = ''


class TlsPolicy:
    """ result of one policy (tlsa, sts, no-policy) """
    def __init__(self, policy_type: str):
        self.type = policy_type
        self.domain: str = ''
        self.org_name: str = ''
        self.string: List[str] = []
        self.mx_host_pattern: List[str] = []

        self.success: int = 0
        self.failure: int = 0

        self.failure_details: List[TlsFailureDetails] = []
        self.failure_summary: Dict[str, TlsFailSummary] = {}


class TlsOneRpt:
    """ One report from one org"""
    def __init__(self, org_name: str):
        self.org_name = org_name
        self.date_start: datetime = datetime.now(timezone.utc)
        self.date_end: datetime = datetime.now(timezone.utc)

        # policy_types = ('tlsa', 'sts', 'no_policy')
        #
        self.policies: Dict[str, TlsPolicy] = {}        # 'tlsa' : TlsPolicy


class TlsOrgReport:
    """ All reports from one org """
    def __init__(self, org_name: str):
        self.org_name: str = org_name

        # summary
        self.date_start: datetime = datetime.now(timezone.utc)
        self.date_end: datetime = datetime.now(timezone.utc)
        self.success: int = 0
        self.failure: int = 0

        # policy_types:
        #   ('tlsa', 'sts', 'no_policy')
        # policies:
        #   {'tlsa': {'domain' : policy, 'domain2' :  policy2, ...}
        self.policies: Dict[str, Dict[str, TlsPolicy]] = {}


class TlsDomainReport:
    """ All reports from one org """
    def __init__(self, domain: str):
        self.domain: str = domain

        # summary
        self.date_start: datetime = datetime.now(timezone.utc)
        self.date_end: datetime = datetime.now(timezone.utc)
        self.success: int = 0
        self.failure: int = 0

        # policy_types = ('tlsa', 'sts', 'no_policy')
        # for each type : {org:tls_policy dict]
        #                 {'org': tls_pol, 'org': tls_pol, ... }
        self.policies: Dict[str, Dict[str, TlsPolicy]] = {}


class TlsReports:
    """ all reports """
    def __init__(self):
        self.reports: List[TlsOneRpt] = []
        self.domain_rpts: Dict[str, TlsDomainReport] = {}
        self.org_rpts: Dict[str, TlsOrgReport] = {}

        # summary
        self.date_start: datetime = datetime.now(timezone.utc)
        self.date_end: datetime = datetime.now(timezone.utc)
        self.success: int = 0
        self.failure: int = 0
