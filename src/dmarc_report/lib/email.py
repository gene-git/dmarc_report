"""
Handles exatrction of mime attachments
"""
import os
import email
from .utils import get_glob_file_list

def email_file_list(topdir):
    """
    return list of files ending in .eml in topdir
    """
    eml_list = get_glob_file_list(topdir, '*.eml')
    return eml_list

def email_extract_attachment(topdir, email_file, skip_exist=True):
    """
    extract mime attachment from email file
     - if attachment file exists we skip
    """

    email_path = os.path.join(topdir, email_file)
    email_str = None
    with open(email_path, 'r', encoding='UTF-8') as fobj:
        email_str = fobj.read()

    if email_str:
        mail = email.message_from_string(email_str)
        attach_fname = mail.get_filename()
        attach_path = os.path.join(topdir, attach_fname)
        if not (skip_exist and os.path.exists(attach_path)):
            with open(attach_path, 'wb') as fobj:
                fobj.write(mail.get_payload(decode=True))

def find_extract_email_attachments(topdir):
    """
    Get all filenames ending in .eml in topdir
    Extract mime attachment into same directory
    """

    eml_list = email_file_list(topdir)
    if not eml_list:
        return

    for eml in eml_list:
        email_extract_attachment(topdir, eml)
