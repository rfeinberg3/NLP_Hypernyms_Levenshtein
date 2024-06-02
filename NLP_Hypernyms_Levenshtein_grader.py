import random
import traceback
import time


studentName = "TestStudent"
inputFileName = 'NLP_Hypernyms_Levenshtein.py'

#there will likely be 5-10 problems

#For problem1()
problems1 = [
	(['dogs', 'cats', 'mammals', 'living things'], """All mammals, such as dogs and cats, eat to survive. Mammals are living things, aren't they?"""),
	(['animals', 'dogs', 'cats'], "Some animals, including cats, are considered. But it is NOT true that dogs are animals; I refuse to accept it."),
	(['hemingway', 'bibliophile', 'author', 'william faulkner', 'mark twain'], "Hemingway was an author of many classics. But also, Hemingway was a bibliophile, having read the works of every other famous American author, such as William Faulkner and Mark Twain.")
	] 
answers1 = [
	{('mammals', 'dogs'), ('mammals', 'cats',), ('living things', 'mammals')},
	{('animals', 'cats'), ('animals', 'dogs')},
	{('author', 'hemingway'), ('bibliophile', 'hemingway'), ('author', 'william faulkner'), ('author', 'mark twain')}
	]


#For problem2()
problems2 = [
	("abc", "abbc"),
	("rjkl;34lkj 34 .!@#\n", "xjkl;34lK j 34 .!@#\n\t"),
	("""Don't let your dreams be dreams\nYesterday you said tomorrow\nSo just do it\nMake your dreams come true\nJust do it""",
		"""Some people dream of success\nWhile you're gonna wake up and work hard at it\nNothing is impossible""")
	] 
answers2 = [
	1,
	6,
	126
	]

	
maxProblemTimeout = 30


outFile = open("grade_"+studentName+".txt", 'w')

def prnt(S):
	global outFile
	outFile.write(str(S) + "\n")
	print(S)

try:
	F = open(inputFileName, 'r', encoding="utf-8")
	exec("".join(F.readlines()))
except Exception as e:
	prnt("Couldn't open or execute '" + inputFileName + "': " + str(traceback.format_exc()))
	prnt("FINAL SCORE: 0")
	exit()


currentScore = 100

#PROBLEM 1
for i in range(len(problems1)):
	P = problems1[i]
	A = answers1[i]
	
	prnt('='*30)
	prnt("TESTING ON INPUT PROBLEM:")
	prnt(P)
	prnt("CORRECT OUTPUT:")
	prnt(str(A))
	prnt("YOUR OUTPUT:")
	try:
		startTime = time.time()
		result = problem1(P[0], P[1])
		prnt(result)
		endTime = time.time()		
		if endTime-startTime > maxProblemTimeout:
			prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (-10 points)")
		elif result==A:
			prnt("Correct!")
		else:
			prnt("Incorrect (-10 points)")
			currentScore -= 10

	except Exception as e:
		prnt("Error while executing this problem: " + str(traceback.format_exc()))
		currentScore -= 10

#PROBLEM 2
for i in range(len(problems2)):
	P = problems2[i]
	A = answers2[i]
	
	prnt('='*30)
	prnt("TESTING ON INPUT PROBLEM:")
	prnt(P)
	prnt("CORRECT OUTPUT:")
	prnt(str(A))
	prnt("YOUR OUTPUT:")
	try:
		startTime = time.time()
		result = problem2(P[0], P[1])
		prnt(result)
		endTime = time.time()		
		if endTime-startTime > maxProblemTimeout:
			prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (-10 points)")
		elif result==A:
			prnt("Correct!")
		else:
			prnt("Incorrect (-10 points)")
			currentScore -= 10

	except Exception as e:
		prnt("Error while executing this problem: " + str(traceback.format_exc()))
		currentScore -= 10

prnt('='*30)
prnt('='*30)
prnt('='*30)
prnt("FINAL SCORE:" + str(currentScore))