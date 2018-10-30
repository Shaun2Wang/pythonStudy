#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from pprint import pprint


url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url, verify=False)

# \| 为|，ASD|asd为匹配的对象
stations = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
print(stations)
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys()))
# pprint(stations, indent=4)
#重定向(在Windows命令行) python parse_station.py > stations.py