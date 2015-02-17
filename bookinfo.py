from abc import ABCMeta, abstractmethod

class bookinfo(object):
	__metaclass__ = ABCMeta
	
	def __init__(self):
		self.info_type=dict()
		self.rtn_res=[]

	@abstractmethod		
	def search(key): pass


