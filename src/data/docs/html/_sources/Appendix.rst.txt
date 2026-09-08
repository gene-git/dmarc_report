.. SPDX-License-Identifier: GPL-2.0-or-later


========
Appendix
========

Dependencies
------------

* Run Time :
  * python (3.14 or later)
  * python-dateutil
  * python-lxml
  * py-cidr (2.7.0 or later)
  * tomli-w (for writing version 2 configs converted from version 1)

* Building Package:
  * git
  * meson
  * meson-python
  - rsync


Available
---------

* On `Github <https://github.com/gene-git/dmarc_report>`_
* On `Archlinux AUR <https://aur.archlinux.org/packages/dmarc_report>`_

Installation
------------

On Arch you can build using the PKGBUILD provided in packaging directory or from the AUR package.
To build manually, clone the repo and then::

    ./scripts/do-build
    ./scripts/do-install <destination-dir>

License
-------

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

 * SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright (c) 2023, Gene C 

