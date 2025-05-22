=========
Changelog
=========

Tags
====

::

	0.6.0 (2023-01-01) -> 6.1.0 (2025-05-21)
	138 commits.

Commits
=======


* 2025-05-21  : **6.1.0**

::

                Use builtin types where possible. e.g. typing.List -> list
 2025-05-05     update Changelog

* 2025-05-05  : **6.0.0**

::

                Tidy ups: PEP-8, PEP-257, PEP-484 PEP-561
                Reorganize code especially for PEP-561 (type hints)
 2025-03-15     update Changelog
                update Changelog

* 2025-03-15  : **5.1.4**

::

                Pre build PDF doc file.
                > PKGBUILD includes short changelog (pacman -Qc dmarc_report)
                update Changelog.rst

* 2025-03-15  : **5.1.3**

::

                Improve README and add theme to sample config
 2025-03-14     update Changelog.rst

* 2025-03-14  : **5.1.2**

::

                Just update PKGBUILD version
 2025-03-13     update Changelog.rst

* 2025-03-13  : **5.1.1**

::

                update Changelog.rst

* 2025-03-13  : **5.1.0**

::

                Add missing config sample file
                update Changelog.rst
                Bug fix by @rikyborg : Typo in ConfData class
 2025-03-11     update Changelog.rst

* 2025-03-11  : **5.0.2**

::

                Update Readme
 2025-03-10     update Changelog.rst

* 2025-03-10  : **5.0.1**

::

                Require py-cidr >= 2.7.0 which has ip sort fix
                update Changelog.rst

* 2025-03-10  : **5.0.0**

::

                remove files no longer being used
                New config file format using single config file shared by dmarc and tls
                report generators
                   version 1 configs with 2 files will be automatically converted and saved
                   as config.v2
                   Auto conversion pulls in new dependency on tomli-w to write the config
                   file.
                Reorg and simplify config and options code.
 2025-02-25     update Changelog.rst

* 2025-02-25  : **4.13.2**

::

                Small update to README
 2025-02-23     Add html and pdf docs to repo
                update Changelog.rst

* 2025-02-23  : **4.13.1**

::

                Change to py-cidr package for network tools.
                Update README
 2025-01-11     update Changelog.rst

* 2025-01-11  : **4.12.5**

::

                Ensure python version requirement is consistent (README, pyproject,
                PKGBUILD, requirements)
 2024-12-31     update Changelog.rst

* 2024-12-31  : **4.12.4**

::

                Add git signing key to Arch Package
                update Changelog.rst

* 2024-12-31  : **4.12.3**

::

                typo
                update Changelog.rst

* 2024-12-31  : **4.12.2**

::

                Add validpgpkeys to PKGBUILD
                update Changelog.rst

* 2024-12-31  : **4.12.1**

::

                All git tags are now signed.
                Update SPDX tags
 2024-11-28     update Changelog.rst

* 2024-11-28  : **4.12.0**

::

                Handle another seconds format in xml file
 2024-10-22     update Changelog.rst

* 2024-10-22  : **4.11.0**

::

                Additional input protections in cidr utils
                update Changelog.rst

* 2024-10-22  : **4.10.0**

::

                Bug fix when no "dom_ips" set. Resolves issue #2 reported by @g4242
 2024-10-20     update Changelog.rst

* 2024-10-20  : **4.9.0**

::

                remove dead code
                update Changelog.rst

* 2024-10-20  : **4.8.0**

::

                For completeness, Handle ip address of form ip/prefix
 2024-10-19     update Changelog.rst

* 2024-10-19  : **4.7.0**

::

                Now use python 3s ipaddress module instead of netaddr.
                  Its faster and we no longer require 3rd party module
                Require python version 3.11 or later
 2024-08-29     update Changelog.rst

* 2024-08-29  : **4.6.0**

::

                Switch to lxml for better handling of namespaces found in some reports
                Now handle namespaces (e.g. GMX uses them)
 2023-12-26     update Changelog.rst

* 2023-12-26  : **4.3.1**

::

                Add missing dateutil to depends in PKGBUILD
 2023-12-10     update Changelog.rst

* 2023-12-10  : **4.3.0**

::

                Add support for extracting reports from multiple emails saved into an mbox
                file - evolution saves emails this way
 2023-11-28     update Changelog.rst

* 2023-11-28  : **4.2.0**

::

                Handle badly formed dmarc report with missing date range
                Switch python build backend to hatch (was poetry)
 2023-10-29     update CHANGELOG.md

* 2023-10-29  : **4.0.0**

::

                Improve tls-rpt
                      Show policy name (tlsa, sts, none)
                      Show count of each failure result type
                      Now checks all "policies" returned in the json report.
                      Add date ranges to report
 2023-09-27     update CHANGELOG.md

* 2023-09-27  : **3.10.0**

::

                Reorganize documentation under Docs and migrate to restructured text
 2023-07-14     Nicer formatting in README-tls.rst
                update CHANGELOG.md

* 2023-07-14  : **3.9.2**

::

                Change to 3.9.2
                update CHANGELOG.md

* 2023-07-14  : **3.9.1**

::

                With updated README-tls.rst this time
                update CHANGELOG.md

