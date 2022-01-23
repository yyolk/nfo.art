"""
Abstract:

    if i define one of
        - artist
        - author
        - ...
    treat them as the same

"""
from typing import List

# from enum import Enum, auto


class Piece:
    url: str
    ...


Film = Piece
Image = Piece
Picture = Piece
...


class Artist:
    name: str
    ...


Author = Artist


class Collective:
    artists: List[Artist]
    ...


Group = Collective
