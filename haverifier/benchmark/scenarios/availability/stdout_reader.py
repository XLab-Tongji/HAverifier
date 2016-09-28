import logging
LOG = logging.getLogger(__name__)

class StdoutReader:
	@staticmethod
	def readLineItem(out, key):
		strs = out.split("\n")
		attributes = strs[1].split("|")
		values = strs[3].split("|")
		dict = {}
		while attributes:
			attribute = attributes.pop().strip()
			value = values.pop().strip()
			if attribute!="":
				dict[attribute] = value
		return dict[key]

	@staticmethod
	def read_line_from_map(out,key):
		strs = out.split("\n")
		print (strs)
		for item in strs:
			if item.find(key)!=-1: 
				LOG.debug("strs[i]: %s" %(item));
				attributes = item.split("|")
				#LOG.debug("attributes0: %s" %(attributes[0]));
				#LOG.debug("attributes1: %s" %(attributes[1]));
				if(attributes[1].lstrip().find(key)==0):
					return attributes[2].strip()
		return "not found"
