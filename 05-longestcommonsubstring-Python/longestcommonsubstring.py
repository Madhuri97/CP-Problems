# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    lngst = ""
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+1):
            subs = s1[i:j]
            if subs in s2:
                if len(subs) > len(lngst):
                    lngst = subs
                elif len(subs) == len(lngst):
                    if subs < lngst:
                        lngst = subs
    return lngst
