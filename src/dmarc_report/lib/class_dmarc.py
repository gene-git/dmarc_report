# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
Report Class DmarcRpt
"""
# pylint: disable=invalid-name,too-many-instance-attributes
# pylint: disable=too-few-public-methods

from py_cidr import (Cidr)
from .dmarc_analyze import dmarc_analyze
from .class_options import DmarcOpts
from .report import print_report
from .class_print import Prnt
from .save_input_files import input_files_disposition
from .utils import file_ext_list

class IPRpt:
    """
    Basic Report Information for one IP address
    """
    def __init__(self):
        self.ip = None
        self.cnt = 0
        self.dmarc_pass = 0
        self.dmarc_fail = 0
        self.dkim_policy_pass = 0
        self.spf_policy_pass = 0
        self.spf_auth_pass = 0
        self.spf_auth_fail = 0
        self.dkim_auth_pass = 0
        self.dkim_auth_fail = 0
        self.dkim_selectors = []      # short selector name

    def add_selector(self, sel_name):
        """ add if dont have """
        if sel_name not in self.dkim_selectors:
            self.dkim_selectors.append(sel_name)

class DomRpt:
    """
    Report Class for one domain reported by an org
    """
    def __init__(self, domain):
        self.domain = domain
        self.total = IPRpt()
        self.ip_rpt = {}                # dict of IPRpts keyed by IP
        self.selectors = []
        self.drange = []

    def add_drange(self, drange):
        """ add drange to list """
        self.drange.append(drange)

    def get_ip_rpt(self, ip):
        """ return IPRpt for ip """
        ip_rpt = self.ip_rpt.get(ip)
        if not ip_rpt:
            ip_rpt = IPRpt()
            self.ip_rpt[ip] = ip_rpt
        return ip_rpt

    def get_num_ips(self):
        """ number of unique ips """
        num_ips = len(self.ip_rpt)
        return num_ips


class OrgRpt:
    """
    Report Class for one reporting org
    """
    def __init__(self, name):
        self.name = name
        self.total = IPRpt()
        self.drange = []            # list of [begin, end] from this org
        self.domain = []            # list of Domain Reports from this org

    def add_drange(self, drange):
        """ add drange to list """
        self.drange.append(drange)

    def get_domain(self, domain):
        """ return domain rpt """
        dom_rpt = None
        for dom in self.domain:
            if dom.domain == domain:
                dom_rpt = dom
                break
        if not dom_rpt:
            dom_rpt = DomRpt(domain)
            self.domain.append(dom_rpt)
        return dom_rpt

    def get_num_domains(self):
        """ number of separate domains for this org """
        num_doms = len(self.domain)
        return num_doms

    def get_num_ips(self):
        """ total number ips across all domains reported by this org """
        num_ips = 0
        for dom in self.domain:
            num_ips += dom.get_num_ips()
        return num_ips

class SelItem:
    """ each selector has short name """
    def __init__(self, domain, sel_domain, sel_name):
        self.domain = domain            # email report domain
        self.name = sel_name
        self.short = ''
        self.passes = 0
        self.fails = 0
        self.sel_domain = [sel_domain]  # forwarded email from sel_domain/selector
        self.cnt = {sel_domain : 0}

class SelMap:
    """ track selector names and counts thereof """
    def __init__(self):
        self.selectors = []

    def next_short(self):
        """ return next short name """
        cnt = 1 + len(self.selectors)
        short = f's{cnt}'
        return short

    def get_sel(self, domain, sel_domain, sel_name, cnt):
        """ return sel item for domain and selector name """
        sel = None
        for this_sel in self.selectors:
            if this_sel.name == sel_name : #and this_sel.domain == domain) :
                sel = this_sel
                if sel_domain not in sel.sel_domain:
                    sel.sel_domain.append(sel_domain)
                    sel.cnt[sel_domain] =  0
                break

        if not sel:
            sel = SelItem(domain, sel_domain, sel_name)
            sel.short = self.next_short()
            self.selectors.append(sel)
        sel.cnt[sel_domain] += cnt
        return sel

class DmarcRpt:
    """
    Top level Report Class
    """
    def __init__(self):

        self.opts = DmarcOpts()
        self.org = []               # list of orgs

        self.total = IPRpt()      # aggregate report
        self.drange = []            # list of [start,end]

        self.selectors = []         # list of selectors encountered
        self.sel_map = SelMap()

        self.dom_nets = Cidr.cidrs_to_nets(self.opts.dom_ips)
        self.prnt = Prnt(self.opts.theme)

    def get_num_orgs(self):
        """ returns num of org """
        num_orgs = len(self.org)
        return num_orgs

    def get_org(self, org_name):
        """ get org for org_name if have it"""
        org = None
        for this_org in self.org:
            if this_org.name == org_name:
                org = this_org
                break
        if not org:
            org = OrgRpt(org_name)
            self.org.append(org)
        return org

    def ip_in_dom_ips(self, ip_str):
        """ check if ip is one of dom_ips """
        return Cidr.cidr_is_subnet(ip_str, self.dom_nets)

    def add_drange(self, drange):
        """
        add drange to list u
          - do we need this - we can always derive it from org.drange ?
        """
        self.drange.append(drange)

    def analyze(self, xml):
        """
        Analyze xml and add to report
        """
        dmarc_analyze(self, xml)

    def get_sel(self, domain, sel_domain, sel_name, cnt):
        """ get selector info for 'name' """
        return self.sel_map.get_sel(domain, sel_domain, sel_name, cnt)

    def print(self):
        """ print the report """
        print_report(self)

    def input_disposition(self, xml_files):
        """ handle disposition of all input files """
        input_files_disposition(self.opts, self.prnt, xml_files)

    def xml_file_list(self):
        """ get list of xml or compressed xml files """
        ext_list = ['xml', 'gz', 'zip']
        flist = file_ext_list(self.opts.dir, ext_list)
        return flist
