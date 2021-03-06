#!/usr/bin/python

import boto3
import logging


class DBS3:

	def __init__(self,bucket):
		self.log = logging.getLogger("DB.S3")
		self.bucket = bucket

		self.client = boto3.client('s3')

class DBMemory:

	def __init__(self):
		self.log = logging.getLogger("DB.Memory")
		self.db = {}

	def updatePage(self,page,user,body):
		if not page in self.db:
			self.db[page]=[]
		self.db[page].insert(0,{'user':user,'body':body})

	def getPage(self,page):
		if page in self.db:
			return self.db[page][0]
		return None

	def doesPageExist(self,page):
		return page in self.db

	def listPageVersions(self,page):
		if not page in self.db:
			return []

		ret = []
		ret.extend(self.db[page])
		ret.reverse()

		return ret

	def getPageVersion(self,page,version):
		if page in self.db and version<=len(self.db[page]):
			return self.db[page][len(self.db[page])-version]
		return None
