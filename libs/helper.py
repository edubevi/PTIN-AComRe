from pathlib import Path

def file_lines(fname):
    x = 0
    with open(fname) as f:
        for (x, l) in enumerate(f):
            pass
    return x + 1

def dd2dms(dd):
    is_positive = dd >= 0
    dd = abs(dd)
    (minutes, seconds) = divmod(dd * 3600, 60)
    (degrees, minutes) = divmod(minutes, 60)
    degrees = (degrees if is_positive else -degrees)
    return degrees, minutes, seconds
