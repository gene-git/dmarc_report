Changelog
=========

[4.0.0] ----- 2023-10-29
 * update project version  
 * Add comment to readme  
 * Improve tls-rpt  
 * Show policy name (tlsa, sts, none)  
 * Show count of each failure result type  
 * Now checks all "policies" returned in the json report.  
 * Add date ranges to report  
 * update Docs/Changelog.rst  

[3.10.0] ----- 2023-09-27
 * update project version  
 * Reorganize documentation under Docs and migrate to restructured text  
 * Nicer formatting in README-tls.rst  
 * update CHANGELOG.md  

[3.9.2] ----- 2023-07-14
 * update project version  
 * update CHANGELOG.md  

[3.9.1] ----- 2023-07-14
 * update project version  
 * update CHANGELOG.md  

[3.9.0] ----- 2023-07-14
 * update project version  
 * Update README with better description of TLS Report and use rst  
 * update CHANGELOG.md  

[3.8.0] ----- 2023-07-09
 * update project version  
 * Add any failure details to report  
 * update CHANGELOG.md  

[3.7.1] ----- 2023-05-18
 * update project version  
 * Update build info in README  
 * update CHANGELOG.md  

[3.7.0] ----- 2023-05-18
 * update project version  
 * install: switch from pip to python installer package  
 * update CHANGELOG.md  

[3.6.3] ----- 2023-05-18
 * update project version  
 * PKGBUILD: add python-build to makedepends  
 * update CHANGELOG.md  

[3.6.2] ----- 2023-05-18
 * update project version  
 * PKGBUILD: build wheel back to using python -m build instead of poetry  
 * update CHANGELOG.md  

[3.6.1] ----- 2023-05-17
 * update project version  
 * Simplify Arch PKGBUILD and more closely follow arch guidelines  
 * update CHANGELOG.md  

[3.6.0] ----- 2023-04-29
 * update project version  
 * Handle exceptions from bad XML report files  
 * update CHANGELOG.md  

[3.5.0] ----- 2023-01-21
 * update project version  
 * remove accidental duplicate line in options class - has no effect  
 * update CHANGELOG.md  

[3.4.0] ----- 2023-01-17
 * update project version  
 * turn debugger off  
 * typo in README-mta-sts.md  
 * update CHANGELOG.md  

[3.3.0] ----- 2023-01-09
 * update project version  
 * More info about selectors including missing ("-")  
 * update CHANGELOG.md  

[3.2.0] ----- 2023-01-09
 * update project version  
 * Add more info about dkim selectors typically from forwarded mail  
 * update CHANGELOG.md  

[3.1.0] ----- 2023-01-09
 * update project version  
 * update CHANGELOG.md  
 * update project version  
 * Sort short dkim selector tags before printing  
 * tweak readme for new tls-rpt tool  
 * update CHANGELOG.md  

[3.0.0] ----- 2023-01-07
 * update project version  
 * Update installer for tls-rpt  
 * Use nicer lines unicode 250x  
 * Refactor code some.  
 * Add new tls-rpt to generate reports for MTA-STS TLS reports  
 * update CHANGELOG.md  

[2.3.0] ----- 2023-01-07
 * update project version  
 * Bug fix - clean up went too far added silly print bug - so sorry  
 * tidy README, add SPDX license line to missed file  
 * update CHANGELOG.md  

[2.2.1] ----- 2023-01-06
 * update project version  
 * Use SPDX licensing.  
 * Lint and tidy  
 * Fix description of input file disposition to show none,save,delete  
 * update CHANGELOG.md  

[2.2.0] ----- 2023-01-05
 * update project version  
 * debug off  
 * Add option for disposition of input files after report is generated.  
 * --inp_files_disp can be none, save or delete.  Default is none.  
 * --inp_files_save_dir specifies where to save input files when disposition is "save"  
 * update CHANGELOG.md  

[2.1.0] ----- 2023-01-03
 * update project version  
 * Right align numbers  
 * Typo README  
 * small tweak to README  
 * update CHANGELOG.md  
 * update project version  

[2.0.0] ----- 2023-01-03
 * update readme  
 * fix help for -ips  
 * debug off for release  
 * Finish Color Report  
 * Fix bug where grand total missed orgs with 1 IP  
 * Color org and domain - more to do  
 * set default theme to dark  
 * prep work for adding color to report  
 * Show which data directory used at top of report  
 * Add suport for reading config file options.  
 * In order, /etc/dmarc_report/config then ~/.config/dmarc_report/config  
 * update CHANGELOG.md  

[1.3.1] ----- 2023-01-03
 * update project version  
 * update CHANGELOG.md  
 * update project version  
 * Improve report format a bit  
 * typo  
 * small README tweak  
 * update CHANGELOG.md  

[1.3.0] ----- 2023-01-02
 * update project version  
 * debug off  
 * silly bug with multipart accidenlty ignoring report file  
 * silly bug with multipart accidenlty ignoring report file  
 * update CHANGELOG.md  

[1.2.1] ----- 2023-01-02
 * update project version  
 * remove reference to ripmime - no longer needed now that we handle mime attachments ourselves  
 * update CHANGELOG.md  

[1.2.0] ----- 2023-01-02
 * update project version  
 * Fix bug with some multipart mime email from some reporters  
 * update CHANGELOG.md  

[1.1.0] ----- 2023-01-02
 * update project version  
 * *.eml* files are now removed after the dmarc report is extracted.  
 * Use option *-k, --keep* to prevent the *.eml* being removed  
 * update CHANGELOG.md  

[1.0.0] ----- 2023-01-02
 * update project version  
 * Added support to extract dmarc reports from mime attachments in email files  
 * Added option *-d, --dir* to specify the directory containing report files  
 * more readme tweaks  
 * tweak readme  
 * update CHANGELOG.md  

[0.9.1] ----- 2023-01-02
 * update project version  
 * Add note on handling email reports efficiently to README  
 * update CHANGELOG.md  

[0.9.0] ----- 2023-01-01
 * update project version  
 * Small tweak to report output  
 * Tweak description  
 * typo  
 * update CHANGELOG.md  

[0.8.1] ----- 2023-01-01
 * update project version  
 * update readme  
 * update README  
 * update CHANGELOG.md  

[0.8.0] ----- 2023-01-01
 * update project version  
 * update CHANGELOG.md  

[0.7.1] ----- 2023-01-01
 * update project version  
 * Add sources  
 * update CHANGELOG.md  

[0.7.0] ----- 2023-01-01
 * update project version  
 * initial commit  

