#!/usr/bin/python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 TLS report generator:
   read tlsreport reports files and generate human readable report.
   Files can be json or zip or gzip json.
"""
# pylint: disable=invalid-name
from lib import TlsRpt
from lib import find_extract_email_attachments
from lib import json_file_read

def main():
    """
    dmarc report tool
    """
    report = TlsRpt()
    topdir = report.opts.data.dir
    keep_eml = report.opts.data.keep

    # process any email files first (extract tls report attachments)
    find_extract_email_attachments(topdir, keep_eml)

    json_files = report.json_file_list()

    sep = 40*'-'
    for (ftype, files) in json_files.items():
        for file in files:
            if report.opts.data.verb:
                print(f'{sep}')
                print (f' - {file}')
            json = json_file_read(topdir, ftype, file)
            report.analyze(json)

    report.print()
    report.input_disposition(json_files)

# -----------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------- All Done ------------------------
