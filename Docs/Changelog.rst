Changelog
=========

Tags
====

.. code-block:: text

	0.6.0 (2023-01-01) -> 7.0.0 (2026-01-03)
	140 commits.

Commits
=======


* 2026-01-03  : **7.0.0**

.. code-block:: text

              - Switch packaging from hatch to uv
                Reorg source code
                License GPL-2.0-or-later
 2025-05-21   ⋯

.. code-block:: text

              - update Changelogs

* 2025-05-21  : **6.1.0**

.. code-block:: text

              - Use builtin types where possible. e.g. typing.List -> list
 2025-05-05   ⋯

.. code-block:: text

              - update Changelog

* 2025-05-05  : **6.0.0**

.. code-block:: text

              - Tidy ups: PEP-8, PEP-257, PEP-484 PEP-561
                Reorganize code especially for PEP-561 (type hints)
 2025-03-15   ⋯

.. code-block:: text

              - update Changelog
              - update Changelog

* 2025-03-15  : **5.1.4**

.. code-block:: text

              - Pre build PDF doc file.
                > PKGBUILD includes short changelog (pacman -Qc dmarc_report)
              - update Changelog.rst

* 2025-03-15  : **5.1.3**

.. code-block:: text

              - Improve README and add theme to sample config
 2025-03-14   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-03-14  : **5.1.2**

.. code-block:: text

              - Just update PKGBUILD version
 2025-03-13   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-03-13  : **5.1.1**

.. code-block:: text

              - update Changelog.rst

* 2025-03-13  : **5.1.0**

.. code-block:: text

              - Add missing config sample file
              - update Changelog.rst
              - Bug fix by @rikyborg : Typo in ConfData class
 2025-03-11   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-03-11  : **5.0.2**

.. code-block:: text

              - Update Readme
 2025-03-10   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-03-10  : **5.0.1**

.. code-block:: text

              - Require py-cidr >= 2.7.0 which has ip sort fix
              - update Changelog.rst

* 2025-03-10  : **5.0.0**

.. code-block:: text

              - remove files no longer being used
              - New config file format using single config file shared by dmarc and tls report generators
                   version 1 configs with 2 files will be automatically converted and saved as config.v2
                   Auto conversion pulls in new dependency on tomli-w to write the config file.
                Reorg and simplify config and options code.
 2025-02-25   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-02-25  : **4.13.2**

.. code-block:: text

              - Small update to README
 2025-02-23   ⋯

.. code-block:: text

              - Add html and pdf docs to repo
              - update Changelog.rst

* 2025-02-23  : **4.13.1**

.. code-block:: text

              - Change to py-cidr package for network tools.
                Update README
 2025-01-11   ⋯

.. code-block:: text

              - update Changelog.rst

* 2025-01-11  : **4.12.5**

.. code-block:: text

              - Ensure python version requirement is consistent (README, pyproject, PKGBUILD, requirements)
 2024-12-31   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-12-31  : **4.12.4**

.. code-block:: text

              - Add git signing key to Arch Package
              - update Changelog.rst

* 2024-12-31  : **4.12.3**

.. code-block:: text

              - typo
              - update Changelog.rst

* 2024-12-31  : **4.12.2**

.. code-block:: text

              - Add validpgpkeys to PKGBUILD
              - update Changelog.rst

* 2024-12-31  : **4.12.1**

.. code-block:: text

              - All git tags are now signed.
                Update SPDX tags
 2024-11-28   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-11-28  : **4.12.0**

.. code-block:: text

              - Handle another seconds format in xml file
 2024-10-22   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-10-22  : **4.11.0**

.. code-block:: text

              - Additional input protections in cidr utils
              - update Changelog.rst

* 2024-10-22  : **4.10.0**

.. code-block:: text

              - Bug fix when no "dom_ips" set. Resolves issue #2 reported by @g4242
 2024-10-20   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-10-20  : **4.9.0**

.. code-block:: text

              - remove dead code
              - update Changelog.rst

