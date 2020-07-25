// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
import java.util.*;

class nthtenlyprime {
	public boolean isPrime(int n) {
		int cnt = 0;
		for(int i = 1; i <= n; i++) {
			if(n%i == 0) {
				cnt++;
			}
		}
		return cnt == 2;
	}

	public boolean isTenly(int n) {
		int sm = 0;
		while(n!=0) {
			sm = sm + n % 10;
			n = n /10;
		}
		if(sm == 10) {
			return true;
		}
		else {
			return false;
		}
	}

	public int fun_nthtenlyprime(int n){
		List<Integer> li = new ArrayList<Integer>();
		int i = 0;
		while(i < 3000) {
			if(isPrime(i) && isTenly(i)) {
				li.add(i);
			}
			i += 1;
		}
		return li.get(n);
	}
	public static void main(String[] args) {
		
	}
}