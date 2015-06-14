
import subprocess
from subprocess import *

'''
mpc class - wrapper to control mpc
'''

class mpc():

	def __init__(self, volume=50, GUI=None):
		self.volume = volume
		self.volume_mute = self.volume
		self.setVolume(volume)
		self.gui = GUI

		self.playing = False

	def clearConsole(self):
		subprocess.check_output("clear", shell=True)

	def play(self):
		print ("----> play")
		subprocess.check_output("mpc play", shell=True)
		self.playing = True


	def stop(self):
		print ("----> stop")
		subprocess.check_output("mpc stop", shell=True)
		self.playing = False


	def pause(self):
		print ("----> pause")
		subprocess.check_output("mpc pause", shell=True)
		self.playing = False


	def mute(self):
		print ("----> mute")
		if self.volume == 0:
			subprocess.check_output("mpc volume " + str(self.volume_mute), shell=True)
		else:
			self.volume_mute = self.volume
			self.volume = 0
			subprocess.check_output("mpc volume " + str(self.volume), shell=True)


	def volume_up(self):
		print ("----> volume up")
		if self.volume != 100:
			self.volume += 10
			subprocess.check_output("mpc volume " + str(self.volume), shell=True)


	def volume_down(self):
		print ("----> volume down")
		if self.volume != 0:
			self.volume -= 10
			subprocess.check_output("mpc volume " + str(self.volume), shell=True)


	def prev(self):
		print ("----> prev")
		subprocess.check_output("mpc prev", shell=True)


	def next(self):
		print ("----> next")
		subprocess.check_output("mpc next", shell=True)


	def setVolume(self, volume=0):
		try:
			print ("----> Set volume: " + str(volume))
			subprocess.check_output("mpc volume " + str(volume), shell=True)
		except (RuntimeError, TypeError, NameError):
			pass

	def getSong(self):
		return subprocess.check_output("mpc current", shell=True)


	def exit(self):
		print ("----> exit")
		self.stop()
		self.gui.root.destroy()


