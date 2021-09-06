# python3

import math

num = int(input())
for i in range(num):
	numlist = [int(x) for x in input().split()]
	dx = numlist[0] - numlist[3]
	dy = numlist[1] - numlist[4]
	dr1 = numlist[2] + numlist[5]
	dr2 = numlist[2] - numlist[5]
	da = math.sqrt(dx*dx+dy*dy)
	if dx == 0 and dy == 0:
		if dr2 == 0:
			print(-1)
		else:
			print(0)
	elif da > max([numlist[2],numlist[5]]):
		if da > dr1:
			print(0)
		elif da == dr1:
			print(1)
		elif da < dr1:
			print(2)
	elif da == max([numlist[2],numlist[5]]):
		print(2)
	else:
		if da == max([numlist[2],numlist[5]]) - min([numlist[2],numlist[5]]):
			print(1)
		elif da < max([numlist[2],numlist[5]]) - min([numlist[2],numlist[5]]):
			print(0)
		else:
			print(2)
