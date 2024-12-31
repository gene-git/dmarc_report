# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 json support tools
"""

import os
import gzip
import zipfile
import json
from .utils import open_file

def get_json_from_zip(fname):
    """
    returns json object
        - fname = foo.json.zip
        - return 'foo.json' as json
    """
    # extract content into memory
    members = []
    with zipfile.ZipFile(fname, 'r') as zipobj:
        for member in zipobj.namelist():
            this_member = zipobj.read(member)
            this_json = json.loads(this_member)
            members.append(this_json)

    return members

def get_json_from_gz(fname):
    """
    returns json object
        - fname = foo.json.zip
        - return 'foo.json' as json
    """
    # extract content into memory
    this_json = None
    with gzip.open(fname, 'rb') as fobj:
        this_member = fobj.read()
        this_json = json.loads(this_member)

    return this_json

def get_json_from_json(fname):
    """
    returns json object
        - fname = foo.json
        - return json
    """
    # extract content into memory
    this_json = None
    fobj = open_file(fname, 'r')
    if fobj:
        this_json = json.load(fobj)
        fobj.close()
    return this_json

def json_file_read(topdir, ext_type, file):
    """
    Read file into json - ext_type is one of extensions from json_file_list method:
      - json, gz, zip
    Note that while zip may contain more than 1 file -
    all tls reports only use zip to compress single file.
    """
    jsons = None
    fpath = os.path.join(topdir, file)
    match ext_type:
        case 'json':
            jsons = get_json_from_json(fpath)

        case 'gz':
            jsons = get_json_from_gz(fpath)

        case 'zip':
            json_list = get_json_from_zip(fpath)
            jsons = json_list[0]
            if len(json_list) > 1:
                print('Warning zip compressed report has more than 1 report file - not exepcted')
    return jsons
