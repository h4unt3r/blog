class dictdot(dict):
	def __call__(self, *args, **kwargs):
		if self.has_key('$'): 
			if callable(self['$']):
				return self['$'](*args, **kwargs)
			else:
				return self['$']

	def __getattr__(self, attr):
		if self.has_key(attr):
			if type(self[attr]) == dict:
				return dictdot(self[attr])
			else:
				return self[attr]
		else:
			raise KeyError("Key '%s' not in dict! >:0" % attr)

	def __setattr__(self, attr, val):
		if self.has_key(attr):
			if type(val) == dict:
				self[attr] = dictdot(val)
			else:
				self[attr] = val
		else:
			raise KeyError("Key '%s' not in dict! >:0" % attr)
