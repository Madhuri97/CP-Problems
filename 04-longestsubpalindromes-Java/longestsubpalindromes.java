// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public boolean fun_isPalindromes(String s) {
		String st = "";
		for(int i = s.length()-1; i >= 0; i--) {
			st += s.charAt(i);
		}
		return st.equals(s);
	}
	public String fun_longestsubpalindromes(String s) {
		String subpalin = "";
		for(int i = 0; i < s.length(); i++) {
			String tmp = "";
			for(int j = i; j < s.length(); j++) {
				tmp += s.charAt(j);
				if(fun_isPalindromes(tmp)) {
					if(tmp.length() > subpalin.length() || (tmp.length() == subpalin.length() && tmp.compareTo(subpalin) > 0)) {
						subpalin = tmp;
					}
				}
			}
		}
		return subpalin;
	}
	public static void main(String[] args) {
		
	}
}
