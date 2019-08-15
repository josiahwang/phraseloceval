# -*- coding: utf-8 -*-
"""
Author: Josiah Wang (http://www.josiahwang.com)

Dataset: a class for representing a Dataset

DatasetLoader: utility/factory class to load a dataset from a preformatted text or json file

"""

import json
import sys
import codecs

if sys.version_info[0] < 3:
	open = codecs.open;

class Dataset(object):
	""" A class for representing a Dataset
	"""

	def __init__(self):
		self._instances = [];
	
	
	def add_instance(self, propertyDict):
		""" Append an instance to the dataset.
		
		Parameters
		----------
		propertyDict : dict
			a dictionary containing the following key/values (minimum)
				"phrase" : str
				"image" : str
				"box" : [x,y,w,h] where (x,y) are coordinates of the top-left of the bounding box and (w, h) are the width and height of the bounding box
		"""
		
		self._instances.append(propertyDict);
	
	
	def get_phraselist(self):
		return [instance["phrase"] for instance in self._instances];
	
	
	def get_imagelist(self):
		return [instance["image"] for instance in self._instances];
	
	
	def get_boxlist(self):
		return [instance["box"] for instance in self._instances];
	
	
	def get_instances(self):
		return self._instances;
	
	
	def get_count(self):
		return len(self._instances);
	
	count = property(get_count);
	size = property(get_count);
	instances = property(get_instances);
	phrases = property(get_phraselist);
	images = property(get_imagelist);
	boxes = property(get_boxlist);


class DatasetLoader:
	""" Utility/factory class to load a Dataset object from a preformatted text or json file
	"""

	def __init__(self):
		pass;

	def read_text(self, filePath): 
		""" Loads a Dataset object from a text file.
		
		Parameters
		----------
		filePath : str
			Path to text file containing the dataset.
			Format of text file: image_id \t phrase \t x \t y \t w \t h 
	
		Returns
		-------
		Dataset
			A Dataset instance, loaded with rows from filePath
		"""
		
		dataset = Dataset();
		for line in open(filePath):
			data = line.strip().split("\t");
			dataset.add_instance({
				"image": data[0],
				"phrase": data[1],
				"box": list(map(float, data[2:6]))}
			);
		return dataset;
	
	
	def read_json(self, jsonFilePath): 
		""" Loads a Dataset object from a json file.
		
		Parameters
		----------
		filePath : str
			Path to json file containing the dataset.
			Minimum format of json file: [{"image": "456329#0", "phrase": "My phrase", "box": [1, 4, 200, 300]}, ...];
					there can be other keys in each entry, it will simply be ignored in this code
		
		Returns
		-------
		Dataset
			A Dataset instance, loaded with rows from filePath
		"""
		
		dataset = Dataset();
		obj = json.load(open(jsonFilePath, encoding="utf-8"));
		for entry in obj:
			dataset.add_instance(entry);
		return dataset;

