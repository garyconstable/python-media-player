

'''
touch class - map click on screen to method call
'''

class touch():

	def __init__(self, config = None):
		self.config = config

	'''
	test if point is between 2 other points
	'''
	def between(self, p, p1, p2):
		if p >= p1 and p <= p2:
			return True
		return False

	'''
	click handler, transform click to array
	'''
	def click(self, event = None):
		self.onClick({'x' : event.x, 'y' : event.y})


	'''
   	test click against config and return matching method call
   	'''
	def onClick(self, event={'x':0,'y':0} ):
		for k, v in self.config.items():
			callback = k
			if self.between(event['x'], v['x_min'] , v['x_max']) and self.between(event['y'], v['y_min'], v['y_max']):
				return callback
		