from nfo_art import EOF_BYTE
from nfo_art.re import eof_pattern

import pytomlpp

example_root_scalars = "sketch/eof_toml.nfo"
example_root_map = "sketch/eof_toml_title_mapping.nfo"


def _loads_nfo_from_toml(s):
    return pytomlpp.loads(s.decode("utf-8"))


def _seek_to_EOF(fp):
    while r.read(1) != EOF_BYTE:
        pass

def _regex_split_EOF(fp):
    raw_nfo = eof_pattern.split(r.read())[-1]
    return raw_nfo

def _main_stuff(nfo):
    """
    do stuff with nfo
    """
    print(nfo)
    print(nfo.get("artist"))


with open(example_root_scalars, "rb") as r:
    raw_nfo = _seek_to_EOF(r)
    nfo = _loads_nfo_from_toml(r.read())
    _main_stuff(nfo)


with open(example_root_map, "rb") as r:
    _seek_to_EOF(r)
    nfo = _loads_nfo_from_toml(r.read())
    _main_stuff(nfo)


with open(example_root_scalars, "rb") as r:
    # this method would allow for mutliple EOF markers
    # could keep backwards compatibility with SAUCE
    # but we don't need to
    raw_nfo = _regex_split_EOF(r)
    nfo = _loads_nfo_from_toml(raw_nfo)
    _main_stuff(nfo)
