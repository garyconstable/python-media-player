

import PIL
import subprocess
import threading
import datetime

try:
	from Tkinter import *
except ImportError:
	from tkinter import * 

from touch import *
from mpc import *
from subprocess import *
from time import sleep



class gui():


	def __init__(self, master = None ):

		self.maxWidth  	  = 320
		self.maxHeight 	  = 240
		self.current_song = ""
		self.songText     = ""
		self.root		  = master
		self.canvas       = None

		self.dateTime 	  = None
		self.volumeTxt 	  = None
		
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
	    self.t = threading.Thread(target=self.check_thread, args=() )
	    self.t.daemon = True
	    self.t.start()

	    self.x = threading.Thread(target=self.check_thread_now, args=() )
	    self.x.daemon = True
	    self.x.start()
	    


	def check_thread(self):
		self.queueText()
		try:
			self.check_thread()
		except:
			print ("----> exception start new Thread")
			#self.t.join()
			self.updateGUI()


	def check_thread_now(self):
		self.writeItems()
		sleep(1)
		try:
			self.check_thread_now()
		except:
			print ("----> exception start new Thread now() ")
			#self.x.join()
			self.updateGUI()



	def queueText(self):
		
		if(self.mpc.playing == True):

			songText = self.mpc.getSong()
			self.canvas.delete(self.current_song)

			displayText = songText

			#create a refernce to the song text
			newText = displayText

			for x in range(0, len(displayText) ):
				#remove from the beginning
				newText = newText[1:]

				#trimmed new val max chars 40
				trimmedVal = newText[:38]

				#remove the current text and display new val
				self.canvas.delete(self.current_song)
				self.current_song = self.canvas.create_text(30, 40,  anchor="nw", fill="white", font="Purisa",text=trimmedVal)
				sleep(0.12)

			self.current_song = self.canvas.create_text(30, 40,  anchor="nw", fill="white", font="Purisa",text=displayText[:38])
			sleep(10)

		else:
			sleep(1)


	def writeItems(self):
		
		'''
		date time
		'''
		self.canvas.delete(self.dateTime)
		current_time = datetime.datetime.now().strftime('%H:%M  %d.%m.%Y')
		self.dateTime = self.canvas.create_text( 30, 20,  anchor="nw", fill="white", font="Purisa", text=current_time)

		'''
		volume
		'''
		self.canvas.delete(self.volumeTxt)
		volume = 'Volume: ' + str(self.mpc.volume) + '%'
		self.volumeTxt = self.canvas.create_text( 30, 63,  anchor="nw", fill="white", font="Purisa", text=volume)






	def exit(self):
		print ("----> exit")
		self.mpc.stop()
		self.root.destroy()


	def run(self):
		print ("----> run")
		self.canvas.pack()
		self.root.mainloop()

