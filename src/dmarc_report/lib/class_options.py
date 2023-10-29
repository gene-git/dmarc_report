# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 DMARC report options
"""
# pylint: disable=too-many-instance-attributes,too-few-public-methods
# pylint: disable=R0801

import os
import argparse
from .config import read_configs

def config_opts(opts):
    """ read configs into options """
    conf = read_configs(opts, 'dmarc')
    if conf:
        for (key,val) in conf.items():
            setattr(opts, key, val)


class DmarcOpts:
    """ cmmand line options """

    def __init__(self):
        self.verb = False
        self.dmarc_fails = False
        self.dkim_fails = False
        self.spf_fails = False
        self.keep = False
        self.dir = './'
        self.theme = 'dark'
        self.dom_ips = None
        self.inp_files_disp = 'none'      # None, 'delete', 'save' (uses inp_files_save_dir)
        self.inp_files_save_dir = None    # e.g relative to self.dir, or absolute

        # load configs
        config_opts(self)

        # expand any "~"
        self.dir = os.path.expanduser(self.dir)

        par = argparse.ArgumentParser(description='dmarc-rpt')
        par.add_argument('-v','--verb',
                         action = 'store_true',
                         help='More verbose')

        par.add_argument('-k','--keep',
                         action = 'store_true',
                         help='Keep .eml files after extracting mime attachment (False)')

        par.add_argument('-ips','--dom_ips',
                         help='Comma separated list of IPs / CIDRs for your own domains')

        par.add_argument('-d','--dir',
                         default = self.dir,
                         help=f'Directory containing dmarc report files (default {self.dir})')

        par.add_argument('-ifd','--inp_files_disp',
                         default = self.inp_files_disp,
                         help='none,delete,save: disposition of input files. See -ifsd  (none)')

        par.add_argument('-ifsd','--inp_files_save_dir',
                         default = self.inp_files_save_dir,
                         help=f'-ifd = save, input files moved to here {self.inp_files_save_dir}')

        par.add_argument('-thm','--theme',
                         default = self.theme,
                         help=f'Set color theme : dark, light, none (default {self.theme})')

        par.add_argument('-fdm','--dmarc_fails',
                         action = 'store_true',
                         help='Only report dmarc fails')

        par.add_argument('-fdk','--dkim_fails',
                         action = 'store_true',
                         help='Only report dkim fails')

        par.add_argument('-fsp','--spf_fails',
                         action = 'store_true',
                         help='Only report spf fails')

        parsed = par.parse_args()
        if parsed:
            for (opt,val) in vars(parsed).items() :
                if opt == 'dom_ips' :
                    if val is None:
                        continue
                    val = val.split(',')
                setattr(self, opt, val)

        # color turned off when theme is None
        if self.theme and self.theme.lower() == 'none':
            self.theme = None
