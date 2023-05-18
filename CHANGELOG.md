# Changelog

## [3.6.3] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-05-18
 - PKGBUILD: add python-build to makedepends  
 - update CHANGELOG.md  

## [3.6.2] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-05-18
 - PKGBUILD: build wheel back to using python -m build instead of poetry  
 - update CHANGELOG.md  

## [3.6.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-05-17
 - Simplify Arch PKGBUILD and more closely follow arch guidelines  
 - update CHANGELOG.md  

## [3.6.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-04-29
 - Handle exceptions from bad XML report files  
 - update CHANGELOG.md  

## [3.5.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-21
 - Remove duplicate line in options class - has no effect  
 - update CHANGELOG.md  

## [3.4.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-17
 - Turn off debug - accidently left on with last release! So sorry  
 - typo in README-mta-sts.md  
 - update CHANGELOG.md  

## [3.3.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-09
 - More info about selectors including missing ("-")  
 - update CHANGELOG.md  

## [3.2.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-09
 - Add more info about dkim selectors typically from forwarded mail  
 - update CHANGELOG.md  

## [3.1.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-09
 - Sort short dkim selector tags before printing  
 - tweak readme for new tls-rpt tool  
 - update CHANGELOG.md  

## [3.0.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-07
 - Refactor code some.  
   Add new tls-rpt to generate reports for MTA-STS TLS reports  
 - update CHANGELOG.md  

## [2.3.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-07
 - Bug fix - clean up went too far added silly print bug - so sorry  
 - tidy README, add SPDX license line to missed file  
 - update CHANGELOG.md  

## [2.2.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-06
 - Use SPDX licensing.  
   Lint and tidy  
 - Fix description of input file disposition to show none,save,delete  
 - update CHANGELOG.md  

## [2.2.0] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2023-01-05
 - Add option for disposition of input files after report is generated.  
   --inp_files_disp can be none, save or delete.  Default is none.  
   --inp_files_save_dir specifies where to save input files when disposition is "save"  
 - update CHANGELOG.md  

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

