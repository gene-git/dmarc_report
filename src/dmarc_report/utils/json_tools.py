# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
 json support tools
"""
from typing import (Any, Dict, List)
import os
import gzip
import zipfile
import json
from .tools import open_file


def get_json_from_zip(fname: str) -> List[Dict[str, Any]]:
    """
    Returns json object.

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


def get_json_from_gz(fname: str) -> Dict[str, Any]:
    """
    Returns json object.

    - fname = foo.json.zip
    - return 'foo.json' as json

    """
    # extract content into memory
    this_json: Dict[str, Any] = {}
    with gzip.open(fname, 'rb') as fobj:
        this_member = fobj.read()
        this_json = json.loads(this_member)
    return this_json


def get_json_from_json(fname: str) -> Dict[str, Any]:
    """
    Returns json object.

    - fname = foo.json
    - return json

    """
    # extract content into memory
    this_json: Dict[str, Any] = {}
    fobj = open_file(fname, 'r')
    if fobj:
        this_json = json.load(fobj)
        fobj.close()
    return this_json


def json_file_read(topdir: str, ext_type: str, file: str) -> Dict[str, Any]:
    """
    Read file into json.

    - ext_type is one of extensions from json_file_list method:
      - json, gz, zip
    Note that while zip may contain more than 1 file,
    all tls reports only use zip to compress single file.
    """
    jsons: Dict[str, Any] = {}
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
                print('Warning zip compressed report > 1 report file.')
                print(' - skipping any after the 1st.')
    return jsons
