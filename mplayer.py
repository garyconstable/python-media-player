



from touch import *
from mpc import *

try:
	# for Python2
	from Tkinter import *
except ImportError:
	# for Python3
	from tkinter import * 


import PIL
from PIL import Image
from PIL import ImageTk

import subprocess
from subprocess import *
import threading
from time import sleep



media_player_control = mpc(volume=50)



touch_config = { 
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





# ---> vars
maxWidth  	 = "320"
maxHeight 	 = "240"
imgFile   	 = "images/skin.gif"

root		 = 0
songText     = "Most relationships seem so transitory"
canvas       = ''
current_song = ''







# ---> functions
'''
def play():
	print ("----> play")
	subprocess.check_output("mpc play", shell=True)

def pause():
	print ("----> pause")
	subprocess.check_output("mpc pause", shell=True)

def mute():
	print ("----> mute")
	global volume
	global volume_mute
	if volume == 0:
		subprocess.check_output("mpc volume " + str(volume_mute), shell=True)
	else:
		volume_mute = volume
		volume = 0
		subprocess.check_output("mpc volume " + str(volume), shell=True)

def volume_up():
	print ("----> volume up")
	global volume
	if volume != 100:
		volume += 10
		subprocess.check_output("mpc volume " + str(volume), shell=True)

def volume_down():
	print ("----> volume down")
	global volume
	if volume != 0:
		volume -= 10
		subprocess.check_output("mpc volume " + str(volume), shell=True)
'''

def queueText(displayText):
	global current_song
	
	#create a refernce to the song text
	newText = displayText;

	for x in range(0, len(displayText) ):
		#remove from the beginning
		newText = newText[1:]

		#trimmed new val max chars 40
		trimmedVal = newText[:40]

		#remove the current text and display new val
		canvas.delete(current_song)
		current_song = canvas.create_text(30, 20,  anchor="nw", fill="white", font="Purisa",text=trimmedVal)
		sleep(0.08)

def get_current_song():
	global songText
	global canvas
	global current_song
	songText = subprocess.check_output("mpc current", shell=True)
	canvas.delete(current_song)
	queueText(songText);	

'''
def prev():
	print ("----> prev")
	subprocess.check_output("mpc prev", shell=True)

def next():
	print ("----> next")
	subprocess.check_output("mpc next", shell=True)

def exit():
	closeApp()

'''











def closeApp():
	print ("----> exit")
	global root
	subprocess.check_output("mpc stop", shell=True)
	root.destroy()

def check_thread():
	get_current_song()
	sleep(2.00)
	try:
		check_thread()
	except:
		print ("----> exception start new Thread")
		updateGUI()

def updateGUI():
    t = threading.Thread(target=check_thread, args=() )
    t.daemon = True
    t.start()
    #t.join()


def clickCallback(event):    
	
	#get the click event button
	t = touch(touch_config)
	t.onClick({'x' : event.x, 'y' : event.y})

	#get the method to call
	method = t.onClick({'x' : event.x, 'y' : event.y})
 	
 	#call the method
 	methodToCall = getattr( media_player_control, str(method) )

 	#try and call the method using global or class call
	try:
		result = methodToCall()
	except AttributeError:
		globals()[method]()
	except TypeError:
		globals()[method]()



	


def main():


	global root
	global songText
	global canvas
	global current_song



	try:
		subprocess.check_output("mpc volume " + str(volume), shell=True)
	except (RuntimeError, TypeError, NameError):
		pass

	try:
		subprocess.check_output("mpc stop", shell=True)
	except (RuntimeError, TypeError, NameError):
		pass


	'''
	root / main window 
	'''
	root = Tk()
	root.title("MediaPlayer")
	root.resizable(width=FALSE, height=FALSE)
	root.geometry(maxWidth+'x'+maxHeight)
	root.protocol('WM_DELETE_WINDOW', closeApp)
	root.attributes('-alpha', 0.9)


	'''
	add the image / draw to canvas
	''' 
	image  = ImageTk.PhotoImage(PIL.Image.open(imgFile))
	canvas = Canvas(root, bg="black", width=maxWidth, height=maxHeight)
	canvas.create_image(int(maxWidth)/2, int(maxHeight)/2, image=image)


	'''
	bind click to canvas
	'''
	canvas.bind('<ButtonPress-1>', clickCallback )



	'''
	main loop
	'''
	updateGUI()
	canvas.pack()
	root.mainloop()

	
if __name__ == '__main__':
	main()
