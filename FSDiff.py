from FSIndex import FSIndex
from FSUtils import readConfiguration
import json

class FSDiff:
	settingsFilePath = ''
	changes = {}
	newFiles = {}
	deletedFiles = {}
	def __init__(self, settingsFilePath):
		self.settingsFilePath = settingsFilePath

	def diff(self):
		oldIndex = FSIndex(self.settingsFilePath)
		newIndex = FSIndex(self.settingsFilePath)
		oldIndex.read()
		newIndex.generate()

		for hashkey, path in newIndex.get().iteritems():
			if hashkey not in oldIndex.get():
				self.changes[path] = hashkey

		for path, hashkey in self.changes.iteritems():
			if path not in oldIndex.get().values():
				self.newFiles[path] = hashkey

		for hashkey, path in oldIndex.get().iteritems():
			if path not in newIndex.get().values():
				self.deletedFiles[path] = hashkey

		print json.dumps(self.deletedFiles, sort_keys=True, indent=4)
		print json.dumps(self.newFiles, sort_keys=True, indent=4)
		#print json.dumps(self.changes, sort_keys=True, indent=4)