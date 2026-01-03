# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>
"""
 Routines to read various various xml report files.
"""
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module         # ELement is cython
# mypy: disable-error-code=import-untyped
from typing import (Any)
import os
import gzip
import zipfile
from datetime import datetime
from lxml import etree
from lxml.etree import Element      # type: ignore


def get_xml_from_zip(fname: str) -> list[Element]:
    """
    returns xml object.
      input: fname = foo.xml.zip
      output: 'foo.xml' as xml object

    Sinze zip file can contain more than one file we return a list.
    All dmarc reports contain only a single file however and
    only use zip to compress.
    """
    # extract content into memory
    members: list[Any] = []
    with zipfile.ZipFile(fname, 'r') as zipobj:
        for member in zipobj.namelist():
            this_member = zipobj.read(member)
            this_xml = etree.fromstring(this_member)
            if this_xml is not None:
                members.append(this_xml)
    return members


def get_xml_from_gz(fname: str) -> Element:
    """
    returns xml object
        input fname = foo.xml.gz
        outpu return 'foo.xml' as xml
    """
    # extract content into memory
    xml: Element = None
    with gzip.open(fname, 'rb') as fobj:
        this_member = fobj.read()
        xml = etree.fromstring(this_member)
    return xml


def get_xml_from_xml(fname: str) -> Element:
    """
    returns xml object
        input fname = foo.xml
        output return xml
    """
    # extract content into memory
    xml_tree = etree.parse(fname)
    xml = xml_tree.getroot()
    return xml


def _get_ns(xml: Element) -> str:
    """
    return any ns.

    - we create a dummy ns
    - we should find way to get actual name space and the
      name:value [, ... name:value]

    """
    ns = xml.nsmap
    return ns


def xml_pull_node(xml: Element, what: str) -> Element:
    """
    Extract 'what' from xml
    """
    item: Element = None
    if xml is not None:
        ns = _get_ns(xml)
        if ns:
            item = xml.find(what, ns)
        else:
            item = xml.find(what)
    return item


def xml_pull_item(xml: Element, what: str) -> str:
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

        if item is not None:
            text = item.text
            if not text:
                text = "-"
    return text


def xml_pull_date_range(metadata: Element) -> list[datetime | None]:
    """
    metadata should contain 'date_range' which in turn
    contains 'begin' and 'end' extract date
    range [start, end] as datetime objects
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
        if begin is not None:
            start_secs = begin.text
            start_secs = int(float(start_secs))
            dstart = datetime.fromtimestamp(start_secs)
        end = date_range.find('end', ns)
        if end is not None:
            end_secs = end.text
            end_secs = int(float(end_secs))
            dend = datetime.fromtimestamp(end_secs)

    drange = [dstart, dend]
    return drange


def xml_pull_records(xml: Element) -> str:
    """
    Return list of records
    """
    ns = _get_ns(xml)
    if ns:
        records = xml.findall('record', ns)
    else:
        records = xml.findall('record')
    return records


def xml_pull_auth_results_dkims(xml: Element) -> str:
    """
    Return list of auth_results/dkim
    """
    ns = _get_ns(xml)
    if ns:
        dkims = xml.findall('auth_results/dkim', ns)
    else:
        dkims = xml.findall('auth_results/dkim')
    return dkims


def xml_pull_auth_results_spf(xml: Element) -> str:
    """
    Return auth_results/spf
    """
    ns = _get_ns(xml)
    if ns:
        spf = xml.find('auth_results/spf', ns)
    else:
        spf = xml.find('auth_results/spf')
    return spf


def xml_file_read(topdir: str, ftype: str, file: str) -> Element:
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
                print('Warning zip compressed report has > 1 report file.')
    return xml
