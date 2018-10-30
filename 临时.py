# import logging

# LOG_FORMAT="%(asctime)s=====%(levelname)s+++++%(message)s"
# logging.basicConfig(filename="test.log",level=logging.DEBUG,format=LOG_FORMAT)
# logging.debug('this is a debug log.')
# logging.info('this is a info log.')
# logging.warning('this is a warning log.')
# logging.error('this is a error log.')
# logging.critical('this is a critical log.')

# import time
# import threading
# def loop1():
# 	print('loop1 start:',time.ctime())
# 	time.sleep(3)
# 	print('loop1 end ',time.ctime())

# def loop2():
# 	print('loop2 start:',time.ctime())
# 	time.sleep(4)
# 	print('loop2 end ',time.ctime())

# def main():
# 	print('----')

# 	t1=threading.Thread(target=loop1,args=())
# 	t1.start()
# 	t2=threading.Thread(target=loop2,args=())
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print('+++++')
# main()

# import multiprocessing
# from time import ctime, sleep

# class ClockProcess(multiprocessing.Process):
# 	def __init__(self,interval):
# 		super().__init__()
# 		self.interval=interval
# 	def run(self):
# 		while True:
# 			print('time is%s'%ctime())
# 			sleep(self.interval)
# if __name__ == '__main__':
# 	p=ClockProcess(3)
# 	p.start()

# 	while True:
# 		print('sleeping....')
# 		sleep(1)

# def consumer(input_q):
#     print('into consumer:', ctime())
#     while True:
#         item = input_q.get()
#         print('pull', item, 'out of q')
#         input_q.task_done()
#     print('out of consumer:', ctime())

# def producer(sequence, output_q):
#     print('into producer:', ctime())
#     for item in sequence:
#         output_q.put(item)
#         print('put', item, 'into q')
#     print('out of producer:', ctime())

# if __name__ == '__main__':
#     q = multiprocessing.JoinableQueue()
#     cons_q = multiprocessing.Process(target=consumer,args=(q,))
#     cons_q.daemon = True
#     cons_q.start()
#     sequence = [1, 2, 3, 4]
#     producer(sequence, q)
#     q.join()

# def fun_inner():
# 	i =0
# 	while True:
# 		i = yield i
# def fun_outer():
# 	yield from fun_inner()

# if __name__ == '__main__':
# 	outer=fun_outer()
# 	next(outer)

# 	# outer.send(None)
# 	for i in range(5):
# 		print(outer.send(i))
# 	outer.send(None)

# a=iter(range(9))
# print(next(a))
# print(next(a))

# import xml.etree.ElementTree as ET
# tree=ET.parse(r'C:\Users\wx030\Downloads\KML_Samples.kml')
# root=tree.getroot()
# print(root.tag)
# for child in root:
# 	print("***")
# 	print(child.tag,child.attrib)
# 	for grandson in child:
# 		print(grandson.tag,grandson.attrib)
# 	else:
# 		print("****")

# import tkinter
# base=tkinter.Tk()
# base.wm_title("Label test")
# lb=tkinter.Label(base,text='python')
# lb.pack()
# bt=tkinter.Button(base,text='ttt')
# bt.pack()
# menubar=tkinter.Menu(base)
# for item in ['file','Edit','View']:
# 	menubar.add_command(label=item)
# 	base['menu']=menubar
# base.mainloop()

# class XMLNamespaces:
#     def __init__(self, **kwargs):
#         self.namespaces = {}
#         for name, uri in kwargs.items():
#             self.register(name, uri)
#     def register(self, name, uri):
#         self.namespaces[name] = '{'+uri+'}'
#     def __call__(self, path):
#         return path.format_map(self.namespaces)
# ns=XMLNamespaces(html="http://www.opengis.net/kml/2.2")

# tree=ET.parse(r'C:\Users\wx030\Downloads\KML_Samples.kml')
# print(tree.find('{http://www.opengis.net/kml/2.2}kml/Document'))
# print(tree.findtext(ns('{html}kml/{html}Document/{html}name')))

# import xml.etree.ElementTree as ET

# kml=ET.Element('kml')
# Document=ET.SubElement(kml,'Document')
# name=ET.SubElement(Document,'name')
# open1=ET.SubElement(Document,'open')
# name.text='andy'
# ET.dump(kml)

# from urllib import request,parse
# import json

# baseurl='http://fanyi.baidu.com/sug'
# data={
# 	'kw':'girl'
# }
# data=parse.urlencode(data).encode('utf-8')
# header={
# 	'Content-Length':len(data)
# }

# rsp=request.urlopen(baseurl,data=data)
# json_data=rsp.read().decode('utf-8')
# print(type(json_data))
# print(json_data)
# json_data=json.loads(json_data)
# print(type(json_data))

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok('are you ok')

import os
os.chdir(r"C:\Resources\Documents")
for files in os.listdir('.'):
	if files.endswith((".pdf",".PDF")):
		print(files)
