

import PIL
import subprocess
import threading

try:
	from Tkinter import *
except ImportError:
	from tkinter import * 

from touch import *
from mpc import *
from subprocess import *
from time import sleep

class gui():


	def __init__(self, master = None):

		self.maxWidth  	  = 320
		self.maxHeight 	  = 240
		self.current_song = ""
		self.songText     = ""
		self.root		  = master
		self.canvas       = None
		
		self.mpc 		  = mpc(10, self)
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



	def init(self, image):
		self.root.title("MediaPlayer")
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.geometry(str(self.maxWidth) + 'x' + str(self.maxHeight))
		self.root.protocol('WM_DELETE_WINDOW', self.exit)
		self.root.attributes('-alpha', 0.9)
		self.canvas = Canvas(self.root, bg="black", width=self.maxWidth, height=self.maxHeight)
		self.canvas.create_image(self.maxWidth/2, self.maxHeight/2, image=image)
		self.canvas.bind('<ButtonPress-1>', self.clickCallback )


	def clickCallback(self, event):
		t = touch(self.touch_config)
		t.onClick({'x' : event.x, 'y' : event.y})
		method = t.onClick({'x' : event.x, 'y' : event.y})
		
		if( method != None):
			methodToCall = getattr( self.mpc, str(method) )
			try:
				result = methodToCall()
			except AttributeError:
				globals()[method]()
			except TypeError:
				globals()[method]()


	def updateGUI(self):
	    t = threading.Thread(target=self.check_thread, args=() )
	    t.daemon = True
	    t.start()
	    #t.join()


	def check_thread(self):
		self.get_current_song()
		sleep(2.00)
		try:
			self.check_thread()
		except:
			print ("----> exception start new Thread")
			self.updateGUI()


	def get_current_song(self):
		songText = self.mpc.getSong()
		self.canvas.delete(self.current_song)
		self.queueText(songText)


	def queueText(self, displayText):
	
		#create a refernce to the song text
		newText = displayText;

		for x in range(0, len(displayText) ):
			#remove from the beginning
			newText = newText[1:]

			#trimmed new val max chars 40
			trimmedVal = newText[:40]

			#remove the current text and display new val
			self.canvas.delete(self.current_song)
			self.current_song = self.canvas.create_text(30, 20,  anchor="nw", fill="white", font="Purisa",text=trimmedVal)
			sleep(0.08)


	def exit(self):
		print ("----> exit")
		self.mpc.stop()
		self.root.destroy()


	def run(self):
		print ("----> run")
		self.canvas.pack()
		self.root.mainloop()

