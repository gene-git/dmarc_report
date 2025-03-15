Changelog
=========

**[5.1.3] ----- 2025-03-15** ::

	    Improve README and add theme to sample config
	    update Changelog.rst


**[5.1.2] ----- 2025-03-14** ::

	    Just update PKGBUILD version
	    update Changelog.rst


**[5.1.1] ----- 2025-03-13** ::

	    update Changelog.rst


**[5.1.0] ----- 2025-03-13** ::

	    Add missing config sample file
	    update Changelog.rst
	    Bug fix by @rikyborg : Typo in ConfData class
	    update Changelog.rst


**[5.0.2] ----- 2025-03-11** ::

	    Update Readme
	    update Changelog.rst


**[5.0.1] ----- 2025-03-10** ::

	    Require py-cidr >= 2.7.0 which has ip sort fix
	    update Changelog.rst


**[5.0.0] ----- 2025-03-10** ::

	    remove files no longer being used
	    New config file format using single config file shared by dmarc and tls report generators
	       version 1 configs with 2 files will be automatically converted and saved as config.v2
	       Auto conversion pulls in new dependency on tomli-w to write the config file.
	    Reorg and simplify config and options code.
	    update Changelog.rst


**[4.13.2] ----- 2025-02-25** ::

	    Small update to README
	    Add html and pdf docs to repo
	    update Changelog.rst


**[4.13.1] ----- 2025-02-23** ::

	    Change to py-cidr package for network tools.
	    Update README
	    update Changelog.rst


**[4.12.5] ----- 2025-01-11** ::

	    Ensure python version requirement is consistent (README, pyproject, PKGBUILD, requirements)
	    update Changelog.rst


**[4.12.4] ----- 2024-12-31** ::

	    Add git signing key to Arch Package
	    update Changelog.rst


**[4.12.3] ----- 2024-12-31** ::

	    typo
	    update Changelog.rst


**[4.12.2] ----- 2024-12-31** ::

	    Add validpgpkeys to PKGBUILD
	    update Changelog.rst


**[4.12.1] ----- 2024-12-31** ::

	    All git tags are now signed.
	    Update SPDX tags
	    update Changelog.rst


**[4.12.0] ----- 2024-11-28** ::

	    Handle another seconds format in xml file
	    update Changelog.rst


**[4.11.0] ----- 2024-10-22** ::

	    Additional input protections in cidr utils
	    update Changelog.rst


**[4.10.0] ----- 2024-10-22** ::

	    Bug fix when no "dom_ips" set. Resolves issue #2 reported by @g4242
	    update Changelog.rst


**[4.9.0] ----- 2024-10-20** ::

	    remove dead code
	    update Changelog.rst


**[4.8.0] ----- 2024-10-20** ::

	    For completeness, Handle ip address of form ip/prefix
	    update Changelog.rst


**[4.7.0] ----- 2024-10-19** ::

	    Now use python 3s ipaddress module instead of netaddr.
	      Its faster and we no longer require 3rd party module
	    Require python version 3.11 or later
	    update Changelog.rst


**[4.6.0] ----- 2024-08-29** ::

	    Switch to lxml for better handling of namespaces found in some reports
	    Now handle namespaces (e.g. GMX uses them)
	    update Changelog.rst


**[4.3.1] ----- 2023-12-26** ::

	    Add missing dateutil to depends in PKGBUILD
	    update Changelog.rst


**[4.3.0] ----- 2023-12-10** ::

	    Add support for extracting reports from multiple emails saved into an mbox file - evolution saves emails this way
	    update Changelog.rst


**[4.2.0] ----- 2023-11-28** ::

	    Handle badly formed dmarc report with missing date range
	    Switch python build backend to hatch (was poetry)
	    update CHANGELOG.md


**[4.0.0] ----- 2023-10-29** ::

	    Improve tls-rpt
	          Show policy name (tlsa, sts, none)
	          Show count of each failure result type
	          Now checks all "policies" returned in the json report.
	          Add date ranges to report
	    update CHANGELOG.md


**[3.10.0] ----- 2023-09-27** ::

	    Reorganize documentation under Docs and migrate to restructured text
	    Nicer formatting in README-tls.rst
	    update CHANGELOG.md


**[3.9.2] ----- 2023-07-14** ::

	    Change to 3.9.2
	    update CHANGELOG.md


**[3.9.1] ----- 2023-07-14** ::

	    With updated README-tls.rst this time
	    update CHANGELOG.md


**[3.9.0] ----- 2023-07-14** ::

	    Update README with better description of TLS Report and use rst
	    update CHANGELOG.md


**[3.8.0] ----- 2023-07-09** ::

	    Add any failure details to tls report
	    update CHANGELOG.md


**[3.7.1] ----- 2023-05-18** ::

	    Update build info in README
	    update CHANGELOG.md


