"""
Abstract:

    if i define one of
        - artist
        - author
        - ...
    treat them as the same

"""

class Piece:
    url: str
    created_by: Artist | Collective
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
    artists: list[Artist]
    ...


Group = Collective
