"""
Handles exatrction of mime attachments
"""
import os
import email
import mimetypes
from .utils import get_glob_file_list

def email_file_list(topdir):
    """
    return list of files ending in .eml in topdir
    """
    eml_list = get_glob_file_list(topdir, '*.eml')
    return eml_list

def email_extract_attachment(topdir, email_file, keep_email, skip_exist=True):
    """
    extract mime attachment from email file
     - if attachment file exists we skip
    """

    email_path = os.path.join(topdir, email_file)
    email_str = None
    if os.path.exists(email_path):
        with open(email_path, 'r', encoding='UTF-8') as fobj:
            email_str = fobj.read()

    if email_str:
        mail = email.message_from_string(email_str)

        # handle multipart
        if mail.is_multipart():
            counter = 1
            for part in mail.walk():
                # multipart/* are just containers
                cmtype = part.get_content_maintype()
                if cmtype in  ['multipart', 'text', 'html']:
                    continue
                # Applications should really sanitize the given filename so that an
                # email message can't be used to overwrite important files
                attach_fname = part.get_filename()
                if not attach_fname:
                    ext = mimetypes.guess_extension(part.get_content_type())
                    if not ext:
                        # Use a generic bag-of-bits extension
                        ext = '.bin'
                    attach_fname = f'part-{counter:03d}{ext}'

                    # skip txt, html and bin
                    if ext in ['.txt', '.html', '.bin'] :
                        continue

                counter += 1
                attach_path = os.path.join(topdir, attach_fname)
                if not (skip_exist and os.path.exists(attach_path)):
                    with open(attach_path, 'wb') as fobj:
                        fobj.write(part.get_payload(decode=True))

        else:
            attach_fname = mail.get_filename()
            attach_path = os.path.join(topdir, attach_fname)
            if not (skip_exist and os.path.exists(attach_path)):
                with open(attach_path, 'wb') as fobj:
                    fobj.write(mail.get_payload(decode=True))
        if not keep_email:
            os.unlink(email_path)

def find_extract_email_attachments(topdir, keep_email):
    """
    Get all filenames ending in .eml in topdir
    Extract mime attachment into same directory
    """

    eml_list = email_file_list(topdir)
    if not eml_list:
        return

    for eml in eml_list:
        email_extract_attachment(topdir, eml, keep_email)
