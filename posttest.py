# -*- coding: utf-8 -*- 

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ('StartStation','2f940836-cedc-41ef-8e28-c2336ac8fe68'),
    ('EndStation','e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'),
    ('SearchDate','2016/09/05'),
    ('SearchTime','14:30'),
    ('SearchWay','DepartureInMandarin')

    ])
req.add_header('Origin','http://www.thsrc.com.tw')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
resp = urlopen(req, data=postData.encode('utf-8'))

print(resp.read().decode('utf-8'))