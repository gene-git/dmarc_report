#!/usr/bin/python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 TLS report generator:
   read tlsreport reports files and generate human readable report.
   Files can be json or zip or gzip json.
"""
# pylint: disable=invalid-name
from lib import TlsRpt
from lib import find_extract_email_attachments
from lib import json_file_read

#import pdb

def main():
    """
    dmarc report tool
    """
    #pdb.set_trace()
    report = TlsRpt()
    topdir = report.opts.dir
    keep_eml = report.opts.keep

    # process any email files first (extract tls report attachments)
    find_extract_email_attachments(topdir, keep_eml)

    json_files = report.json_file_list()

    sep = 40*'-'
    for (ftype, files) in json_files.items():
        for file in files:
            if report.opts.verb:
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