**[3.7.0] ----- 2023-05-18** ::

	    install: switch from pip to python installer package. This adds optimized bytecode
	    update CHANGELOG.md


**[3.6.3] ----- 2023-05-18** ::

	    PKGBUILD: add python-build to makedepends
	    update CHANGELOG.md


**[3.6.2] ----- 2023-05-18** ::

	    PKGBUILD: build wheel back to using python -m build instead of poetry
	    update CHANGELOG.md


**[3.6.1] ----- 2023-05-17** ::

	    Simplify Arch PKGBUILD and more closely follow arch guidelines
	    update CHANGELOG.md


**[3.6.0] ----- 2023-04-29** ::

	    Handle exceptions from bad XML report files
	    update CHANGELOG.md


**[3.5.0] ----- 2023-01-21** ::

	    Remove duplicate line in options class - has no effect
	    update CHANGELOG.md


**[3.4.0] ----- 2023-01-17** ::

	    Turn off debug - accidently left on with last release! So sorry
	    typo in README-mta-sts.md
	    update CHANGELOG.md


**[3.3.0] ----- 2023-01-09** ::

	    More info about selectors including missing ("-")
	    update CHANGELOG.md


**[3.2.0] ----- 2023-01-09** ::

	    Add more info about dkim selectors typically from forwarded mail
	    update CHANGELOG.md


**[3.1.0] ----- 2023-01-09** ::

	    Sort short dkim selector tags before printing
	    tweak readme for new tls-rpt tool
	    update CHANGELOG.md


**[3.0.0] ----- 2023-01-07** ::

	    Refactor code some.
	    Add new tls-rpt to generate reports for MTA-STS TLS reports
	    update CHANGELOG.md


**[2.3.0] ----- 2023-01-07** ::

	    Bug fix - clean up went too far added silly print bug - so sorry
	    tidy README, add SPDX license line to missed file
	    update CHANGELOG.md


**[2.2.1] ----- 2023-01-06** ::

	    Use SPDX licensing.
	    Lint and tidy
	    Fix description of input file disposition to show none,save,delete
	    update CHANGELOG.md


**[2.2.0] ----- 2023-01-05** ::

	    Add option for disposition of input files after report is generated.
	       --inp_files_disp can be none, save or delete.  Default is none.
	       --inp_files_save_dir specifies where to save input files when disposition is "save"
	    update CHANGELOG.md


**[2.1.0] ----- 2023-01-03** ::

	    Right align numbers
	    small tweak to README
	    update CHANGELOG.md


**[2.0.0] ----- 2023-01-03** ::

	    Fix bug where grand total missed orgs with 1 IP
	    Add color report, default theme is dark. Can be light, dark or none to turn color off
	    Add support for config files: /etc/dmarc_report/config - ~.config/dmarc_report/config
	      Config file is TOML format where each variable is the long_option name:
	      e.g. dir = "/a/b/dmarc_stuff"
	    Add new option to set your IP or CIDR blocks - this will allow your own IPs to be colored
	      Makes it easy to spot mail generated from your own IP vs mail lists etc
	    update CHANGELOG.md


**[1.3.1] ----- 2023-01-03** ::

	    Improve report format a bit
	    typo
	    small README tweak
	    update CHANGELOG.md


**[1.3.0] ----- 2023-01-02** ::

	    silly bug with multipart accidenlty ignoring report file
	    update CHANGELOG.md


**[1.2.1] ----- 2023-01-02** ::

	    remove reference to ripmime - no longer needed now that we handle mime attachments ourselves
	    update CHANGELOG.md


**[1.2.0] ----- 2023-01-02** ::

	    Fix bug with some multipart mime email from some reporters
	    update CHANGELOG.md


**[1.1.0] ----- 2023-01-02** ::

	    *.eml* files are now removed after the dmarc report is extracted.
	       Use option *-k, --keep* to prevent the *.eml* being removed
	    update CHANGELOG.md


**[1.0.0] ----- 2023-01-02** ::

	    Added support to extract dmarc reports from mime attachments in email files
	        Added option *-d, --dir* to specify the directory containing report files
	    more readme tweaks
	    tweak readme
	    update CHANGELOG.md


**[0.9.1] ----- 2023-01-02** ::

	    Add note on handling email reports efficiently to README
	    remove unused file
	    update CHANGELOG.md


**[0.9.0] ----- 2023-01-01** ::

	    Small tweak to report output
	    fix typo
	    update CHANGELOG.md


**[0.8.1] ----- 2023-01-01** ::

	    update readme
	    update CHANGELOG.md


**[0.8.0] ----- 2023-01-01** ::

	    bump vers to 0.8.0
	    update CHANGELOG.md


**[0.7.0] ----- 2023-01-01** ::

	    prep for release


**[0.6.0] ----- 2023-01-01** ::

	    initial commit


