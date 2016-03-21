#Nancy McNamara, Brian Mann
#CP2, phonetic word generator

import random

random.seed()

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "X", "Y", "Z"] #pretty obvious, currently a list of all consonants except Q

consonant_blends_anywhere = ["CH", "TH", "SH", "GH", "PH", "SC", "SK", "SM", "SP", "ST"] #these are consonant blends that can be treated as one letter and can go anywhere a consonant would

#consonant_blends_end_syllable = ["BB", "FF", "DD", "GG", "MM", "LL", "NN", "PP", "RR", "MB"] #end of syllables, these made the words really messy


vowel_blends = ["OO", "OA", "EE", "AE", "EA", "AE", "AI", "AO", "AU", "EI", "EO", "EU", "IE", "IA", "IO", "IU", "OE", "OI", "OU", "UA", "UE", "UO", "UI"] #two vowels, some are more common than others, and these tend to make the words look/feel ugly

vowels = ["A", "E", "I", "O", "U"] #list of all vowels, not sure what to do about Y

consonant_blends_start_syllable = ["SL", "SN", "WH"] #consonant blends that can be treated as one letter but can only start a syllable

hierarchy = [consonant_blends_anywhere+consonants+consonant_blends_start_syllable, vowels, consonants+consonant_blends_anywhere] #helps keep letter possibilities organized 


#function that returns a random element from a list, while avoiding the most recent element (if we decide to add that functionality)
def pick_one(group, last):
	index = random.randint(0, len(group)-1)
	#this part prevents a repeat
	while group[index] == last:
		index = random.randint(0, size-1)
	return group[index]

#have to initialize the string to += it
string=""


num = random.randint(1,5) #number of syllables, 1-5
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
	

print string

#S->S1S2S3 | S1S2 S | S2 S | S2S3 S | epsilon
#Sone->S1S2S3 S
#Stwo->S1S2 (Sone | Stwo | epsilon)
#Sthree->S2 (Sone | Stw
#Sfour->S2S3
#S2-> vowel | vowel_blend
#S1-> (consonant | consonant_blend_anywhere | consonant_blend_end_syllable)
#S3->(consonant | consonant_blend_anywhere | consonant_blend_end_syllable)



