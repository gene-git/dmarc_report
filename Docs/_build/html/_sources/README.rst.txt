.. SPDX-License-Identifier: MIT

############
dmarc_report
############

Overview
========

Generate a human readable DMARC report from 1 or more standard DMARC and TLS-RPT xml email reports .

Note: 

   All git tags are signed by <arch@sapience.com>.
   Public key is available via WKD or download from website:
   https://www.sapience.com/tech
   After key is on keyring use the PKGBUILD source line ending with *?signed*
   or manually verify using *git tag -v <tag-name>

New / Interesting
=================

**Interesting**

 * Switch to *py-cidr* package for handling IPs instead of own versions.

   Available 
     - github <https://github.com/gene-git/py-cidr>
     - AUR <https://aur.archlinux.org/packages/py-cidr>

 * Now use python 3's ipaddress module instead of netaddr. 
   Its faster and we no longer require 3rd party library

 * Require python version 3.11 or later

 * Switch to lxml for better handling of xml namespaces found in some reports

 * Add support for handling mbox file with multiple emails containing reports.
   While some clients save multiple emails in separate *.eml* files, others, like
   evolution, save them all in a single *.mbox* file. Add support for this.

 * tls-rpt  

   New tool to generate report for TLS reports for MTA-STS or DANE. See README-tls.md
   This report has been updated - see Changelog for details.

 * *-ifd, --inp_file_disp*  

   Input file disposition options one of : none,save,delete  
   If set to save then all input files (xml, compressed xml and any kept eml files) are moved
   to directory specified by *inp_files_save_dir*.  


 * *-ifsd, --inp_files_save_dir*  

   When *inp_file_disp* is set, then input files are moved to this directory after report
   is generated.  Files are saved by year-month under the save directory


###############
Getting Started
###############

Installation
============

Available on
 * `Github`_
 * `Archlinux AUR`_

On Arch you can build using the PKGBUILD provided in packaging directory or from the AUR package.
To build manually, clone the repo and 

.. code-block:: bash

        rm -f dist/*
        python -m build --wheel --no-isolation
        root_dest="/"
        ./scripts/do-install $root_dest

When running as non-root then set root_dest a user writable directory

Applications
============

Save all DMARC or TLS-RPT reports into a directory. These are typically compressed xml files 
sent as email attachments.

config files
------------

There are 2 config files, *config* for dmarc-rpt and *tls-config* for tls-rpt.

Config files are in a directory which is searched in order:

.. code-block::

        /etc/dmarc_report/[tls-]config
        ~/.config/dmarc_report/[tls-]config

First config found is used.

Config files are standard TOML format.  Available config settings are set using::

        command_line_long_opt_name = xxx

e.g. to set data report dir use::

        dir = "/foo/goo/dmarc_reports"

Command line options override corresponding config setting.

Example of dmarc *config*::

        # comment
        dir = "~/dmarc/xml"
        inp_files_disp = "save"
        inp_files_save_dir = "../saved"
        dom_ips = ['1.1.1.1', '1.2.2.0/24']

This config says to read all the saved email reports from *~/dmarc/xml*
and to keep those files after processing report by moving them to *~/dmarc/saved*.
It also says that ips listed in dom_ips are your own domains.

Example of tls-rpt *tls-config*::

        # comment
        dir = "~/tls-rpt/xml"
        inp_files_disp = "save"
        inp_files_save_dir = "../saved"

See *Options* section for more detail.

dmarc-rpt Usage
---------------

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

Then save all the raw .eml files into ~/dmarc/reports and run before running the report

.. code-block:: bash

        dmarc-rpt

All attachments from dmarc email reports would be saved into "~/dmarc/saved/2023-01"
in this example. 

tls-rpt Usage
-------------

tls-rpt works in a similar way to dmarc-rpt, except it operates on TLS-RPT (compresses) xml inputs.

Command line options are shown first in parens below, followed by 
the corresponding config version in square brackets, if available.

Common Options
---------------

These apply to both dmarc-rpt and tls-rpt

 * (*-h, --help*)  
   Help for command line options.

 * (*-d, --dir*) [*dir = /path/xxx/*]  

   Allows specifying the directory with the dmarc report files to be processed.  
   The directory holding the report files (.eml, .xml, .gz or .zip)
   By default, dir is the current directory.

 * (*-k, --keep*)  [*keep = true*] 

   Prevent the *.eml* being removed after the attached xml reports are extracted.

 * (*-thm, --theme*)   

   Report is now in color.
   Default theme is 'dark'. Theme can be 'light' 'dark' or 'none', which turns off color report.

 * (*-v, --verb*)

   More verbose output

 * (*-ifd, --inp_file_disp*)  [*inp_file_disp = save*]

   Input file disposition options one of : none,save,delete
   If set to save then all input files (xml, compressed xml and any kept eml files) are moved
   to directory specified by *inp_files_save_dir*.  

 * (*-ifsd, --inp_files_save_dir*)

   When *inp_file_disp* is set, then input files are moved to this directory after report
   is generated.  Files are saved by year-month under the save directory

 * (*ips, --dom_ips*) [*dom_ips = ['1.1.1.0/24', '2.2.2.16/29'*]

   Comma separated list of IPs / CIDRs for your own domains. When used in config file 
   format as array of IP strings.

dmarc-rpt Specific Options
--------------------------

These are only applicable for dmarc-rpt.

 * (*-ips, --dom_ips*)  [*dom_ips = [ip, cidr, ... ]*]  

   Set the ips for your own domain(s), which will then be colored to make them easy to spot.
   Command line option is just comma separated list - no square brackets like config file.

 * (*fdm, --dmarc_fails*)

    Only include dmarc failures in report

 * (*fdk, --dkim_fails*)

    Only include dkim failures in report

 * (*fsp, --spf_fails*)

    Only include spf failures in report


Saving Email Reports From Email Client
======================================

In most mail clients, such as thunderbird,  one can select multiple email reports and 
then use *File -> Save As* to save the email files into a directory of your choosing.
Each email gets saved with a *.eml* extension.

########
Appendix
########

Dependencies
============

* Run Time :
  * python (3.13 or later)

* Building Package:
  * git
  * wheel (aka python-wheel)
  * build (aka python-build)
  * installer (aka python-installer)
  * poetry (aka python-poetry)
  - rsync

* Optional for building docs:

  * sphinx
  * texlive-latexextra  (archlinux packaguing of texlive tools)

Philosophy
==========

We follow the *live at head commit* philosophy. This means we recommend using the
latest commit on git master branch. We also provide git tags.

This approach is also taken by Google [1]_ [2]_.


License
=======

Created by Gene C. and licensed under the terms of the MIT license.

 * SPDX-License-Identifier: MIT
 * Copyright (c) 2023, Gene C 


.. _Github: https://github.com/gene-git/dmarc_report
.. _Archlinux AUR: https://aur.archlinux.org/packages/dmarc_report

.. [1] https://github.com/google/googletest  
.. [2] https://abseil.io/about/philosophy#upgrade-support

