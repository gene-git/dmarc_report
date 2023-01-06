# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 Routines to read various various xml report files.
"""
# pylint: disable=R0913, R0914

import os
import gzip
import zipfile
import datetime
import xml.etree.ElementTree as xml_et
from .utils import get_glob_file_list

def get_xml_from_zip(fname):
    """
    returns xml object
      input: fname = foo.xml.zip
      output: 'foo.xml' as xml object

    Sinze zip file can contain more than one file we return a list.
    All dmarc reports contain only a single file however and only use zip to compress.
    """
    # extract content into memory
    members = []
    with zipfile.ZipFile(fname, 'r') as zipobj:
        for member in zipobj.namelist():
            this_member = zipobj.read(member)
            this_xml = xml_et.fromstring(this_member)
            members.append(this_xml)

    return members

def get_xml_from_gz(fname):
    """
    returns xml object
        input fname = foo.xml.gz
        outpu return 'foo.xml' as xml
    """
    # extract content into memory
    xml = None
    with gzip.open(fname, 'rb') as fobj:
        this_member = fobj.read()
        xml = xml_et.fromstring(this_member)

    return xml

def get_xml_from_xml(fname):
    """
    returns xml object
        input fname = foo.xml
        output return xml
    """
    # extract content into memory
    xml_tree = xml_et.parse(fname)
    xml = xml_tree.getroot()

    return xml

def xml_pull_item(xml, what):
    """
    Extract 'what' from xml
    """
    text = "-"
    if xml:
        item = xml.find(what)
        if item is not None:
            text = item.text
            if not text:
                text = "-"
    return text

def xml_pull_date_range(metadata):
    """
    metadata should contain 'date_range' which in turn contains 'begin' and 'end'
    extract date range [start, end] as datetime objects
    """
    dstart = None
    dend = None
    date_range = metadata.find('date_range')
    if date_range is not None:
        begin = date_range.find('begin')
        if begin  is not None:
            start_secs = begin.text
            dstart = datetime.datetime.fromtimestamp(int(start_secs))
        end = date_range.find('end')
        if end is not None:
            end_secs = end.text
            dend = datetime.datetime.fromtimestamp(int(end_secs))

    drange = [dstart, dend]
    return drange

def xml_file_list(topdir):
    """
    Make list of xml files (plain or zip or gzip)
    Return dictionary containing list of files of each type
    """
    plain_files = get_glob_file_list(topdir, '*.xml')
    gzip_files = get_glob_file_list(topdir, '*.gz')
    zip_files = get_glob_file_list(topdir, '*.zip')

    xml_files = {
            'xml' : plain_files,
            'gzip' : gzip_files,
            'zip' : zip_files
            }
    return  xml_files

def xml_file_read(topdir, ftype, file):
    """
    Read file into xml - ftype is one of types retturned by xml_file_list():
      - xml, gz, zip
    Note that while zip may contain more than 1 file - all dmarc reports
    only use zip to compress single file.
    """
    fpath = os.path.join(topdir, file)
    match ftype:
        case 'xml':
            xml = get_xml_from_xml(fpath)

        case 'gzip':
            xml = get_xml_from_gz(fpath)

        case 'zip':
            xml_list = get_xml_from_zip(fpath)
            xml = xml_list[0]
            if len(xml_list) > 1:
                print('Warning zip compressed report has more than 1 report file - not exepcted')
    return  xml
