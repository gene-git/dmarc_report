#!/usr/bin/python3
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
DMARC report generator:

read aggregate dmarc reports files in current directory (RUA)
and generate report. Files can be xml, zip or gzip xml.
"""
# pylint: disable=invalid-name
from dmarc_rpt.dmarc import DmarcReport
from dmarc_rpt.utils import xml_file_read
from dmarc_rpt.utils import find_extract_email_attachments


def main():
    """
    dmarc report tool
    """
    report = DmarcReport()
    topdir = report.opts.data.dir
    keep_eml = report.opts.data.keep

    # process any email files first (extract dmarc report attachments)
    find_extract_email_attachments(topdir, keep_eml)

    # returns dict of items ftype: file_list
    xml_files = report.xml_file_list()

    sep = 40*'-'
    for (ftype, files) in xml_files.items():
        for file in files:
            if report.opts.data.verb:
                print(f'{sep}')
                print(f' - {file}')
            xml = xml_file_read(topdir, ftype, file)
            report.analyze(xml)

    report.print()

    #
    # disposition of input files
    #
    report.input_disposition(xml_files)


# -----------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------- All Done ------------------------
