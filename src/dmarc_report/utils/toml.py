# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>
"""
toml support
 - toml reader is native to 3.11+
"""
from typing import (Any)
import os
import tomllib as toml
from .tools import open_file


def read_toml_file(fpath) -> dict[str, Any]:
    """
    read toml file and return a dictionary
    """
    this_dict: dict[str, Any] = {}
    if os.path.exists(fpath):
        fobj = open_file(fpath, 'r')
        if fobj:
            data = fobj.read()
            fobj.close()
            this_dict = toml.loads(data)
    return this_dict
