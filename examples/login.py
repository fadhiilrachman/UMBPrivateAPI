# -*- coding: utf-8 -*-
from umb import *

# deklarasi class UMB
umb = UMB()
username = '41516010040'
password = 'passwordku'

# panggil fungsi login dari class umb
login = umb.login(username, password)

# buat logger untuk mode CLI
log(login.json)