
import pygame
from gui import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((320, 240))
	done = False
	myimage = pygame.image.load("images/skin.png")
	imagerect = myimage.get_rect()
	player = gui(screen)
	mp = mpc(0)

	while not done:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
		elif event.type == pygame.MOUSEBUTTONUP:
			Mouse_x, Mouse_y = pygame.mouse.get_pos()
			print [Mouse_x, Mouse_y]
			player.clickCallback(Mouse_x, Mouse_y)

		screen.fill((0,0,0))
		screen.blit(myimage, imagerect)
		pygame.display.flip()

	mp.exit()

if __name__ == '__main__':
	main()
