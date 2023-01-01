#!/usr/bin/python3
"""
 DMARC report generator:
   read aggregate dmarc reports files in current directory (RUA) and generate report.
   Files can be xml or zip or gzip xml.
"""
# pylint: disable=R0913, R0914

#import pdb
from lib import DmarcRpt
from lib import xml_file_list
from lib import xml_file_read

def main():
    """
    dmarc report tool
    """
    #pdb.set_trace()
    report = DmarcRpt()

    # returns dict of items ftype: file_list
    xml_files = xml_file_list()

    sep = 40*'-'
    for (ftype, files) in xml_files.items():
        for file in files:
            if report.opts.verb:
                print(f'{sep}')
                print (f' - {file}')
            xml = xml_file_read(ftype, file)
            report.make_report(xml)

    report.print()

# -----------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------- All Done ------------------------
