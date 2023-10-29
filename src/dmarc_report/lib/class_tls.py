# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 MTA-STS TLS Report Class
"""
# pylint: disable=R0903
from .class_tls_options import TlsOpts
from .class_tlsrpt import TlsReports
from .tls_report_generate import generate_tls_report
from .tls_update import tls_update_reports
from .tls_analyze import tls_analyze_one
from .class_print import Prnt
from .save_input_files import input_files_disposition
from .utils import file_ext_list

class TlsRpt:
    """
    Report class for TLS reports
     - includes tlsa and mta-sts
    """
    def __init__(self):
        self.opts = TlsOpts()

        self.reports = TlsReports()
        self.prnt = Prnt(self.opts.theme)

    def analyze(self, one_json):
        """
        Analyze one json report and add to report
        """
        one_rpt = tls_analyze_one(one_json)
        tls_update_reports(one_rpt, self.reports)

    def print(self):
        """ print the report """
        generate_tls_report(self)

    def input_disposition(self, json_files):
        """ handle disposition of all input files """
        input_files_disposition(self.opts, self.prnt, json_files)

    def json_file_list(self):
        """ get list of xml or compressed xml files """
        ext_list = ['json', 'gz', 'zip']
        flist = file_ext_list(self.opts.dir, ext_list)
        return flist
