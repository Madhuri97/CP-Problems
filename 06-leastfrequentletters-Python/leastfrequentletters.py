# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")
import string

def leastfrequentletters(s):
	# Your code goes here
	if len(s) == 0:
		return ""
	s = s.lower()
	st = string.ascii_lowercase
	i = 0
	micnt = 100
	strf = ''
	while i < 26:
		cnt = s.count(st[i])
		if micnt > cnt > 0:
			micnt = cnt
			strf = st[i]
		elif micnt == cnt:
			strf += st[i]
		i += 1
	if strf == '':
		return strf
	return strf
	
	# st = ""
	# strf = ""
	# cnt = 0
	# for i in range(len(s)):
	# 	if (s[i].isalpha()):
	# 		st += s[i]
	# 	for j in st:
	# 		if j not in strf:
	# 			strf += j
	# 		cnt += 1
	# 	if cnt < 1:
	# 		return strf
	# 	return ""
	# return ""
