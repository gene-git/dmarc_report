# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>
"""
Helper tools for dmarc report generator
"""
# pylint: disable=invalid-name
import os
import stat
import glob
from operator import itemgetter

def drange_summary(drange_list):
    """
    takes list of [start, end]
    returns earliest start and last end and whether range is continuous by date.
    """
    start = '?'
    end = '?'
    contig = False

    # do something if faced with no dates
    fmt = '%y/%m/%d %H:%M'

    # handle missing dates in report

    drange_clean = []
    for item in drange_list:
        if not (item[0] and item[1]) :
            continue
        drange_clean.append(item)

    if not drange_clean:
        return (start, end, contig)

    # start
    num = len(drange_clean)

    dts = sorted (drange_clean, key=itemgetter(0))
    dstart = dts[0][0]
    dend = dts[num-1][1]

    if not (dstart and dend):
        return (start, end, True)

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

    contig_flag = ''
    if not contig :
        contig_flag = '*'

    return (start, end, contig_flag)

def get_glob_file_list(topdir, pattern, withpath=False):
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

def open_file(path, mode):
    """
     Open a file and return file object
    """
    # pylint: disable=W1514,R1732
    try:
        fobj = open(path, mode)
    except OSError as err:
        print(f'Error opening file {path} : {err}')
        fobj = None
    return fobj

def merge_dict(dic1, dic2):
    """
    Merge dic2 over dic1 (dic2 overrides dic1)
    """
    if not dic1:
        return dic2
    if not dic2:
        return dic1

    merged = dic1.copy()
    for (key,val) in dic2.items():
        if key in merged:
            if isinstance(val, dict) and isinstance(merged[key], dict):
                merged[key] = merge_dict(merged[key], val)
            else:
                merged[key] = val
        else:
            merged[key] = val
    return merged

def make_dir_path(path_dir):
    """
    makes directory and any missing path components
      - set reasonable permissions
    """
    okay = True
    dirmode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
    try:
        os.makedirs(path_dir, exist_ok=True)
        os.chmod(path_dir, dirmode)
    except OSError as _error:
        okay = False
    return okay

def file_ext_list(topdir, ext_list):
    """
    Make dictionary of files with extensions in ext_list
    Return dictionary containing list of files of each extension type
    """
    fext_dict = {}
    if not ext_list:
        return fext_dict

    for ext in ext_list:
        glob_pat = f'*.{ext}'
        files = get_glob_file_list(topdir, glob_pat)
        fext_dict[ext] = files

    return fext_dict
