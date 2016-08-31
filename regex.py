import re

test = "-------ABC------------"
pattern = r"\w+"
pattern = re.compile(pattern)

match = pattern.match(test)
print (match)
#print (match.group())

match = pattern.search(test)
print (match.group())


# split String on ;
pattern = re.compile(r"\s*;\s*")
text = "aaa  ; bbb ;ccc     ;        ddd ;  eee"
list = pattern.split(text)
print (list)

# Text substitution
pattern = re.compile(r"\s*;\s*")
text = "aaa  ; bbb ;ccc     ;        ddd ;  eee"
newText = pattern.sub("---", text)
print (newText)

string = "AAAA1111BBBB2222CCCC3333DDDD";
pattern = r"""         
	^	# start of line
	(.*?)	# 0 or more characters
		# non greedy
	(\d+)	# 1 or more digits
	(.*)	# 0 or more characters
	$	# end of line
           """
           
compiledPattern = re.compile(pattern, re.VERBOSE)
result = compiledPattern.search(string)
print (result.group())

text = "---111122223333333333334444555566667777---"
pattern = "2+(3+)4+(5+)6+"

# search for pattern
pattern = re.compile(pattern)
result = pattern.search(text)

# print results
print ("full match: ")
print(result.group(0))
print ("capture pattern 1: ")
print(result.group(1))
print ("capture pattern 2: ")
print(result.group(2))
print ("all captures: ")
print(result.groups())

text = "AB12CD34EF56GH"
pattern = r"(\d+)"

# find all occurrences of pattern
matcher = re.findall(pattern, text)
print (matcher)

# iterate through finding the pattern
print("\r\nPrinting repeating patterns:\r\n")
for matcher in re.finditer(pattern, text):
    print (matcher.groups(0))

# Greedy and Non Greedy Matches
text = "AAAA1111BBBB2222CCCC3333DDDD"
greedyPattern = r"^(.+)(\d+)(.+)$"
nonGreedyPattern = r"^(.+?)(\d+)(.+)$"
print ("Greedy")
print(re.findall(greedyPattern, text))
print ("None Greedy")
print(re.findall(nonGreedyPattern, text))









