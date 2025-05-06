# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
Handles exatrction of mime attachments
"""
from typing import (List)
import os
import email
import mimetypes
from .tools import random_ascii_name
from .tools import get_glob_file_list


def email_file_list(topdir: str) -> List[str]:
    """
    Return list of files ending in .eml in topdir.
    """
    eml_list = get_glob_file_list(topdir, '*.eml')
    return eml_list


def mbox_file_list(topdir: str) -> List[str]:
    """
    Return list of files ending in .mbox in topdir.
    """
    mbox_list = get_glob_file_list(topdir, '*.mbox')
    return mbox_list


def email_data_extract_attachment(topdir: str, email_str: str,
                                  skip_exist=True):
    """
    Extract mime attach from mail string.
    """
    if not email_str:
        return

    mail = email.message_from_string(email_str)

    # handle multipart
    if mail.is_multipart():
        counter = 1
        for part in mail.walk():
            # multipart/* are just containers
            cmtype = part.get_content_maintype()
            if cmtype in ['multipart', 'text', 'html']:
                continue

            #
            # Applications should really sanitize the given filename so that an
            # email message can't be used to overwrite important files
            #
            attach_fname = part.get_filename()
            if not attach_fname:
                ext = mimetypes.guess_extension(part.get_content_type())
                if not ext:
                    # Use a generic bag-of-bits extension
                    ext = '.bin'
                attach_fname = f'part-{counter:03d}{ext}'

                # skip txt, html and bin
                if ext in ['.txt', '.html', '.bin']:
                    continue

            counter += 1
            attach_path = os.path.join(topdir, attach_fname)
            if not (skip_exist and os.path.exists(attach_path)):
                with open(attach_path, 'wb') as fobj:
                    data = bytes(part.get_payload(decode=True))
                    fobj.write(data)

    else:
        attach_fname = mail.get_filename()
        if not attach_fname:
            attach_fname = random_ascii_name(6)

        attach_path = os.path.join(topdir, attach_fname)
        if not (skip_exist and os.path.exists(attach_path)):
            with open(attach_path, 'wb') as fobj:
                data = bytes(mail.get_payload(decode=True))
                fobj.write(data)


def eml_extract_attachment(topdir: str, email_file: str,
                           keep_email: bool, skip_exist=True):
    """
    extract mime attachment from email file
     - if attachment file exists we skip
    """
    email_path = os.path.join(topdir, email_file)
    email_str = None
    if not os.path.exists(email_path):
        return

    with open(email_path, 'r', encoding='UTF-8') as fobj:
        email_str = fobj.read()

    if email_str:
        email_data_extract_attachment(topdir, email_str, skip_exist)

    if not keep_email:
        os.unlink(email_path)


def mbox_extract_attachments(topdir: str, mbox: str,
                             keep_email: bool, skip_exist: bool = True):
    """
    Extract attachments from mbox file
      each email starts with "From " and ends wiht blank line
    """
    mbox_path = os.path.join(topdir, mbox)
    if not os.path.exists(mbox_path):
        return

    with open(mbox_path, 'r', encoding='UTF-8') as fobj:
        data = fobj.read()

    if not data:
        return

    data_rows = data.splitlines()
    email_str = ''
    for row in data_rows:
        if row.startswith('From '):
            if email_str != '':
                email_data_extract_attachment(topdir, email_str, skip_exist)
            email_str = row + '\n'
        else:
            email_str += row + '\n'

    if email_str:
        email_data_extract_attachment(topdir, email_str, skip_exist)

    if not keep_email:
        os.unlink(mbox_path)


def find_extract_email_attachments(topdir: str, keep_email: bool):
    """
    Get all filenames ending in .eml in topdir
    Extract mime attachment into same directory
    """
    eml_list = email_file_list(topdir)
    mbox_list = mbox_file_list(topdir)

    if not (eml_list or mbox_list):
        return

    for eml in eml_list:
        eml_extract_attachment(topdir, eml, keep_email)

    for mbox in mbox_list:
        mbox_extract_attachments(topdir, mbox, keep_email)
