import sys, pygame, time, random, math, logging
from random import randint
from pygame.locals import *

logging.basicConfig(level=logging.DEBUG)

# Global constants
mapSize = 1000 # in metres
screenSize = 800 # in pixels
viewDistance = 50 # in metres
maxSpriteSize = 5 # in metres
scaleToScreen = screenSize / viewDistance

frameRate = 100 # frames per second
frameInterval = 1000/frameRate # milliseconds between frames
moveRate = 10 # m/sec
moveIncrement = float(moveRate) / frameRate

# Colours
black = 0, 0, 0

# Sprites
playerSprite = pygame.image.load("player.png")
redCircle = pygame.image.load("redcircle.png")
blueCircle = pygame.image.load("bluecircle.png")
gridMarkerSprite = pygame.image.load("gridmarker.png")

# Classes
class WorldObject:
	def __init__(self):
		self.x=""
		self.y=""
		self.drawMe=False
		self.objType=""
		self.sprite=""

class Player(WorldObject):
	def __init__(self):
		self.sprite=playerSprite

class GridMarker(WorldObject):
	def __init__(self):
		self.sprite=gridMarkerSprite

class GoodThing(WorldObject):
	def __init__(self):
		self.sprite=blueCircle

class BadThing(WorldObject):
	def __init__(self):
		self.sprite=redCircle

# Functions
def initMap(worldObjs):
	random.seed()
	
	# grid
	gridSpace = mapSize/100
	gridMarkerX = gridSpace
	gridMarkerY = gridSpace
	while gridMarkerY < mapSize:
		while gridMarkerX < mapSize:
			newObj = GridMarker()
			newObj.x = gridMarkerX
			newObj.y = gridMarkerY
			worldObjs.append(newObj)
			gridMarkerX += gridSpace
		gridMarkerX = gridSpace
		gridMarkerY += gridSpace
			
	# bad things
	for i in range(1, 4):
		newObj = BadThing()
		newObj.x = randint(1, mapSize)
		newObj.y = randint(1, mapSize)
		worldObjs.append(newObj)

	# good things
	for i in range(1, 4):
		newObj = GoodThing()
		newObj.x = randint(1, mapSize)
		newObj.y = randint(1, mapSize)
		worldObjs.append(newObj)

	# player
	player = Player()
	player.x = randint(1, mapSize)
	player.y = randint(1, mapSize)
	worldObjs.append(player)
	return player

def getDist(worldObjA, worldObjB):
	xDist = worldObjA.x - worldObjB.x
	if xDist < 0 :
		xDist = xDist * -1
	yDist = worldObjA.y - worldObjB.y
	if yDist < 0 :
		yDist = yDist * -1
	return math.sqrt( xDist**2 + yDist**2 )

def drawSprite( canvas, sprite, objX, objY, playerX, playerY ):
	# Work out the screen position relative to the player
	screenX = (float(playerX) - objX) * scaleToScreen + screenSize/2
	screenY = (float(playerY) - objY) * scaleToScreen + screenSize/2
	
	# Now draw it
	spriteRect = sprite.get_rect()
	spriteRect.centerx = screenX
	spriteRect.centery = screenY
	canvas.blit(sprite, spriteRect)

def handleCommand(player):
	event=pygame.event.poll()
	pygame.event.clear() # Just take the first event, ignore held down keys
	if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q) or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_F4 and bool(event.mod & KMOD_ALT)):
		return True
	elif event.type == KEYDOWN and event.key == K_KP1:
		# Down and left
		player.x += float(moveIncrement)
		player.y -= float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP2:
		# Down
		player.y -= float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP3:
		# Down and right
		player.x -= float(moveIncrement)
		player.y -= float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP4:
		# Left
		player.x += float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP6:
		# Right
		player.x -= float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP7:
		# Up and left
		player.x += float(moveIncrement)
		player.y += float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP8:
		# Up
		player.y += float(moveIncrement)
	elif event.type == KEYDOWN and event.key == K_KP9:
		# Up and right
		player.x -= float(moveIncrement)
		player.y += float(moveIncrement)

	return False

def mainLoop():
	# Init infrastructure
	canvas = pygame.display.set_mode([screenSize, screenSize], FULLSCREEN | DOUBLEBUF | HWSURFACE)
	clock = pygame.time.Clock()
	pygame.key.set_repeat(frameInterval, frameInterval)
	pygame.mouse.set_visible(False)
	
	# Initialise sprites
	playerSprite.convert
	redCircle.convert
	blueCircle.convert
	gridMarkerSprite.convert
	
	worldObjects=[]	
	player = initMap(worldObjects)
	
	while True:
		# Draw the screen
		canvas.fill(black)
		for thisObj in worldObjects:
			if isinstance(thisObj, Player):
				# The player is always centered on the screen
				drawSprite(canvas, thisObj.sprite, 0, 0, 0, 0)
			elif getDist(thisObj, player) <= viewDistance:
				drawSprite(canvas, thisObj.sprite, thisObj.x, thisObj.y, player.x, player.y)
		
		# Get and process player input
		quitNow = handleCommand(player)
		if quitNow:
			break
		pygame.display.flip()
		clock.tick(frameRate)

# Code execution starts here
if __name__ == "__main__":
	mainLoop()

