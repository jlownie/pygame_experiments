import random, sys, tty, termios

# Initialise terminal so we can catch characters from input
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

japaneseNumbers = ["maru", "ichi", "ni", "san", "shi", "go", "roku", "shichi", "hachi", "kyuu", "juu"]

random.seed()

class question:
	number = 0
	text = ""
	waveFile = ""

def getQuestion():
	newQuestion = question()
	newQuestion.number = random.randint(0,9)
	newQuestion.text = japaneseNumbers[newQuestion.number]
	return newQuestion

def getKeyPress():
	# Get input from the user
	try:
		tty.setraw(sys.stdin.fileno())
		answer = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

while True:
	thisQuestion = getQuestion()
	print thisQuestion.text
	
	answer = getKeyPress()

	try:
		answer = int(answer)
	except ValueError:
		quit()
		
	if thisQuestion.number == answer:
		print "Correct"
	else:
		print "The correct answer is " + str(thisQuestion.number)

