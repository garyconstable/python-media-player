
from touch import *
from mpc import *

class gui():

	def __init__(self, master = None ):
		self.mpc 		  = mpc(0)
		self.touch_config = {
			'play' : {
				'x_min'	:  16,
				'x_max'	:  75,
				'y_min'	: 122,
				'y_max'	: 172
			},
			'pause' : {
				'x_min'	:  91,
				'x_max'	: 150,
				'y_min'	: 122,
				'y_max'	: 172
			},
			'volume_up' : {
				'x_min'	: 169,
				'x_max'	: 228,
				'y_min'	: 122,
				'y_max'	: 172
			},
			'mute' : {
				'x_min'	: 245,
				'x_max'	: 303,
				'y_min'	: 122,
				'y_max'	: 172
			},
			'prev' : {
				'x_min'	:  16,
				'x_max'	:  75,
				'y_min'	: 185,
				'y_max'	: 229
			},
			'next' : {
				'x_min'	:  91,
				'x_max'	: 150,
				'y_min'	: 185,
				'y_max'	: 229
			},
			'volume_down' : {
				'x_min'	: 169,
				'x_max'	: 228,
				'y_min'	: 185,
				'y_max'	: 229
			},

			'exit' : {
				'x_min'	: 245,
				'x_max'	: 303,
				'y_min'	: 185,
				'y_max'	: 229
			},
		}
		self.mpc.stop()
		self.mpc.clearConsole()

	def clickCallback(self, x, y):
		t = touch(self.touch_config)
		method = t.onClick({'x' : x, 'y' : y})

		if( method != None):
			methodToCall = getattr( self.mpc, str(method) )
			try:
				result = methodToCall()
			except AttributeError:
				globals()[method]()
			except TypeError:
				globals()[method]()
