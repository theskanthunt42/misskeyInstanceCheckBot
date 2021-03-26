"""M E T H"""
import math

def filesize(size_bytes):
    #pylint: disable=invalid-name
    """
    Convert filesize into readable human unit system\n
    ref: https://stackoverflow.com/a/52002551\n
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def big_number(num):
    """
    Pretty print big numbers.\n
    E.g. 1145141919810 -> 1.15T\n
    ref: https://stackoverflow.com/a/45846841\n
    """
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return \
        '{}{}'.format(\
            '{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
