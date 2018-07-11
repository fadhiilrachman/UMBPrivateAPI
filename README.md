# UMB Private API

 [![Version 1.0.1](https://img.shields.io/badge/beta-1.0.1-brightgreen.svg "Version 1.0.1")](https://pypi.python.org/pypi/umb) [![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg "LICENSE")](https://github.com/fadhiilrachman/UMBPrivateAPI/blob/master/LICENSE) [![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
 
UMB information system's private API based on their mobile application

----

This work is **no way** affiliated with Mercu Buana University or PT. Sentra Vidya Utama (SEVIMA). These files are the results of research into the UMB Mobile application.

## Requirement

The umb module only requires Python 3. You can download from [here](https://www.python.org/downloads/). 

## Installation

Installation is simple. It can be installed from pip using the following command:
```sh
$ pip install umb
```
Or from the code:
```sh
$ python setup.py install
```

## Usage

```python
>>> from umb import *
>>> umb = UMB()
>>> login = umb.login('username', 'password')
>>> log(login.json)
```

### Examples

All examples can be found [here](https://github.com/fadhiilrachman/UMBPrivateAPI/tree/master/examples).

## Updates

From pip using the following command:
```sh
$ pip install umb --upgrade
```

## Author
Fadhiil Rachman / [@fadhiilrachman](https://www.instagram.com/fadhiilrachman)