* 2023-07-14  : **3.9.0**

::

                Update README with better description of TLS Report and use rst
 2023-07-09     update CHANGELOG.md

* 2023-07-09  : **3.8.0**

::

                Add any failure details to tls report
 2023-05-18     update CHANGELOG.md

* 2023-05-18  : **3.7.1**

::

                Update build info in README
                update CHANGELOG.md

* 2023-05-18  : **3.7.0**

::

                install: switch from pip to python installer package. This adds optimized
                bytecode
                update CHANGELOG.md

* 2023-05-18  : **3.6.3**

::

                PKGBUILD: add python-build to makedepends
                update CHANGELOG.md

* 2023-05-18  : **3.6.2**

::

                PKGBUILD: build wheel back to using python -m build instead of poetry
 2023-05-17     update CHANGELOG.md

* 2023-05-17  : **3.6.1**

::

                Simplify Arch PKGBUILD and more closely follow arch guidelines
 2023-04-29     update CHANGELOG.md

* 2023-04-29  : **3.6.0**

::

                Handle exceptions from bad XML report files
 2023-01-21     update CHANGELOG.md

* 2023-01-21  : **3.5.0**

::

                Remove duplicate line in options class - has no effect
 2023-01-17     update CHANGELOG.md

* 2023-01-17  : **3.4.0**

::

                Turn off debug - accidently left on with last release! So sorry
 2023-01-12     typo in README-mta-sts.md
 2023-01-09     update CHANGELOG.md

* 2023-01-09  : **3.3.0**

::

                More info about selectors including missing ("-")
                update CHANGELOG.md

* 2023-01-09  : **3.2.0**

::

                Add more info about dkim selectors typically from forwarded mail
                update CHANGELOG.md

* 2023-01-09  : **3.1.0**

::

                Sort short dkim selector tags before printing
 2023-01-07     tweak readme for new tls-rpt tool
                update CHANGELOG.md

* 2023-01-07  : **3.0.0**

::

                Refactor code some.
                Add new tls-rpt to generate reports for MTA-STS TLS reports
                update CHANGELOG.md

* 2023-01-07  : **2.3.0**

::

                Bug fix - clean up went too far added silly print bug - so sorry
 2023-01-06     tidy README, add SPDX license line to missed file
                update CHANGELOG.md

* 2023-01-06  : **2.2.1**

::

                Use SPDX licensing.
                Lint and tidy
 2023-01-05     Fix description of input file disposition to show none,save,delete
                update CHANGELOG.md

* 2023-01-05  : **2.2.0**

::

                Add option for disposition of input files after report is generated.
                   --inp_files_disp can be none, save or delete.  Default is none.
                   --inp_files_save_dir specifies where to save input files when disposition
                   is "save"
 2023-01-03     update CHANGELOG.md

* 2023-01-03  : **2.1.0**

::

                Right align numbers
                small tweak to README
                update CHANGELOG.md

* 2023-01-03  : **2.0.0**

::

                Fix bug where grand total missed orgs with 1 IP
                Add color report, default theme is dark. Can be light, dark or none to turn
                color off
                Add support for config files: /etc/dmarc_report/config -
                ~.config/dmarc_report/config
                  Config file is TOML format where each variable is the long_option name:
                  e.g. dir = "/a/b/dmarc_stuff"
                Add new option to set your IP or CIDR blocks - this will allow your own IPs
                to be colored
                  Makes it easy to spot mail generated from your own IP vs mail lists etc
                update CHANGELOG.md

* 2023-01-03  : **1.3.1**

::

                Improve report format a bit
 2023-01-02     typo
                small README tweak
                update CHANGELOG.md

* 2023-01-02  : **1.3.0**

::

                silly bug with multipart accidenlty ignoring report file
                update CHANGELOG.md

* 2023-01-02  : **1.2.1**

::

                remove reference to ripmime - no longer needed now that we handle mime
                attachments ourselves
                update CHANGELOG.md

* 2023-01-02  : **1.2.0**

::

                Fix bug with some multipart mime email from some reporters
                update CHANGELOG.md

* 2023-01-02  : **1.1.0**

::

                *.eml* files are now removed after the dmarc report is extracted.
                   Use option *-k, --keep* to prevent the *.eml* being removed
                update CHANGELOG.md

* 2023-01-02  : **1.0.0**

::

                Added support to extract dmarc reports from mime attachments in email files
                    Added option *-d, --dir* to specify the directory containing report
                    files
                more readme tweaks
                tweak readme
                update CHANGELOG.md

* 2023-01-02  : **0.9.1**

::

                Add note on handling email reports efficiently to README
 2023-01-01     remove unused file
                update CHANGELOG.md

* 2023-01-01  : **0.9.0**

::

                Small tweak to report output
                fix typo
                update CHANGELOG.md

* 2023-01-01  : **0.8.1**

::

                update readme
                update CHANGELOG.md

* 2023-01-01  : **0.8.0**

::

                bump vers to 0.8.0
                update CHANGELOG.md

* 2023-01-01  : **0.7.0**

::

                prep for release

* 2023-01-01  : **0.6.0**

::

                initial commit


