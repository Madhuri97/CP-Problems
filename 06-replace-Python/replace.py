# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().
# helloworld123 hello 345
# helloworld123 123   345
# helloworld123 world 345

def fun_replace(s1, s2, s3):
	idx = s1.count(s2)
	if(idx == 0):
		return s1

	elif idx == 1:
		s = ""
		before = s1.find(s2)
		after = before + len(s2)
		s = s1[0:before]+s3+s1[after:]
		return s

	else:
		s = s1
		for i in range(idx):
			before = s.find(s2)
			after = before + len(s2)
			s = s[0:before] + s3 + s[after:]
		return s
	
			# s1 = s1.replace(s2,s3)
	# return s1


