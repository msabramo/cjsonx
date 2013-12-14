#!/usr/bin/python

import textwrap

from distutils.core import setup, Extension

__version__ = "0.0.0"

macros = [('MODULE_VERSION', '"%s"' % __version__)]

setup(name         = "python-cjsonx",
      version      = __version__,
      author       = "Michael C Schuller",
      author_email = "petronius@d3mok.net",
      url          = "https://github.com/petronius/cjsonx/",
      download_url = "https://github.com/petronius/cjsonx/",
      description  = "Fast JSON encoder/decoder for Python, with date/time and"
                     "decimal extensions",
      long_description = textwrap.dedent("""
        This module provides an extension to the JSON standard.

        This is a modified version of Dan Pascu's cjson module, and provides a
        couple of minor extensions to the JSON standard (which I am calling JSONX
        for the purposes of the documentation), as well as support for checking the
        __jsonx__ method of non-builtin object types that are being encoded to JSON.
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
      """.strip()),
      license      = "LGPL",
      platforms    = ["Platform Independent"],
      classifiers  = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      ext_modules  = [
        Extension(name='cjsonx', sources=['cjsonx.c'], define_macros=macros)
      ]
)
