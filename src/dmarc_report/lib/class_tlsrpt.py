# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 MTA-STS TLS Report Class
"""
# pylint: disable=R0903
from .class_tls_options import TlsOpts
from .tls_report import print_tls_report
from .class_print import Prnt
from .save_input_files import input_files_disposition
from .tls_analyze import tls_analyze
from .utils import file_ext_list

class TlsDom:
    """ Data for 1 domain as reported by 1 org """
    def __init__(self, dom_name):
        self.name = dom_name
        self.success = 0
        self.failure = 0
        self.failure_details_all = []
        self.failure_details_sum = []

    def merge_failure_details(self, details):
        """ update sum and all """

        if not self.failure_details_sum:
            self.failure_details_sum.append(details)
        else:
            result_type = details.get('result-type')
            session_count = details.get('failed-session-count')
            for item in self.failure_details_sum:
                if item['result-type'] == result_type:
                    item['failed-session-count'] += session_count

        self.failure_details_all.append(details)

    def merge_failure_details_list(self, details_list):
        """ update sum and all """
        for details in details_list:
            self.merge_failure_details(details)

class TlsOrg:
    """ report for each reporting organiziation """
    def __init__(self, org_name):
        self.name = org_name
        self.dom = []
        self.success = 0
        self.failure = 0

    def get_dom(self, dom_name):
        """ get TlsDom instance for dom_name """
        dom = None
        for this_dom in self.dom:
            if this_dom.name == dom_name:
                dom = this_dom
                break
        if not dom:
            dom = TlsDom(dom_name)
            self.dom.append(dom)
        return dom

class TlsRpt:
    """
    Report class for MTA-STS TLS reports
    """
    def __init__(self):
        self.opts = TlsOpts()

        self.org = []
        self.success = 0
        self.failure = 0
        self.prnt = Prnt(self.opts.theme)

    def get_org(self, org_name):
        """ return org_name class instance """
        org = None
        for this_org in self.org:
            if this_org.name == org_name:
                org = this_org
                break
        if not org:
            org = TlsOrg(org_name)
            self.org.append(org)
        return org

    def get_num_orgs(self):
        """ number of orgs """
        num_orgs = len(self.org)
        return num_orgs

    def analyze(self, json):
        """
        Analyze one json report and add to report
        """
        tls_analyze(self, json)

    def print(self):
        """ print the report """
        print_tls_report(self)

    def input_disposition(self, json_files):
        """ handle disposition of all input files """
        input_files_disposition(self.opts, self.prnt, json_files)

    def json_file_list(self):
        """ get list of xml or compressed xml files """
        ext_list = ['json', 'gz', 'zip']
        flist = file_ext_list(self.opts.dir, ext_list)
        return flist
