# dmarc_report

Generate Report from dmarc email reports

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

Save all dmarc reports into a directory. The ripmime[1] tool is useful for extracting compressed xml 
report files from saved emails especially if saving multiple email reports.

Change to the directory containing one or more dmarc report files and simply run


        dmarc-rpt

The tool processes all xml and gzip/zip compressed xml files.

[1] https://github.com/inflex/ripMIME


## License

`dmarc_rpt` was created by Gene C. It is licensed under the terms of the MIT license.

## Credits
