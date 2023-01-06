# dmarc_report

Generate a human readable DMARC report from 1 or more standard xml email reports .

## Installation

Available on
 - [Github source ](https://github.com/gene-git/dmarc_report)
 - [Archlinux AUR](https://aur.archlinux.org/packages/dmarc_report)
   PKGBUILD also in source tree under packaging

If on Arch can build using the PKGBUILD provided which is also available in the AUR.

To build it manually, clone the repo and do:

        rm -f dist/*
        poetry build --format wheel
        root_dest="/"
        ./scripts/do-install $root_dest

  If running as non-root then set root\_dest a user writable directory

### Dependencies

- Run Time :
  - python (3.9 or later)
  - netaddr (aka python-netaddr )
  - tomli (for python < 3.11)

- Building Package:
  - git
  - poetry (aka python-poetry)
  - wheel (aka python-wheel)
  - pip (aka python-pip)
  - rsync

## Interesting, New or Coming Soon

### New

 - *-ifd, --inp_file_disp*  
   Input file disposition options one of : none,save,delete  
   If set to save then all input files (xml, compressed xml and any kept eml files) are moved
   to directory specified by *inp_files_save_dir*.  


 - *-ifsd, --inp_files_save_dir*  
   When *inp_file_disp* is set, then input files are moved to this directory after report
   is generated.  Files are saved by year-month under the save directory

### Interesting

 - Added support for config files  
   Order is /etc/dmarc\_report/config then ~/.config/dmarc\_report/config
   Config files are in toml format and options are set using

        long_opt_name = xxx

 - *-thm, --theme*  
   Report is now in color.
   Default theme is 'dark'. Theme can be 'light' 'dark' or 'none', which turns off color report.

 - *-ips, --dom_ips*  
   *dom_ips = [ip, cidr, ... ]  
   Set the ips and/or cidr blocks for your own domain(s). 
   This is used to color them making them easier to spot.
   Command line option is just comma separated list - no square brackets like config file.

## Usage

Save all dmarc reports into a directory. 
Change to the directory containing one or more dmarc report files and simply run


        dmarc-rpt

Any email files, those ending with *.eml* will be processed first. These are assumed to
contain the dmarc report as a mime attachment. The attachment is extracted from any such email 
files. 

Then all remaining files are read and processed. The tool processes all xml 
and gzip/zip compressed xml dmarc report files and generates a human readable report.

We following Postel's law and try to be liberal in what we accept as input. To that end
we accept the dmarc XML report file, a gzip/zip compressed version of same or a saved email 
file text file with the report itself being a mime attachment.

Any file with extension *.eml* is treated as an email file.

To avoid line wrapping, the report should be viewed on wide enough terminal; roughly 112 or chars or more.

For convenience after report is generated, the inptu files can be autotically moved to a save 
direcory, left where they are or removed. A typical sequents of eveents is to save
the email reports, run dmarc-rpt.  By auto moving (or removing) the input files, makes it simpler
when doing the next batch of dmarc reports.

For example, you might save all .eml files in same directory and with config settings:

        dir = "~/dmarc/reports"
        inp_files_disp = "save"
        inp_files_save_dir = "../saved"
        dom_ips = ['1.1.1.1', '1.2.2.0/24']


Then save all the raw .eml files into ~/.dmarc/reports and run :

        dmarc-rpt

Then all attachments delivered from email dmarc reports would be saved into "~/dmarc/saved/2023-01"
as an example. 

## Options

Options are read first from config files then command line. Config files are read
from */etc/dmarc_report/config* then *~/.config/dmarc_report/config*.  Config files
are in standard TOML format.

Available config settings use command line long option = xxx.
Below the command line options are shown first followed by config.

e.g. to set data report dir in config use:

        dir = "/foo/goo/dmarc_reports"

 - *-d, --dir*   
   *dir = *  
   Allows specifying the directory with the dmarc report files to be processed.  
   The directory holding the report files (.eml, .xml, .gz or .zip)
   By default, dir is the current directory.

 - *-k, --keep*  
   *keep = true*  
   Prevent the *.eml* being removed after the attached xml reports are extracted.

 - *-thm, --theme*  
   Report is now in color.
   Default theme is 'dark'. Theme can be 'light' 'dark' or 'none', which turns off color report.

 - *-ips, --dom_ips*  
   *dom_ips = [ip, cidr, ... ]  
   Set the ips for your own domain(s), which will then be colored to make them easy to spot.
   Command line option is just comma separated list - no square brackets like config file.

 - *-ifd, --inp_file_disp*  
   Input file disposition options one of : none,save,delete
   If set to save then all input files (xml, compressed xml and any kept eml files) are moved
   to directory specified by *inp_files_save_dir*.  

 - *-ifsd, --inp_files_save_dir*  
   When *inp_file_disp* is set, then input files are moved to this directory after report
   is generated.  Files are saved by year-month under the save directory

 - *-h, --help*  
   Help for command line options.

## Saving Email Reports From Email Client

In most mail clients, such as thunderbird,  one can select multiple email reports and 
then use *File -> Save As* to save the email files into a directory of your choosing.
Each email gets saved with a *.eml* extension.


## License

`dmarc_rpt` was created by Gene C. It is licensed under the terms of the MIT license.
SPDX-License-Identifier: MIT
Copyright (c) 2023, Gene C 


