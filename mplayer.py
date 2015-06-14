

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

	media_player_gui = gui(root)
	media_player_gui.init(image)
	media_player_gui.updateGUI()
	media_player_gui.run()

if __name__ == '__main__':
	main()
