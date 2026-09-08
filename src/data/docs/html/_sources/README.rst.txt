.. SPDX-License-Identifier: GPL-2.0-or-later

============
dmarc_report
============

Overview
========

Generate a human readable report from 1 or more standard DMARC and TLS-RPT xml email reports .
DMARC reports are made using *dmarc-rpt* while TLS-RPTs use *tls-rpt*

**Note**: 

All git tags are signed by <arch@sapience.com>.
Public key is available via WKD or download from `sapience website <https://www.sapience.com/tech>`_.
After key is on keyring use the PKGBUILD source line ending with *?signed*
or manually verify using *git tag -v <tag-name>*


Getting Started
===============

Save all DMARC or TLS-RPT reports into a directory. These are typically compressed xml/json files 
sent as email attachments. The saved reports can be :

* individual email files each with a compressed xml/json attachment. Thunderbird saves them this way.
  These are saved with a *.eml* extension.

* one single file with several emails, each with the attachment. Evolution saves this way.
  These are saved with *.mbox* extension.

* Individual compressed, or uncmompressed, xml reports created by saving the attachments from each email.
 
*dmarc-rpt* and *tls-rpt* will extract the actual **xml** (*dmarc*) or **json** (tls-rpt) data 
from all of the above.

Quick start
-----------

Save all emails with DMARC or TLS-RPT attachments to a directory, change into that directory and run
either dmarc-rpt or tls-rpt as appropriate.

It is generally more convenient to use a config file explained below.


Config Files
------------

Config files are read, in order, from directories::

    /etc/dmarc_report/
    ~/.config/dmarc_report/

with the settings in *~/.config/...* overriding any found in */etc/...*.
Command line options override config settings.

There are two config file formats supported. The older version 1 format uses 2 separate files:

* *config* - for dmarc-rpt
* *tls-config* - for tls-rpt

New version 2 format uses a single file, *config.v2*. Version 2 config will be used if its found.
If only version 1 configs are found they will be automatically converted to version 2, which 
are used thereafter.

All config files use standard TOML format. Config files use 3 sections. A global section
and one each for dmarc and tls-rpt.

Available config values are set using::

    command_line_long_opt_name = xxx

e.g. to set data report dir use::

    dir = "/foo/goo/dmarc_reports"

A sample config is available in the *conf.d* directory. A typical config might be of the form::

    # comment
    [global]
        theme = 'dark'
        inp_files_disp = "save"
        inp_files_save_dir = "../saved"

    [dmarc]
        dom_ips = ['1.1.1.1', '1.2.2.0/24']
        dir = "~/mail-reports/dmarc/xml"

    [tls]
        dir = "~/mail-reports/tls/xml"

Variables set in *[dmarc]* or *[tls]* sections override any correspodning global ones.

This sample config says to read all the saved dmarc email reports from *~/mail-reports/dmarc/xml* and
the tls reports from *~/mail-reports/tls/xml*.

And to save the raw files after processing report by moving them to *~/mail-reports/dmarc/saved*
or *~/mail-reports/tls/saved*.

For dmarc it says that ips listed in *dom_ips* are for your own domains.

Command line options override the corresponding config setting.
See *Options* section for more detail.

dmarc-rpt
---------

Change to the directory containing the one or more dmarc report files and simply run

 .. code-block:: bash

        dmarc-rpt

When using the *--dir* option (or config setting *dir*) it is not necessary 
to change directories before running the report.

Any email files, those ending with *.eml* will be processed first. These are assumed to
contain the report as a mime attachment. The attachment is extracted from any such email 
files. Some mail clients save multiple emails as a single mbox file. Each email in the mbox
file will be similarly processed and have the attached report extracted.

Then all remaining files are read and processed. The tool processes all xml 
and gzip/zip compressed xml dmarc report files and generates a human readable report.

We follow Postel's law and try to be liberal in what we accept as input. To that end
we accept the dmarc XML report file, a gzip/zip compressed version of same or a saved email 
file text file with the report itself being a mime attachment.

Any file with extension *.eml* is treated as an email file.

To avoid line wrapping, the report should be viewed on wide enough terminal; roughly 112 or chars or more.

For convenience after report is generated, the input files can be automatically moved to a save 
direcory, left where they are or removed. A typical sequents of events is to save
the email reports, run dmarc-rpt.  By auto moving (or removing) the input files, makes it simpler
when doing the next batch of dmarc reports.

Then save all the raw .eml files into ~/dmarc/reports and run the report.

All attachments from dmarc email reports would be saved into "~/dmarc/saved/2023-01"
in this example. 

tls-rpt
-------

tls-rpt works in a similar way to dmarc-rpt, except it operates on TLS-RPT (compressed) xml inputs.

Command line options:

Common Options
---------------

These apply to both dmarc-rpt and tls-rpt::

    -h, --help                          show this help message and exit
    -d, --dir DIR                       Directory containing dmarc report files (xxx)
    -ifd, --inp_files_disp WHAT         none, delete, save: disposition of input files. See -ifsd (save)
    -ifsd, --inp_files_save_dir DIR     When -ifd is save, input files moved here afer report (../saved)
    -k, --keep                          Keep .eml files extracted from attachment (False)
    -thm, --theme THEME                 Set color theme: dark, light, none (dark)
    -v, --verb                          Be more verbose

dmarc-rpt Additional Options
-----------------------------

In addition to the common options::

    -ips, --dom_ips NUM                 Comma separated list of IPs / CIDRs for your own domains
    -fdm, --dmarc_fails                 DMARC Report - limit to failures
    -fdk, --dkim_fails                  DKIM Report - limit to failures
    -fsp, --spf_fails                   SPF Report - limit to failures

For example to have these IP addresses marked in the reports::

    --dom-ips "1.1.1.0/24,2.2.2.16/29"

Or when used in the config file::

    dom_ips = ['1.1.1.0/24', '2.2.2.16/29']


Saving Email Reports From Email Client
--------------------------------------

In most mail clients, such as thunderbird,  one can select multiple email reports and 
then use *File -> Save As* to save the email files into a directory of your choosing.
Each email gets saved with a *.eml* extension.

