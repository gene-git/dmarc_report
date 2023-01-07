# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 disposition of all input files
"""
import os
from datetime import datetime

from .email import email_file_list
from .utils import make_dir_path

def input_files_disposition(opts, prnt, ftyp_files):
    """
    inp_files_disp:
        none        = do nothing
        delete      = remove them
        save        = move/save into inp_files_save_dir
    """

    #
    # If no User request, return
    #
    if opts.inp_files_disp is None or opts.inp_files_disp == 'none':
        return

    delete_files = False
    save_files = False
    if opts.inp_files_disp.startswith('del') or opts.inp_files_disp.startswith('rem'):
        delete_files = True
    elif opts.inp_files_disp.startswith('sav'):
        save_files = True
        save_dir = opts.inp_files_save_dir
        if not save_dir:
            prnt('Warning: ', fg_col='warn')
            prnt('to save inputs --inp_files_save_dir must provide directory\n')
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
        save_input_files(opts, prnt, files)

    elif delete_files:
        delete_input_files(opts, prnt, files)

def save_subdir():
    """ Save input files in subdir based on date """
    today = datetime.today()
    year = today.year
    month = today.month
    subdir = f'{year:d}-{month:02d}'
    return subdir

def save_input_files(opts, prnt, files):
    """ save nput files """
    if not files:
        return

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

def delete_input_files(opts, prnt, files):
    """ remove nput files """

    if not files:
        return

    topdir = opts.dir
    for file in files:
        fpath = os.path.join(topdir, file)
        if os.path.exists(fpath):
            try :
                os.unlink(fpath)
            except OSError as err:
                prnt(f'Error {err}: ', fg_col='error')
                prnt(f'removing file {file}\n')
