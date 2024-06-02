"""This is a sample file for hw1. 
It contains the function that should be submitted,
except all it does is output a random value out of the
possible values that are allowed.
- Dr. Licato"""

import random
import re

def problem1(NPs, s):
	hypernyms = set()
	string_split = s.split(".") #split string by '.' character to aid in parsing multiple parts of the text.

	for i in range(len(NPs)):
		for j in range(len(NPs)):
			type1_start = re.compile(r'(is|was|are) (a |an )?(type of |kind of )?') #type1 regex
			type2_start = re.compile(r', (including|such as) ((\w+,){2,})?(.+(and |or ))?') #type2 regex
			for string in string_split:
				mo1 = type1_start.search(string)
				mo2 = type2_start.search(string)

				# mo1 and mo2 come back as NoneType if the search doesn't find any matches
				if(mo1 != None):
					str_mo1 = mo1.group() #str_mo1 = captured string from regex parsing
					str1_start = NPs[i]+' '+str_mo1+NPs[j] #type 1 format containing nouns from NPs
					if((s.casefold()).find(str1_start) != -1):
						hypernyms.add( (NPs[j], NPs[i]) ) #if str1_start is in our string s, then we can surely add the tuple to our set

				if(mo2 != None):
					str_mo2 = mo2.group() #str_mo2 = captured string from regex parsing
					str2_start = NPs[i]+str_mo2+NPs[j] #type 2 format containing nouns from NPs
					if((s.casefold()).find(str2_start.casefold()) != -1):
						hypernyms.add((NPs[i], NPs[j]))  #if str1_start is in our string s, then we can surely add the hypernym to our set
						#since our parsing may also contain other nouns, we must scan through it as well.
						for k in range(len(NPs)):
							if((NPs[k] in str2_start.casefold()) and (NPs[k].casefold() != NPs[i].casefold())):
								hypernyms.add( (NPs[i], NPs[k]) ) #if noun(s) from NPs exist in st2_start, and they are not our hypernym, then we can surely add the tuple to our set
	return hypernyms


def problem2(s1, s2):
	rows = len(s1)+1
	columns = len(s2)+1

	#initialize empty MxN matrix
	matrix = [[0 for i in range(columns)] for j in range(rows)]

	#create first row
	for i in range(rows):
		matrix[i][0] = i
	#create first column
	for j in range(columns):
		matrix[0][j] = j

	#main recurrence
	for i in range(1, rows):
		for j in range(1, columns):
			if(s1[i-1] == s2[j-1]):
					matrix[i][j] = matrix[i-1][j-1] #if the character from each string is the same. i.e substitution with no cost
			else:
				matrix[i][j] = min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+2) #if the characters from each string are NOT the same choose the best option. (insertion, deletion, or substition w/cost)


	return matrix[rows-1][columns-1] #the edit distance