# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>
"""
Helper tools for dmarc report generator
"""
# pylint: disable=invalid-name
# Use IO since we dont know if open used for TextIO or BinaryIO
from typing import (Any, IO)
import os
import stat
import glob
import random
import string
from operator import itemgetter
from datetime import datetime


def drange_summary(drange_list: list[list[datetime]]) -> tuple[str, str, str]:
    """
    takes list of [start, end]
    returns earliest start and last end and
    whether range is contiguous by date.
    """
    start = '?'
    end = '?'
    contig = False
    contig_flag = ''

    # do something if faced with no dates
    fmt = '%y/%m/%d %H:%M'

    # handle missing dates in report

    drange_clean: list[list[datetime]] = []
    for item in drange_list:
        if not (item[0] and item[1]):
            continue
        drange_clean.append(item)

    if not drange_clean:
        return (start, end, contig_flag)

    # start
    num = len(drange_clean)
    dts = sorted(drange_clean, key=itemgetter(0))
    dstart: datetime = dts[0][0]
    dend: datetime = dts[num-1][1]

    if not (dstart and dend):
        return (start, end, '')

    fmt = '%y/%m/%d %H:%M'
    start = dstart.strftime(fmt)
    end = dend.strftime(fmt)
    # contig - we ignore time
    contig = True
    prev = dts[0]
    for idx in range(1, num):
        this = dts[idx]
        if this[0].date() == prev[1].date():
            prev = this
        else:
            contig = False
            break

    if not contig:
        contig_flag = '*'

    return (start, end, contig_flag)


def get_glob_file_list(topdir, pattern, withpath=False) -> list[str]:
    """
    gets list of files in topdir/pattern
      - returns filenames without topdir unless withpath=True
    """
    if topdir.endswith('/'):
        gpat = f'{topdir}{pattern}'
    else:
        gpat = f'{topdir}/{pattern}'

    flist = glob.glob(gpat)
    if not withpath:
        fnames = []
        for fpath in flist:
            file = os.path.basename(fpath)
            fnames.append(file)
        flist = fnames
    return flist


def open_file(path: str, mode: str) -> IO | None:
    """
     Open a file and return file object
    """
    # pylint: disable=W1514,R1732
    try:
        fobj = open(path, mode)
    except OSError as err:
        print(f'Error opening file {path}: {err}')
        fobj = None
    return fobj


def merge_dict(dic1: dict[str, Any], dic2: dict[str, Any]
               ) -> dict[str, Any]:
    """
    Merge dic2 over dic1 (dic2 overrides dic1)
    """
    if not dic1:
        return dic2
    if not dic2:
        return dic1

    merged = dic1.copy()
    for (key, val) in dic2.items():
        if key in merged:
            if isinstance(val, dict) and isinstance(merged[key], dict):
                merged[key] = merge_dict(merged[key], val)
            else:
                merged[key] = val
        else:
            merged[key] = val
    return merged


def make_dir_path(path_dir: str) -> bool:
    """
    makes directory and any missing path components
      - set reasonable permissions
    """
    okay = True
    dirmode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP
    dirmode |= stat.S_IROTH | stat.S_IXOTH
    try:
        os.makedirs(path_dir, exist_ok=True)
        os.chmod(path_dir, dirmode)
    except OSError as _error:
        okay = False
    return okay


def file_ext_list(topdir: str, ext_list: list[str]
                  ) -> dict[str, list[str]]:
    """
    Make dictionary of files with extensions in ext_list
    Return dictionary containing list of files of each extension type
    """
    fext_dict: dict[str, list[str]] = {}
    if not ext_list:
        return fext_dict

    for ext in ext_list:
        glob_pat = f'*.{ext}'
        files = get_glob_file_list(topdir, glob_pat)
        fext_dict[ext] = files

    return fext_dict


def random_ascii_name(num: int) -> str:
    """
    Return random string of length num

    Args:
        num (int)
        An integer of desired length of the string.
    Returns:
        str:
        A string of "num" random ASCII characters.
    """
    ascii_list = [random.choice(string.ascii_letters) for _ in range(num)]
    return ''.join(ascii_list)
