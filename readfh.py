#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open(r'C:\Resources\test.txt','rb') as f:
	data = f.read().decode('utf-8')
fh = re.findall(r'([A-Z|a-z]{3,4}-?\d{3,4})', data)
with open(r'C:\Resources\Deyz\pythonStudy\fh.txt','a') as f:
	for a in fh:
		f.write('{}\n'.format(a))
