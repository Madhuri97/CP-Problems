# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.
# 4,5,6,7 => True
# 1,1,3,2 => False
def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if(qR == oR):
		return True
	if qC == oC:
		return True
	d1 = abs(qR - oR)
	d2 = abs(qC - oC)
	if d1 == d2:
		return True
	return False