# Changelog

## [2.1.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-03
 - Right align numbers  
 - small tweak to README  
 - update CHANGELOG.md  

## [2.0.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-03
 - Fix bug where grand total missed orgs with 1 IP  
   Add color report, default theme is dark. Can be light, dark or none to turn color off  
   Add support for config files: /etc/dmarc_report/config - ~.config/dmarc_report/config  
   Config file is TOML format where each variable is the long_option name:  
   e.g. dir = "/a/b/dmarc_stuff"  
   Add new option to set your IP or CIDR blocks - this will allow your own IPs to be colored  
   Makes it easy to spot mail generated from your own IP vs mail lists etc  
 - update CHANGELOG.md  

## [1.3.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-03
 - Improve report format a bit  
 - typo  
 - small README tweak  
 - update CHANGELOG.md  

## [1.3.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - silly bug with multipart accidenlty ignoring report file  
 - update CHANGELOG.md  

## [1.2.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - remove reference to ripmime - no longer needed now that we handle mime attachments ourselves  
 - update CHANGELOG.md  

## [1.2.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - Fix bug with some multipart mime email from some reporters  
 - update CHANGELOG.md  

## [1.1.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - *.eml* files are now removed after the dmarc report is extracted.  
   Use option *-k, --keep* to prevent the *.eml* being removed  
 - update CHANGELOG.md  

## [1.0.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - Added support to extract dmarc reports from mime attachments in email files  
   Added option *-d, --dir* to specify the directory containing report files  
 - more readme tweaks  
 - tweak readme  
 - update CHANGELOG.md  

## [0.9.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-02
 - Add note on handling email reports efficiently to README  
 - remove unused file  
 - update CHANGELOG.md  

## [0.9.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-01
 - Small tweak to report output  
 - fix typo  
 - update CHANGELOG.md  

## [0.8.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-01
 - update readme  
 - update CHANGELOG.md  

## [0.8.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-01
 - bump vers to 0.8.0  
 - update CHANGELOG.md  

## [0.7.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-01
 - prep for release  

## [0.6.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-01
 - initial commit  

