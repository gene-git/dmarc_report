#!/usr/bin/python3
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
TLS report generator:

read tlsreport reports files and generate human readable report.
Files can be json or zip or gzip json.
"""
# pylint: disable=invalid-name
from dmarc_rpt.tls import TlsReport
from dmarc_rpt.utils import find_extract_email_attachments
from dmarc_rpt.utils import json_file_read


def main():
    """
    dmarc report tool
    """
    report = TlsReport()
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
                print(f' - {file}')
            json = json_file_read(topdir, ftype, file)
            if json:
                report.analyze(json)

    report.print()
    report.input_disposition(json_files)


# -----------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------- All Done ------------------------
