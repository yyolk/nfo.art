# [nfo.art][nfo.art]


# Example `art.nfo`

See `sketch/eof_toml.nfo`.

<!-- TODO: See `art.nfo`. -->

## Literal File Structure

Following SAUCE, do whatever you want ahead.
Since all ANSI art intepreters do per-byte recognitions, and usually ignore,
and usually stop on the literal `EOF` character `\x1a`, `^Z`.

With any number of formats that can be attached today without necessarily
limited by the amount of characters that SAUCE was limiting it to.

TOML seems the most obvious with nfo.art and `art.nfo`'s use case is to expand
artist's creativity in the releases through [clever.gallery][clever.gallery]

## Test it locally

```sh
# after you setup your preferred venv...
pip install -r requirements.txt
python -m testkit
```


[nfo.art]: https://nfo.art
[clever.gallery]: https://clever.gallery
