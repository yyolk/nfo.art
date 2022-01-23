from nfo_art import EOF_BYTE
from nfo_art.re import eof_pattern

import pytomlpp

example_root_scalars = "sketch/eof_toml.nfo"
example_root_map = "sketch/eof_toml_title_mapping.nfo"


def _loads_nfo_from_toml(fp):
    return pytomlpp.loads(fp.read().decode("utf-8"))


def _seek_to_EOF(fp):
    while (file_eof := r.read(1)) != EOF_BYTE:
        pass


def _main_stuff(nfo):
    """
    do stuff with nfo
    """
    print(nfo)
    print(nfo.get("artist"))


with open(example_root_scalars, "rb") as r:
    raw_nfo = _seek_to_EOF(r)
    nfo = _loads_nfo_from_toml(r)
    _main_stuff(nfo)


with open(example_root_map, "rb") as r:
    _seek_to_EOF(r)
    nfo = _loads_nfo_from_toml(r)
    _main_stuff(nfo)


with open(example_root_scalars, "rb") as r:
    # this method would allow for mutliple EOF markers
    # could keep backwards compatibility with SAUCE
    # but we don't need to
    raw_nfo = eof_pattern.split(r.read())[-1]
    nfo = pytomlpp.loads(raw_nfo.decode("utf-8"))
    _main_stuff(nfo)
