// # Write the function eggCartons(eggs) that takes 
// # a non-negative integer number of eggs, and returns 
// # the smallest integer number of cartons required to hold 
// # that many eggs, where a carton may hold up to 12 eggs

class eggcartons {
	public int fun_eggcartons(int eggs){
		final int i = 12;
		if(eggs == 0){
			return 0;
		} else if(eggs%i == 0) {
			return eggs/i;
		} else if(eggs%i == 1) {
			return eggs/i + 1;
		} else {
			return 1;
		}		
	}
	public static void main(String[] args) {
		
	}
}