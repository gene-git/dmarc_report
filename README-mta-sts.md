# tls-rpt

Generate a human readable tls report from 1 or more standard mta-sts tls report files.

## Installation

Part of the dmarc\_report package

### New

 - tls-rpt
   Tool to generate reports from 1 or more emailed mta-sts reports. Similar to 
   dmarc-rpt, the tool can consume email files (.eml) or the json attachments (plain or compressed)
   delivered as part of the usual mts-sts reports - and in directory specified by *inp_files_save_dir*.  

### Interesting

## Brief Background

MTA-STS is defined in [RFC 8461](https://www.rfc-editor.org/rfc/rfc8461) and quoting 
from the RFC:

```
SMTP MTA Strict Transport Security (MTA-STS) is a mechanism enabling
   mail service providers (SPs) to declare their ability to receive
   Transport Layer Security (TLS) secure SMTP connections and to specify
   whether sending SMTP servers should refuse to deliver to MX hosts
   that do not offer TLS with a trusted server certificate.
```

To receive TLS reports requires 2 things.

 - a policy file available via the email domain web server.  
   For *example.com* it would be :

        https://mta-sts.example.com/.well-known/mta-sts.txt
    
 - 2 DNS TXT record for the domain.
   For example:  
    
        _mta-sts.example.org.  IN TXT “v=STSv1; id=202301011200;”  
        _smtp._tls.example.org IN TXT "v=TLSRPTv1;rua=mailto:tlsrpt@example.com"


The policy file is of the form where mode is *enforce* or *testing*:

        version: STSv1
        mode: enforce
        mx: example.com
        mx: *.example.com
        max_age: 1296000

The TLS reports will be sent to the email provided by second TXT record, in above example
they will go to *tlsrpt@example.com*.


## Usage

Save all tls reports into a directory. 
Change to the directory containing one or more dmarc report files and simply run

        tls-rpt

When using the --dir option (or config) it is not necessary to change directories before
running the report.

Any email files, those ending with *.eml* will be processed first. These are assumed to
contain the dmarc report as a mime attachment. The attachment is extracted from any such email 
files. 

Then all remaining files are read and processed. The tool processes all json 
and gzip/zip compressed json tls report files and generates a human readable report.

Any file with extension *.eml* is treated as an email file.

For convenience after report is generated, the input files can be automatically moved to a save 
direcory, left where they are or removed. A typical sequents of eveents is to save
the email reports, run dmarc-rpt.  By auto moving (or removing) the input files, makes it simpler
when doing the next batch of dmarc reports.

For example, you might save all .eml files in same directory and with config settings:

        dir = "~/tlsrpt/reports"
        inp_files_disp = "save"
        inp_files_save_dir = "../saved"

Then save all the raw .eml files into ~/tlsrpt/reports and run :

        tls-rpt

Then all attachments from email reports would be saved into "~/tlsrpt/saved/2023-01"
in this example. 

## Options

Options are read first from config files then command line. Config files are read
from */etc/dmarc_report/config-tls* then *~/.config/dmarc_report/config-tls*.  Config files
are in standard TOML format.

Config settings use command line long option = xxx.
Below, the command line options are shown first followed by config.

e.g. to set data report dir in config use:

        dir = "/foo/goo/other"

 - *-d, --dir*   
   *dir = *  
   Allows specifying the directory with the dmarc report files to be processed.  
   The directory holding the report files (.eml, .json, .gz or .zip)
   By default, dir is the current directory.

 - *-k, --keep*  
   *keep = true*  
   Prevent the *.eml* being removed after the attached xml reports are extracted.

 - *-thm, --theme*  
   Report is now in color.
   Default theme is 'dark'. Theme can be 'light' 'dark' or 'none', which turns off color report.

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

Created by Gene C. It is licensed under the terms of the MIT license.

 - SPDX-License-Identifier: MIT
 - Copyright (c) 2023, Gene C 


