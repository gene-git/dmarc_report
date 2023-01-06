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

def read_configs(_opts):
    """
    Read any config settings
     - /etc/dmarc_report/config
     - ~/.config/dmarc_report/config
    """
    config = None
    app = 'dmarc_report'
    home = str(Path.home())
    confs = [f'/etc/{app}/config', f'{home}/.config/{app}/config']

    for conf in confs:
        if os.path.exists(conf) and os.access(conf, os.R_OK):
            this_conf = read_toml_file(conf)

            if not config:
                config = this_conf
            else:
                config = merge_dict(config, this_conf)

    return config
