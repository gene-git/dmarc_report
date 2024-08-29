# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
 Routines to read various various xml report files.
"""
# pylint: disable=c-extension-no-member

import os
import gzip
import zipfile
import datetime
from lxml import etree
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
            this_xml = etree.fromstring(this_member)
            if this_xml is not None:
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
        xml = etree.fromstring(this_member)
    return xml

def get_xml_from_xml(fname):
    """
    returns xml object
        input fname = foo.xml
        output return xml
    """
    # extract content into memory
    xml_tree = etree.parse(fname)
    xml = xml_tree.getroot()

    return xml

def _get_ns(xml):
    """
    return any ns
     - we create a dummy ns
     - we should find way to get actual name space and the name:value [, ... name:value]
    """
    ns = xml.nsmap
    #ns = None
    #if xml and xml.tag and xml.tag[0] == '{':
    #    ns = xml.tag[1:].split('}')[0]
    return ns

def xml_pull_node(xml, what):
    """
    Extract 'what' from xml
    """
    item = None
    if xml is not None:
        ns = _get_ns(xml)
        if ns:
            item = xml.find(what, ns)
        else:
            item = xml.find(what)

    return item

def xml_pull_item(xml, what):
    """
    Extract 'what' from xml
    """
    text = "-"
    if xml is not None:
        ns = _get_ns(xml)
        if ns:
            item = xml.find(what, ns)
        else:
            item = xml.find(what)

        if item is not None :
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
    ns = _get_ns(metadata)
    if ns:
        date_range = metadata.find('date_range', ns)
    else:
        date_range = metadata.find('date_range')
    if date_range is not None:
        begin = date_range.find('begin', ns)
        if begin  is not None:
            start_secs = begin.text
            dstart = datetime.datetime.fromtimestamp(int(start_secs))
        end = date_range.find('end', ns)
        if end is not None:
            end_secs = end.text
            dend = datetime.datetime.fromtimestamp(int(end_secs))

    drange = [dstart, dend]
    return drange

def xml_pull_records(xml):
    """
    Return list of records
    """
    ns = _get_ns(xml)
    if ns:
        records = xml.findall('record', ns)
    else:
        records = xml.findall('record')
    return records

def xml_pull_auth_results_dkims(xml):
    """
    Return list of auth_results/dkim
    """
    ns = _get_ns(xml)
    if ns:
        dkims = xml.findall('auth_results/dkim', ns)
    else:
        dkims = xml.findall('auth_results/dkim')
    return dkims

def xml_pull_auth_results_spf(xml):
    """
    Return auth_results/spf
    """
    ns = _get_ns(xml)
    if ns:
        spf = xml.find('auth_results/spf', ns)
    else:
        spf = xml.find('auth_results/spf')
    return spf

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

        case 'gz':
            xml = get_xml_from_gz(fpath)

        case 'zip':
            xml_list = get_xml_from_zip(fpath)
            xml = xml_list[0]
            if len(xml_list) > 1:
                print('Warning zip compressed report has more than 1 report file - not exepcted')
    return  xml
