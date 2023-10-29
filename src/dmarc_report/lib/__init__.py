# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Gene C
"""
Support routines for dmarc report generator
"""
from .class_dmarc import DmarcRpt
from .xml_tools import xml_file_list
from .xml_tools import xml_file_read
from .email import find_extract_email_attachments
from .save_input_files import input_files_disposition
from .class_tls import TlsRpt
from .json_tools import json_file_read
