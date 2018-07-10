.. contents::

UMB information system's private API

**Homepage**: https://github.com/fadhiilrachman/UMBPrivateAPI

Requirements
============
The UMB module only requires Python 3

Installation
============
Installation is simple. It can be installed from pip using the following
command::

    $ pip install umb

Or from the terminal::

    $ python setup.py install

Usage
============
::

    >>> from umb import *
    >>> umb = UMB()
    >>> login = umb.login('username', 'password')
    >>> log(login.json)

All examples can be found `here <https://github.com/fadhiilrachman/UMBPrivateAPI/tree/master/examples>`_.