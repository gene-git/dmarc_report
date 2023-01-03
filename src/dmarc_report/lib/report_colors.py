"""
 Colors used for dmarc, dkim and spf
"""
def dmarc_colors(cnt, passes, fails, pass_pct):
    """
    Colors for DMARC column
    """
    if passes == cnt:
        color = 'okay'

    elif passes == 0:
        color = 'error'

    else:
        color = 'warn'

    return color

def dkim_colors(cnt, passes, fails, aligns):
    """
    Set dkim colors for pass, fail, align 
     - dkim may have more than 1 selector
       Can have passes == cnt and also have fails on second selector
       Common when there is 1 RSA and 1 ED25519 selector
    """
    #
    # Passes
    #
    if passes >= cnt:
        color_pass = 'okay'

    elif passes == 0:
        color_pass = 'error'

    else:
        color_pass = 'warn'

    #
    # Fails
    #
    if fails == 0:
        color_fail = 'okay'

    elif fails > 0:
        color_fail = 'warn'

    if aligns >= cnt:
        color_align = 'okay'

    elif aligns == 0:
        color_align = 'error'
    else:
        color_align = 'warn'

    return (color_pass, color_fail, color_align)

def spf_colors(cnt, passes, fails, aligns):
    """
    Set dkim colors for pass, fail, align 
     - dkim may have more than 1 selector
       Can have passes == cnt and also have fails on second selector
       Common when there is 1 RSA and 1 ED25519 selector
    """
    #
    # Passes
    #
    if passes == cnt:
        color_pass = 'okay'

    elif passes == 0:
        color_pass = 'error'

    else:
        color_pass = 'warn'

    #
    # Fails
    #
    if fails == 0:
        color_fail = 'okay'

    elif fails == cnt:
        color_fail = 'error'

    else:
        color_fail = 'warn'

    if aligns == cnt:
        color_align = 'okay'

    elif aligns == 0:
        color_align = 'error'
    else:
        color_align = 'warn'

    return (color_pass, color_fail, color_align)




