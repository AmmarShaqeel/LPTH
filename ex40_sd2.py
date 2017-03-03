class DictValue(object):
	
	def __init__(self, value):
		self.value = value
		
	def print_value(self):
		 print self.value
			

people = { 'hat':'person'}
			
test = DictValue(people['hat'])

test.print_value()