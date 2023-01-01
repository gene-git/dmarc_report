#!/usr/bin/python
"""
 DMARC report options
"""
# pylint: disable=R0903

import argparse

class DmarcOpts:
    """ cmmand line options """

    def __init__(self):
        self.verb = False
        self.dmarc_fails = False
        self.dkim_fails = False
        self.spf_fails = False

        par = argparse.ArgumentParser(description='dmarc-rpt')
        par.add_argument('-v','--verb',
                        action = 'store_true',
                        help='More verbose')

        par.add_argument('-fdm','--dmarc_fails',
                        action = 'store_true',
                        help='Only report dmarc fails')

        par.add_argument('-fdk','--dkim_fails',
                        action = 'store_true',
                        help='Only report dkim fails')

        par.add_argument('-fsp','--spf_fails',
                        action = 'store_true',
                        help='Only report spf fails')

        parsed = par.parse_args()
        if parsed:
            for (opt,val) in vars(parsed).items() :
                setattr(self, opt, val)
