# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
"""
class_print.py
 Screen output with color
 Output sent to stdout
 Colors are turned off if non-tty
"""
# pylint: disable=too-many-locals
from typing import (Dict, Optional, Tuple)
import sys
from .color_pick import color_pick


def rpt_colors(theme: str) -> Dict[str, str]:
    """
    Colors for report
    """
    light = ''
    if theme and theme.lower().startswith('l'):
        light = 'l'
    rpt_map = {
            'org': 'tan' + light,
            'dom': 'cyan' + light,
            'okay': 'green' + light,
            'warn': 'warn' + light,
            'error': 'error' + light,
            }
    return rpt_map


class AscCol:
    """
    Simple Ascii Color Map
    """
    # pylint: disable=R0903
    def __init__(self, theme):
        self.theme = theme
        self.color_map = {
                'blue': 27,
                'cyan': 51,
                'cyanl': 39,
                'green': 10,
                'greenl': 2,
                'orange': 9,
                'pink': 13,
                'redl': 196,
                'red': 196,
                'tan': 208,
                'tanl': 131,
                'yellow': 11,
                'yellowl': 13,
                'white': 254,
                'warn': 11,
                'warnl': 13,
                'fail': 160,
                'error': 196,
                'errorl': 196,
                'info': 208,
                'hdr': 227,
                }
        # List of known colors
        self.col_list = list(self.color_map.keys())
        self.rpt_color_map = rpt_colors(theme)
        self.rpt_col_list = list(self.rpt_color_map.keys())

    def _lookup_color_number(self, color: str) -> int:
        """
        Maps color name to ascii color number (256 color)
        """
        if self.theme and self.theme.lower().startswith('l'):
            color_num = 0  # black
        else:
            color_num = 254  # white

        if isinstance(color, str):
            # match color and retrieve it's ascii color number
            # - number -
            # - report keys
            # - any known color
            # default fg for theme

            #
            # check if its a report color name
            #
            color_rpt = color_pick(color, self.rpt_col_list)
            if color_rpt:
                color = self.rpt_color_map[color_rpt]

            color_matched = color_pick(color, self.col_list)
            if color_matched:
                color_num = self.color_map[color_matched]
            else:
                if self.theme and self.theme.lower().startswith('l'):
                    color_num = 0       # unknown - make it black
                else:
                    color_num = 254     # unknown - make it white
        return color_num

    def colorize(self, txt: str, fg_col: str = '', bg_col: str = '',
                 bold: bool = False) -> Tuple[str, int]:
        """
        Colorize a string using 256 color ascii escapes.

        Colors are a few names or digit from 0-255

        Return:
            (str, int):
            colorized text and number of additional chars
            used to make any color.
            "clen" needed to keep format widths correct
        """
        esc = '\033['
        set_fg = '38;5;'
        set_bg = '48;5;'
        set_off = '0'
        # under = '\033[4m'

        clen = 0

        set_bold = ''
        color_fg = ''
        color_bg = ''
        if bold:
            set_bold = ';1'

        if fg_col:
            color_fg_num = self._lookup_color_number(fg_col)
            color_fg = f'{set_fg}{color_fg_num}'

        if bg_col:
            color_bg_num = self._lookup_color_number(bg_col)
            color_bg = f'{set_bg}{color_bg_num}'

        if fg_col or bg_col or bold:
            lbefore = len(txt)
            txt = f'{esc}{color_fg}{color_bg}{set_bold}m{txt}{esc}{set_off}m'
            lafter = len(txt)
            clen = lafter - lbefore

        return (txt, clen)


class Prnt:
    """
    Prnt class - handles screen writes
    see prnt() and companion methods
    """
    # pylint: disable=R0903
    def __init__(self, theme: str):
        self.color = AscCol(theme)
        self.fpo = sys.stdout
        self.tty = False
        self.theme = theme

        if self.fpo.isatty():
            self.tty = True

    def prnt(self, txt: str,
             fg_col: Optional[str] = '',
             bg_col: Optional[str] = '',
             bold: Optional[bool] = False):
        """
        Handles the work for messages with header or footer (dashes)

        txt can be string or list of strings
        Single string can contain newlines.
            fg: ascii color uses first letter or use number 0-254 (Default 'w')
                      blue Bold cyan fail red green head under warn
        """
        # pylint: disable=R0913
        (txt, _clen) = self.colorize(txt, fg_col=fg_col, bg_col=bg_col,
                                     bold=bold)
        self.fpo.write(txt)
        self.fpo.flush()

    def colorize(self, txt, fg_col=None, bg_col=None, bold=False
                 ) -> Tuple[str, int]:
        """ colorize text without printing """
        clen = 0
        if self.tty and self.theme:
            (txt, clen) = self.color.colorize(txt, fg_col=fg_col,
                                              bg_col=bg_col, bold=bold)
        return (txt, clen)
