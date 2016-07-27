#Nancy McNamara, Brian Mann
#CP2, phonetic word generator

import random

random.seed()

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "X", "Y", "Z"] #pretty obvious, currently a list of all consonants except Q

consonant_blends_anywhere = ["CH", "TH", "SH", "GH", "PH", "SC", "SK", "SM", "SP", "ST", "SQU"] #these are consonant blends that can be treated as one letter and can go anywhere a consonant would

consonant_blends_end_syllable = ["BB", "FF", "DD", "GG", "MM", "LL", "NN", "PP", "RR", "BS", "CS", "DS" ,"FS", "GS", "HS", "KS", "LS", "MS", "NS", "PS", "SS", "TS", "VS", "WS", "YS", "GHS", "PHS", "SCS", "SKS", "SPS", "STS", "LCH", "LTH", "LSH", "LGH", "LPH", "LST", "LSP"] #end of syllables, these made the words really messy

for con in consonants:
	if con != "R" and con != "L" and con != "H" and con != "W" and con != "J":
		consonant_blends_end_syllable.append("L"+con)
		consonant_blends_end_syllable.append("R"+con)

vowel_blends = ["OO", "OA", "EE", "EA", "AE", "AI", "AO", "AU", "EI", "EO", "EU", "IE", "IA", "IO", "IU", "OE", "OI", "OU", "UA", "UE", "UO", "UI"] #two vowels, some are more common than others, and these tend to make the words look/feel ugly

#vowels = ["A", "E", "I", "O", "U", 
vowels = ["Y"] #list of all vowels, not sure what to do about Y

consonant_blends_start_syllable = ["TR", "SN", "WH", "QU", "WR", "DR", "SL", "VR", "SW"] #consonant blends that can be treated as one letter but can only start a syllable

for con in consonants:
	if con != "D" and con != "R" and con != "T" and con != "L" and con != "H" and con !="W" and con != "J" and con != "M" and con != "N" and con != "S" and con !="V" and con != "Y" and con !="Z" and con !="X":
		consonant_blends_start_syllable.append(con+"L")
		consonant_blends_start_syllable.append(con+"R")

hierarchy = [consonant_blends_anywhere+consonants+consonant_blends_start_syllable, vowels+vowel_blends, consonants+consonant_blends_end_syllable+consonant_blends_anywhere] #helps keep letter possibilities organized 


#function that returns a random element from a list, while avoiding the most recent element 
def pick_one(group, last):
	index = random.randint(0, len(group)-1)
	#this part prevents a repeat
	while group[index] == last:
		index = random.randint(0, len(group)-1)
	return group[index]

#have to initialize the string to += it
string=""
guy=" "

minimum=1
maximum=4
num = random.randint(1,4) #number of syllables, 1-5
for count in range(0,num):
	pick = random.randint(minimum,maximum)
	if pick==1: 
		guy = pick_one(hierarchy[0], guy[-1]) + pick_one(hierarchy[1], guy[-1]) + pick_one(hierarchy[2], guy[-1])
		string+=guy
		minimum=1
		maximum=4
	elif pick==2:
		guy = pick_one(hierarchy[0], guy[-1]) + pick_one(hierarchy[1], guy[-1])
		string+=guy
		minimum=1
		maximum=2
	elif pick==3:
		guy = pick_one(hierarchy[1], guy[-1]) + pick_one(hierarchy[2], guy[-1])
		string+=guy
		minimum=1
		maximum=4
	elif pick==4:
		guy = pick_one(hierarchy[1], guy[-1])
		string+=guy
		minimum=1
		maximum=2
print string

#S->Sone | Stwo | Sthree | Sfour 
#Sone->S1S2S3S | S1S2S3    can be followed by anything
#Stwo->S1S2Sone | S1S2Stwo | S1S2     consonant vowel can be followed by anything but vowel consonant and vowel
#Sthree->S2Sone | S2Stwo       vowel can be followed by anything but vowel and vowel consonant
#Sfour->S2S3S | S2S3      can be followed by anything
#S2-> vowel | vowel_blend
#S1->consonant | consonant_blend_anywhere | consonant_blend_start_syllable
#S3->consonant | consonant_blend_anywhere | consonant_blend_end_syllable



