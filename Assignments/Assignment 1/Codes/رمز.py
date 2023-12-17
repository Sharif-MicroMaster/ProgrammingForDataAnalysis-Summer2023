k = int(input())
code = input()

ans = 0
for i in code:
	dial = input()
	moves = dial.find(i)
	ans = ans + min(moves, 9 - moves)
	
print(ans)