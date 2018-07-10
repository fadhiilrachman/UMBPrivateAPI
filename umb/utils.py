# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re, sys
from datetime import datetime

PY3 = sys.version_info[0] == 3

def log(text, show_time=False):
	t=''
	if show_time:
		t+="[%s] " % str(datetime.now())
	t+="%s" % text
	print(t)

def is_data_exist(file, data):
	with open(file, 'r') as exist:
		rd = exist.read()
		if re.search(data, rd):
			return True
		else:
			return False
def gen_nim_mhs(prog, dept, year, class_, no):
	num_no=list(str(no))
	nums=len(num_no)
	if nums == 1:
		num='000%s' % str(no)
	elif nums == 2:
		num='00%s' % str(no)
	elif nums == 3:
		num='0%s' % str(no)
	else:
		num=no
		nim='%s%s%s%s%s' % (prog, dept, year, class_, num)
	return nim

def to_snake_case(text):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()