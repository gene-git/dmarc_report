# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 DMARC / TLS report options
"""
# pylint: disable=too-many-instance-attributes,too-few-public-methods
# pylint: disable=
from dataclasses import dataclass, field
from typing import List

import os
import argparse
from .config import read_config

@dataclass
class ConfData:
    '''
    config options
     - for both dmarc and tls
    '''
    verb : bool = False
    keep : bool = False
    dir : str = './'
    theme : str = 'dark'
    inp_files_disp : str = 'none'
    inp_files_save_dir : str = None

    dom_ips : List[str] = field(default_factory=list)
    dmarc_fails : bool = False
    dkim_fails : bool = False
    spf_fails : bool = False

class Conf:
    """ cmmand line options """

    def __init__(self, app:str):
        self.okay : bool = True
        self.app = app      # 'dmarc' or 'tls'

        self.data : ConfData         # app determines if dmarc or tls config section used.

        if app not in ('dmarc', 'tls'):
            print(f' Error: invalid app : {app}')
            self.okay = False
            return

        #
        # load config file
        #
        get_config_opts(self, app)

        #
        # Command line options
        #
        par = argparse.ArgumentParser(description='dmarc-rpt')
        opts = available_options(self, app)
        for opt in opts:
            (opt_s, opt_l), kwargs = opt
            if opt_l :
                par.add_argument(opt_s, opt_l, **kwargs)
            else:
                par.add_argument(opt_s, **kwargs)

        parsed = par.parse_args()
        if parsed:
            for (opt,val) in vars(parsed).items() :
                if opt == 'dom_ips' :
                    if not val :
                        continue
                    if isinstance(val, str):
                        val = val.split(',')
                setattr(self.data, opt, val)

        if self.data.dir:
            # expand any "~"
            self.data.dir = os.path.expanduser(self.data.dir)
            self.data.dir = os.path.abspath(self.data.dir)

        # color turned off when theme is None
        if self.data.theme and self.data.theme.lower() == 'none':
            self.data.theme = None

def get_config_opts(conf:Conf, app:str) :
    """ 
    read configs into options
    Read global section - for dmarc merge dmarc section or for tls merge the tls section
    """
    conf.data = ConfData()
    conf_dict = read_config()
    if conf_dict:
        conf_global = conf_dict.get('global')
        if conf_global:
            for (key,val) in conf_global.items():
                setattr(conf.data, key, val)

        conf_dmarc = conf_dict.get('dmarc')
        if app == 'dmarc' and conf_dmarc:
            for (key,val) in conf_dmarc.items():
                setattr(conf.data, key, val)

        conf_tls = conf_dict.get('tls')
        if app == 'tls' and conf_tls:
            for (key,val) in conf_tls.items():
                setattr(conf.data, key, val)

        if conf.data.dir:
            # expand any "~"
            conf.data.dir = os.path.expanduser(conf.data.dir)

def available_options(conf:Conf, app:str):
    '''
    Command line options
        app is 'dmarc' or 'tls'
        set defaults to current values in conf.data which are either defaults
        or read from config files.
        This way config file sets values and command line options can override
    '''
    data = conf.data

    opts = []
    act = 'action'
    act_on = 'store_true'

    value = data.verb
    ohelp = 'Be more verbose'
    opt = [('-v','--verb'), {'help' : ohelp, act : act_on, 'default':value}]
    opts.append(opt)

    value = data.keep
    ohelp = f'Keep .eml files after extracting mime attachment ({value})'
    opt = [('-k','--keep'), {'help' : ohelp, act : act_on, 'default': value}]
    opts.append(opt)

    directory = os.path.expanduser(conf.data.dir)
    ohelp = f'Directory containing dmarc report files ({directory})'
    opt = [('-d','--dir'), {'help' : ohelp, 'default': directory}]
    opts.append(opt)

    value = data.inp_files_disp
    ohelp = f'none,delete,save: disposition of input files. See -ifsd ({value})'
    opt = [('-ifd','--inp_files_disp'), {'help' : ohelp, 'default': value}]
    opts.append(opt)

    value = data.inp_files_save_dir
    ohelp = f'When -ifd is save, input files moved here afer report ({value})'
    opt = [('-ifsd','--inp_files_save_dir'), {'help' : ohelp, 'default': value }]
    opts.append(opt)

    value = data.theme
    ohelp = f'Set color theme : dark, light, none ({value})'
    opt = [('-thm','--theme'), {'help' : ohelp, 'default': value}]
    opts.append(opt)

    #
    # DMARC Only
    #
    if app == 'dmarc':
        value = data.dom_ips
        ohelp = 'Comma separated list of IPs / CIDRs for your own domains'
        opt = [('-ips','--dom_ips'), {'help' : ohelp, 'default' :value}]
        opts.append(opt)

        value = data.dmarc_fails
        ohelp = 'DMARC Report - limit to failures'
        opt = [('-fdm','--dmarc_fails'), {'help' : ohelp, act : act_on, 'default': value}]
        opts.append(opt)

        value = data.dkim_fails
        ohelp = 'DKIM Report  - limit to failures'
        opt = [('-fdk','--dkim_fails'), {'help' : ohelp, act : act_on, 'default': value}]
        opts.append(opt)

        value = data.spf_fails
        ohelp = 'SPF Report  - limit to failures'
        opt = [('-fsp','--spf_fails'), {'help' : ohelp, act : act_on, 'default': value}]
        opts.append(opt)

    #
    # TLS Only
    #
    # if app == 'tls':

    #
    # Sort options alphabetically
    #   - All option keys must be valid strings ("short", "long")
    #
    opts.sort(key = lambda item : item[0][1])

    #
    # Any positional args go here
    #

    return opts
