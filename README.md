**Everything below represents aspirational goals for this module, and has not
necessarily been implemented yet**

Currently working features:

- Parsing some datetime objects (timedelta, simple times, simple dates)
- Parsing decimal values in decima.Decimal objects

# cjsonx

This module is a modified version of Dan Pascu's cjson module for Python, which
is available in the Python Package Index: https://pypi.python.org/pypi/python-cjson

This version provides a couple of minor extensions to the JSON standard, as well
as support for checking the `__json__` method of non-builtin object types that are
being encoded to JSON.

## Extensions to JSON

This module provides for two non-standard extensions to JSON syntax,
specifically aimed at encoding and moving around Python data. Those extensions
are:

* Datetime/date/time/timedelta encoding.
* Decimal notation for numbers

These are mostly present as convenience for instances where JSON is being passed
between Python processes (JavaScript, of course, has no concept of decimals as
distinct from floats). Furthermore, for highly complex serialization of Python
objects, the Pickle and cPickle modules are probably your best bet, but this has
the advantage of being more human-friendly notation.

### Datetime/date/time/timedelta syntax

#### Datetime

The basic syntax is as follows:
```
{
    "key_name": d"YYYY-MM-DD HH:MM:SS:UUUUUU"
}
```
where 'YYYY' is the year, 'MM' the date, 'DD' the numerical day, 'HH' the hour,
'MM' the minute, 'SS' the seconds, and 'UUUUUU' the microseconds. All are zero-
padded numbers. The microseconds can be left off (resulting in
`YYYY-MM-DD HH:MM:SS`) and a value of zero will be assumed.

Any string matching these rules will result in a Python `datetime` object.

#### Date

If you leave off the time portion (including any time zone information), the
string will be parsed into a `date` object. For example:
```
{
    "key_name": d"YYYY-MM-DD"
}
```

Trailing spaces or any other extra characters will result in an error.

#### Time and timedelta

Furthermore, the date portion (and any preceding space) may be dropped for a
`time` object, like so:
```
{
    "key_name": d"HH:MM:SS:UUUUUUT±HH:MM"
}
```

As before, microseconds and time zone information are optional, and will be
included only if they are specified.

`timedelta` objects can be encoded using a similar syntax, by preceding the time
notation with a '+' or '-'. In place of hours, minutes, or seconds, only the
fields days, seconds, and microseconds are specified. That would look something
like this:
```
{
    "key_name": d"±DD:SS:UUUUU"
}
```
Days must not be omitted (although it can be zero) and need not be zero-padded.
Seconds and microseconds must not be omitted either (again, can be zero and/or
one digit wide).

### Decimal syntax

Numbers preceded with a 'D' will be parsed as `Decimal` objects. The syntax is:
```
{
    "some_key": D1.0
}
```

There is no limit on the number of decimal places, and `D0.1` is just as valid
as `D.1` (although the encoder will always enter a leading zero before the
decimal portion of the number).

### The `__json__` method

The original `cjson` module has no support for objects which are not built-in
Python types. To ease this problem slightly, `cjsonx` will first attempt to find
and call the `__json__` method on any object passed into it (this also allows
you to override the default parsing behaviour of builtins).

This magic method should return a value that is parseable itself (ie, a dict,
list, array, date, time, timedelta, datetime, or Decimal object) or a completely
parsed string (which also fulfills the first criteria, and will be returned as-
is). Returning anything else will result in an EncodeError being thrown.

## License

All code in this module is licensed under the LGPLv2.0 (see the LICENSE.md file
for more information).

## Authorship

Original `cjson` module code is copyright (C) 2006-2007 Dan Pascu.

Modifications and extenions are copyright (C) 2013 Michael C Schuller.

## Bug reports, suggestions, contributions

Should all be filed on the issues page of the github project, which can be
found at:

https://github.com/petronius/cjsonx/

## Original README:

This module implements a very fast JSON encoder/decoder for Python.

JSON stands for JavaScript Object Notation and is a text based lightweight
data exchange format which is easy for humans to read/write and for machines
to parse/generate. JSON is completely language independent and has multiple
implementations in most of the programming languages, making it ideal for
data exchange and storage.

The module is written in C and it is up to 250 times faster when compared to
the other python JSON implementations which are written directly in python.
This speed gain varies with the complexity of the data and the operation and
is the the range of 10-200 times for encoding operations and in the range of
100-250 times for decoding operations.
