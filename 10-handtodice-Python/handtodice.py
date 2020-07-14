# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	
	temp1 = hand%10
	hand = hand//10
	temp2 = hand%10
	hand = hand//10
	temp3 = hand%10
	return temp3,temp2,temp1

	# your code goes here
	
