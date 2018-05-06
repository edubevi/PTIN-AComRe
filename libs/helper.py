import random
import string

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


def random_dni():
    return (lambda x: '%s%s' % (x, "TRWAGMYFPDXBNJZSQVHLCKE"[x % 23]))(random.randint(10000000, 99999999))


def spawn_position(building=random.choice(['A', 'B', 'Neapolis'])):
    internal_lat = internal_long = 0.0
    if building == 'A':
        internal_lat = random.uniform(41.221814, 41.220892)
        internal_long = random.uniform(1.730924, 1.729499)
    elif building == 'B':
        internal_lat = random.uniform(41.223351, 41.223314)
        internal_long = random.uniform(1.736664, 1.734798)
    elif building == 'Neapolis':
        internal_lat = random.uniform(41.223760, 41.222952)
        internal_long = random.uniform(1.734363, 1.732982)
    return internal_lat, internal_long


def jsonfy_data(id, type, name):
    return {'id': id,
            'type': type,
            'name': name}