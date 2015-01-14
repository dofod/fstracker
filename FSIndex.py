from FSUtils import readConfiguration
import json
import os
import hashlib
import copy

class FSIndex:
	settings = {}
	index = {}
	def __init__(self, settingsFilePath):
		self.settings = readConfiguration(settingsFilePath)

	def _getHash(self, filepath):
		return hashlib.md5(open(filepath).read()).hexdigest()

	def get(self):
		return self.index

	def write(self):
		indexFile = open(self.settings['local']['index'], 'w')
		indexFile.write(json.dumps(self.index))
		indexFile.close()

	def read(self):
		indexFile = open(self.settings['local']['index'])
		self.index = json.loads(indexFile.read())
		indexFile.close()

	def generate(self):
		rootdir = self.settings['local']['root'].strip('"').strip('\\')
		self.index = {}
		for root, subdirs, files in os.walk(rootdir):
			for f in files:
				self.index[self._getHash(os.path.join(root,f))] = os.path.join(root, f).replace(rootdir, '')

	def compare(self):
		self.generate()
		self.write()
		self.read()
		oldIndex = copy.deepcopy(self.index)
		self.generate()
		for key, value in self.index.iteritems():
			if key not in oldIndex:
				print value