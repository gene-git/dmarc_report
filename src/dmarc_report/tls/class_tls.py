# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 MTA-STS TLS Report Class
"""
from utils import file_ext_list
from utils import input_files_disposition

from ._class_tls import TlsRpt
from .tls_report_generate import generate_tls_report
from .tls_update import tls_update_reports
from .tls_analyze import tls_analyze_one


class TlsReport(TlsRpt):
    """
    Report class for TLS reports.

    includes tlsa and mta-sts
    """
    def analyze(self, one_json):
        """
        Analyze one json report and add to report
        """
        one_rpt = tls_analyze_one(one_json)
        tls_update_reports(one_rpt, self.reports)

    def print(self):
        """ print the report """
        generate_tls_report(self)

    def input_disposition(self, json_files: dict[str, list[str]]):
        """ handle disposition of all input files """
        input_files_disposition(self.opts.data, self.prnt, json_files)

    def json_file_list(self) -> dict[str, list[str]]:
        """ get list of xml or compressed xml files """
        ext_list = ['json', 'gz', 'zip']
        flist = file_ext_list(self.opts.data.dir, ext_list)
        return flist
