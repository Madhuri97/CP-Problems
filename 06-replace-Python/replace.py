# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().
# helloworld123 123 345

def fun_replace(s1, s2, s3):
	for i in range(len(s1)):
		while(i < len(s2)):
			if(s1[i] == s2[i]):
				s1[i] = s1 + s3[i]
			else: s1[i] = s1[i]+s2[i]
			i = i+1
	return s1