* 2024-10-20  : **4.8.0**

.. code-block:: text

              - For completeness, Handle ip address of form ip/prefix
 2024-10-19   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-10-19  : **4.7.0**

.. code-block:: text

              - Now use python 3s ipaddress module instead of netaddr.
                  Its faster and we no longer require 3rd party module
                Require python version 3.11 or later
 2024-08-29   ⋯

.. code-block:: text

              - update Changelog.rst

* 2024-08-29  : **4.6.0**

.. code-block:: text

              - Switch to lxml for better handling of namespaces found in some reports
                Now handle namespaces (e.g. GMX uses them)
 2023-12-26   ⋯

.. code-block:: text

              - update Changelog.rst

* 2023-12-26  : **4.3.1**

.. code-block:: text

              - Add missing dateutil to depends in PKGBUILD
 2023-12-10   ⋯

.. code-block:: text

              - update Changelog.rst

* 2023-12-10  : **4.3.0**

.. code-block:: text

              - Add support for extracting reports from multiple emails saved into an mbox file - evolution saves emails this way
 2023-11-28   ⋯

.. code-block:: text

              - update Changelog.rst

* 2023-11-28  : **4.2.0**

.. code-block:: text

              - Handle badly formed dmarc report with missing date range
                Switch python build backend to hatch (was poetry)
 2023-10-29   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-10-29  : **4.0.0**

.. code-block:: text

              - Improve tls-rpt
                      Show policy name (tlsa, sts, none)
                      Show count of each failure result type
                      Now checks all "policies" returned in the json report.
                      Add date ranges to report
 2023-09-27   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-09-27  : **3.10.0**

.. code-block:: text

              - Reorganize documentation under Docs and migrate to restructured text
 2023-07-14   ⋯

.. code-block:: text

              - Nicer formatting in README-tls.rst
              - update CHANGELOG.md

* 2023-07-14  : **3.9.2**

.. code-block:: text

              - Change to 3.9.2
              - update CHANGELOG.md

* 2023-07-14  : **3.9.1**

.. code-block:: text

              - With updated README-tls.rst this time
              - update CHANGELOG.md

* 2023-07-14  : **3.9.0**

.. code-block:: text

              - Update README with better description of TLS Report and use rst
 2023-07-09   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-07-09  : **3.8.0**

.. code-block:: text

              - Add any failure details to tls report
 2023-05-18   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-05-18  : **3.7.1**

.. code-block:: text

              - Update build info in README
              - update CHANGELOG.md

* 2023-05-18  : **3.7.0**

.. code-block:: text

              - install: switch from pip to python installer package. This adds optimized bytecode
              - update CHANGELOG.md

* 2023-05-18  : **3.6.3**

.. code-block:: text

              - PKGBUILD: add python-build to makedepends
              - update CHANGELOG.md

* 2023-05-18  : **3.6.2**

.. code-block:: text

              - PKGBUILD: build wheel back to using python -m build instead of poetry
 2023-05-17   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-05-17  : **3.6.1**

.. code-block:: text

              - Simplify Arch PKGBUILD and more closely follow arch guidelines
 2023-04-29   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-04-29  : **3.6.0**

.. code-block:: text

              - Handle exceptions from bad XML report files
 2023-01-21   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-01-21  : **3.5.0**

.. code-block:: text

              - Remove duplicate line in options class - has no effect
 2023-01-17   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-01-17  : **3.4.0**

.. code-block:: text

              - Turn off debug - accidently left on with last release! So sorry
 2023-01-12   ⋯

.. code-block:: text

              - typo in README-mta-sts.md
 2023-01-09   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-01-09  : **3.3.0**

.. code-block:: text

              - More info about selectors including missing ("-")
              - update CHANGELOG.md

* 2023-01-09  : **3.2.0**

.. code-block:: text

              - Add more info about dkim selectors typically from forwarded mail
              - update CHANGELOG.md

* 2023-01-09  : **3.1.0**

