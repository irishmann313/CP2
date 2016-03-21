#Nancy McNamara, Brian Mann
#CP2, phonetic word generator

import random

random.seed()

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "X", "Y", "Z"]

consonant_blends_anywhere = ["CH", "TH", "SH", "GH", "PH", "SC", "SK", "SM", "SP", "ST"]

#consonant_blends_end_syllable = ["BB", "FF", "DD", "GG", "MM", "LL", "NN", "PP", "RR", "MB"] #end of syllables

#consonant_blends_

vowel_blends = ["OO", "OA", "EE", "AE", "EA", "AE", "AI", "AO", "AU", "EI", "EO", "EU", "IE", "IA", "IO", "IU", "OE", "OI", "OU", "UA", "UE", "UO", "UI"]

vowels = ["A", "E", "I", "O", "U"]

consonant_blends_start_syllable = ["SL", "SN", "WH"] #start of syllables

hierarchy = [consonant_blends_anywhere+consonants+consonant_blends_start_syllable, vowels, consonants+consonant_blends_anywhere]


def pick_one(group, last):
	size = len(group)
	index = random.randint(0, size-1)
	while group[index] == last:
		index = random.randint(0, size-1)
	return group[index]

string=""

num = random.randint(1,5)
for count in range(1,num):
	pick = random.randint(1,3)

	if pick==1:
		print 'cons vowel cons'
		string += pick_one(hierarchy[0], "") + pick_one(hierarchy[1], "") + pick_one(hierarchy[2],"")
	elif pick==2:
		print 'cons vowel'
		string += pick_one(hierarchy[0], "") + pick_one(hierarchy[1], "")
	elif pick==3:
		print 'vowel cons'
		string += pick_one(hierarchy[1], "") + pick_one(hierarchy[2],"")

#else
#	print 'epsilon'
#	string+=""
	

print string

if random.randint(0,1):
	print 'yes'
else:
	print 'no'

#S->S1S2S3 | S1S2 S | S2 S | S2S3 S | epsilon
#S2-> vowel | vowel_blend
#S1-> (consonant | consonant_blend_anywhere | consonant_blend_end_syllable)
#S3->(consonant | consonant_blend_anywhere | consonant_blend_end_syllable)



random.randint(1, 10)
