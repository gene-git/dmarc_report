# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 MTA-STS TLS Report Class
"""
# pylint: disable=too-few-public-methods
from utils import Conf
from utils import Prnt

from .class_tlsrpt import TlsReports


class TlsRpt:
    """
    Report class for TLS reports.

    includes tlsa and mta-sts
    """
    def __init__(self):
        self.opts = Conf('tls')

        self.reports = TlsReports()
        self.prnt = Prnt(self.opts.data.theme)
