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

- Building Package:
  - git
  - poetry (aka python-poetry)
  - wheel (aka python-wheel)
  - pip (aka python-pip)
  - rsync

## Usage

Save all dmarc reports into a directory. The ripmime[1] tool is useful for extracting attached compressed xml 
report files from saved emails especially if saving multiple email reports.

Change to the directory containing one or more dmarc report files and simply run


        dmarc-rpt

The tool processes all xml and gzip/zip compressed xml files.

[1] https://github.com/inflex/ripMIME

### Extracting xml attachments from emails

In thunderbird if I select multiple email reports and then use File -> Save As into a directory
each email gets saved with a *.eml* extension. Then attached dmarc reports can be extracted using 
ripMIME using a little script such as:

        #!/bin/bash
        #
        # extract attachments from all the saved '.eml' files
        #
        for i in *.eml
        do
            echo " ... $i"
            ripmime -i "$i"
        done
        rm -f textfile* *.eml

I file all email dmarc reports into a separate dmarc report email folder
using dovecot's pigeonhole sieve functionality. 

The sieve rule matches on the *To* header and then uses
*fileinto* the dmarc folder. This makes it very simple to select all, save and process 
quickly to get the final (human) report for all the email reports.

## License

`dmarc_rpt` was created by Gene C. It is licensed under the terms of the MIT license.

