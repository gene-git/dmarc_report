# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
Read options from config files:
    1) /etc/dmarc_report/config
    2) ~/.config/dmarc_options/config
"""
import os
from pathlib import Path
from .toml import read_toml_file
from .utils import merge_dict

def read_configs(_opts, app):
    """
    Read any config settings
     - app is one of: dmarc, tls
     - /etc/dmarc_report/config
     - ~/.config/dmarc_report/config
    """
    config = None
    tool = 'dmarc_report'
    home = str(Path.home())
    if app == 'tls':
        conf_file = 'tls-config'
    else:
        conf_file = 'config'
    confs = [f'/etc/{tool}/{conf_file}', f'{home}/.config/{tool}/{conf_file}']

    for conf in confs:
        if os.path.exists(conf) and os.access(conf, os.R_OK):
            this_conf = read_toml_file(conf)

            if not config:
                config = this_conf
            else:
                config = merge_dict(config, this_conf)

    return config
