# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
Class DmarcRpt

Keep all methods with separate helper functions in
subclass. This allows us to organize the code
without the dreaded "circular" dependency when helper
imports the class.
"""
# pylint: disable=invalid-name,too-many-instance-attributes
# pylint: disable=too-few-public-methods

from ._class_dmarc import (IPRpt, DomRpt, OrgRpt, DmarcRpt)
from .dmarc_analyze import dmarc_analyze
from .report import print_report


class IPReport(IPRpt):
    """
    Basic Report Information for one IP address
    """


class DomReport(DomRpt):
    """
    Report Class for one domain reported by an org
    """


class OrgReport(OrgRpt):
    """
    Report Class for one reporting org
    """


class DmarcReport(DmarcRpt):
    """
    Top level Report Class
    """
    def analyze(self, xml):
        """
        Analyze xml and add to report
        """
        dmarc_analyze(self, xml)

    def print(self):
        """ print the report """
        print_report(self)