.. code-block:: text

              - Sort short dkim selector tags before printing
 2023-01-07   ⋯

.. code-block:: text

              - tweak readme for new tls-rpt tool
              - update CHANGELOG.md

* 2023-01-07  : **3.0.0**

.. code-block:: text

              - Refactor code some.
                Add new tls-rpt to generate reports for MTA-STS TLS reports
              - update CHANGELOG.md

* 2023-01-07  : **2.3.0**

.. code-block:: text

              - Bug fix - clean up went too far added silly print bug - so sorry
 2023-01-06   ⋯

.. code-block:: text

              - tidy README, add SPDX license line to missed file
              - update CHANGELOG.md

* 2023-01-06  : **2.2.1**

.. code-block:: text

              - Use SPDX licensing.
                Lint and tidy
 2023-01-05   ⋯

.. code-block:: text

              - Fix description of input file disposition to show none,save,delete
              - update CHANGELOG.md

* 2023-01-05  : **2.2.0**

.. code-block:: text

              - Add option for disposition of input files after report is generated.
                   --inp_files_disp can be none, save or delete.  Default is none.
                   --inp_files_save_dir specifies where to save input files when disposition is "save"
 2023-01-03   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-01-03  : **2.1.0**

.. code-block:: text

              - Right align numbers
              - small tweak to README
              - update CHANGELOG.md

* 2023-01-03  : **2.0.0**

.. code-block:: text

              - Fix bug where grand total missed orgs with 1 IP
                Add color report, default theme is dark. Can be light, dark or none to turn color off
                Add support for config files: /etc/dmarc_report/config - ~.config/dmarc_report/config
                  Config file is TOML format where each variable is the long_option name:
                  e.g. dir = "/a/b/dmarc_stuff"
                Add new option to set your IP or CIDR blocks - this will allow your own IPs to be colored
                  Makes it easy to spot mail generated from your own IP vs mail lists etc
              - update CHANGELOG.md

* 2023-01-03  : **1.3.1**

.. code-block:: text

              - Improve report format a bit
 2023-01-02   ⋯

.. code-block:: text

              - typo
              - small README tweak
              - update CHANGELOG.md

* 2023-01-02  : **1.3.0**

.. code-block:: text

              - silly bug with multipart accidenlty ignoring report file
              - update CHANGELOG.md

* 2023-01-02  : **1.2.1**

.. code-block:: text

              - remove reference to ripmime - no longer needed now that we handle mime attachments ourselves
              - update CHANGELOG.md

* 2023-01-02  : **1.2.0**

.. code-block:: text

              - Fix bug with some multipart mime email from some reporters
              - update CHANGELOG.md

* 2023-01-02  : **1.1.0**

.. code-block:: text

              - *.eml* files are now removed after the dmarc report is extracted.
                   Use option *-k, --keep* to prevent the *.eml* being removed
              - update CHANGELOG.md

* 2023-01-02  : **1.0.0**

.. code-block:: text

              - Added support to extract dmarc reports from mime attachments in email files
                    Added option *-d, --dir* to specify the directory containing report files
              - more readme tweaks
              - tweak readme
              - update CHANGELOG.md

* 2023-01-02  : **0.9.1**

.. code-block:: text

              - Add note on handling email reports efficiently to README
 2023-01-01   ⋯

.. code-block:: text

              - remove unused file
              - update CHANGELOG.md

* 2023-01-01  : **0.9.0**

.. code-block:: text

              - Small tweak to report output
              - fix typo
              - update CHANGELOG.md

* 2023-01-01  : **0.8.1**

.. code-block:: text

              - update readme
              - update CHANGELOG.md

* 2023-01-01  : **0.8.0**

.. code-block:: text

              - bump vers to 0.8.0
              - update CHANGELOG.md

* 2023-01-01  : **0.7.0**

.. code-block:: text

              - prep for release

* 2023-01-01  : **0.6.0**

.. code-block:: text

              - initial commit


