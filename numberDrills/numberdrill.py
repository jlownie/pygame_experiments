import random, sys, tty, termios, pygame.mixer

class question:
	number = 0
	text = ""
	waveFile = ""

def prepareQuestions():
	counter = 0
	questionArray = []
	
	for numberText in ["maru", "ichi", "ni", "san", "shi", "go", "roku", "shichi", "hachi", "kyuu"]:
		newQuestion = question()
		newQuestion.number = counter
		newQuestion.text = numberText
		questionArray.append(newQuestion)
		counter = counter + 1
	
	print "Number of questions is " + str(len(questionArray))
	return questionArray

def getQuestion():
	questionChoice = random.randint(0, len(japaneseNumbers) - 1)
	thisQuestion = japaneseNumbers[questionChoice]
	return thisQuestion

def getKeyPress():
	# Get input from the user
	try:
		tty.setraw(sys.stdin.fileno())
		answer = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return answer

# Code execution starts here

# Initialise terminal so we can catch characters from input
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

random.seed()
pygame.mixer.init()

japaneseNumbers = prepareQuestions()

# Ask questions until the user chooses to exit
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

