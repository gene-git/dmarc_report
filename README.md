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

- Optional :
  - ripMIME

- Building Package:
  - git
  - poetry (aka python-poetry)
  - wheel (aka python-wheel)
  - pip (aka python-pip)
  - rsync

## Interesting, New or Coming Soon

### New

 - Added support to extract dmarc reports from mime attachments in  
   email files.  Any file with extension *.eml* is treated as an email file.
   No longer necessary to use standalone program to extract mime attachments.

 - Added option *-d, --dir*  
   Allows specifying the directory with the dmarc report files to be processed.  
   The default dir remains the current directory.

## Usage

Save all dmarc reports into a directory. 
Change to the directory containing one or more dmarc report files and simply run


        dmarc-rpt

Any email files, those ending with *.eml* will be processed first. These are assumed to
contain the dmarc report as a mime attachment. The attachment is extracted from any such email 
files. 

Then all remaining files are read and processed. The tool processes all xml 
and gzip/zip compressed xml dmarc report files and generates a human readable report.

## Saving Email Reports

In most mail clients, such as thunderbird,  one can select multiple email reports and 
then use *File -> Save As* to save the email files into a directory of your choosing.
Each email gets saved with a *.eml* extension.


## License

`dmarc_rpt` was created by Gene C. It is licensed under the terms of the MIT license.

