

try:
	from Tkinter import *
except ImportError:
	from tkinter import * 

from PIL import Image
from PIL import ImageTk
from gui import *


def main():

	root = Tk()
	image  = ImageTk.PhotoImage(PIL.Image.open("images/skin.gif"))
	
	#root = Tk()
	#png = PIL.Image.open('images/skin.gif').convert("RGBA")
	#png.load()
	
	#root = Tk()
	#tmp = PIL.Image.open('images/skin2.png').convert("RGB")
	#image  = ImageTk.PhotoImage(tmp)

	media_player_gui = gui(root)
	media_player_gui.init(image)
	media_player_gui.updateGUI()
	media_player_gui.run()

if __name__ == '__main__':
	main()
