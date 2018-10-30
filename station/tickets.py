#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help 显示帮助菜单
    -g        高铁
    -d        动车
    -t        特快
    -k        快速
    -z        直达

Example:
    tickets beijing shanghai 2016-09-11
"""

from docopt import docopt
from stations import stations
import requests
from prettytable import PrettyTable


calss TrainCollention(object):
    header = 'train station time duration frist second softsleep hardsleep hardsit'.split()
    def __init__(self, rows):
    	self.rows = rows
    def _get_duration(self.row)

def cli():

    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # 构建URL
    url = 'https://kyfw.12306.cn / otn / lcxxcx / query?purpose_codes = ADULT & queryDate = {} & from_station ={} & to_station = {}'.format(
        date, from_station, to_station)
    r = requests.get(url, verify=False)
    rows = r.json()['data']['datas']
    trains = TrainCollention(rows)
    trains.pretty_print()

if __name__ == '__main__':
    cli()
