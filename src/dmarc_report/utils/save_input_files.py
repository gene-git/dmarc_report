# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 disposition of all input files
"""
import os
from datetime import datetime

from .email import email_file_list
from .tools import make_dir_path
from .class_options import (ConfData)
from .class_print import Prnt


def input_files_disposition(opts: ConfData, pcls: Prnt,
                            ftyp_files: dict[str, list[str]]):
    """
    inp_files_disp:

    - none        = do nothing
    - delete      = remove them
    - save        = move/save into inp_files_save_dir

    Args:
        opts (ConfData):
        Config options data class.

        prnt (Prnt):
        print function with asccii color escapes.

        ftyp_files (dict[str, list[str]]:
        list of files for each file type in the dictionary for each of
        [xml, gzip, zip].

    """
    prnt = pcls.prnt

    #
    # If no User request, return
    #
    if opts.inp_files_disp is None or opts.inp_files_disp == 'none':
        return

    delete_files = False
    save_files = False
    disp = opts.inp_files_disp
    if disp.startswith('del') or disp.startswith('rem'):
        delete_files = True

    elif disp.startswith('sav'):
        save_files = True
        save_dir = opts.inp_files_save_dir
        if not save_dir:
            prnt('Warning: ', fg_col='warn')
            prnt('to save inputs need --inp_files_save_dir\n')
            save_files = False

    #
    # anything to do?
    #
    if not (delete_files or save_files):
        return

    #
    # Make list of input files
    #
    files = []
    for (_ftype, flist) in ftyp_files.items():
        if flist:
            files += flist

    # Add .eml files if being kept
    if opts.keep:
        eml_files = email_file_list(opts.dir)
        files = files + eml_files

    if not files:
        return

    if save_files:
        save_input_files(opts, pcls, files)

    elif delete_files:
        delete_input_files(opts, pcls, files)


def save_subdir() -> str:
    """ Save input files in subdir based on date """
    today = datetime.today()
    year = today.year
    month = today.month
    subdir = f'{year:d}-{month:02d}'
    return subdir


def save_input_files(opts: ConfData, pcls: Prnt, files: list[str]):
    """ save nput files """
    if not files:
        return

    prnt = pcls.prnt
    #
    # set up dir - handle relative and absolute names
    #
    topdir = opts.dir
    save_dir = opts.inp_files_save_dir
    subdir = save_subdir()

    if os.path.isabs(save_dir):
        save_dir = os.path.join(save_dir, subdir)
    else:
        save_dir = os.path.join(topdir, save_dir, subdir)

    save_dir = os.path.normpath(save_dir)

    if not os.path.exists(save_dir):
        okay = make_dir_path(save_dir)
        if not okay:
            prnt('Error: ', fg_col='error')
            prnt(f'making save dir : {save_dir}\n')
            return

    for file in files:
        fpath = os.path.join(topdir, file)
        dest_path = os.path.join(save_dir, file)
        try:
            os.rename(fpath, dest_path)
        except OSError as err:
            prnt(f'Error {err}: ', fg_col='error')
            prnt(f'moving file {file}: {save_dir}\n')


def delete_input_files(opts: ConfData, pcls: Prnt, files: list[str]):
    """ remove nput files """

    if not files:
        return
    topdir = opts.dir
    prnt = pcls.prnt

    for file in files:
        fpath = os.path.join(topdir, file)
        if os.path.exists(fpath):
            try:
                os.unlink(fpath)
            except OSError as err:
                prnt(f'Error {err}: ', fg_col='error')
                prnt(f'removing file {file}\n')
