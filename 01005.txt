import sys
from collections import deque
sys.setrecursionlimit(10**6)

def gettime(n):
	if buildtime[n] > -1:
		return buildtime[n]
	if dic.get(n):
		r = 0
		for i in dic.get(n):
			r = max(r, gettime(i)+d[i-1])
		buildtime[n] = r
	else:
		buildtime[n] = 0
	return buildtime[n]

case = int(sys.stdin.readline())
for i in range(case):
	n, k = [int(x) for x in sys.stdin.readline().split()]
	d = [int(x) for x in sys.stdin.readline().split()]
	dic = dict()
	for j in range(k):
		x, y = [int(x) for x in sys.stdin.readline().split()]
		if dic.get(y):
			dic.get(y).append(x)
		else:
			dic[y] = [x]
	w = int(sys.stdin.readline())
	buildtime = [-1]*(n+1)
	queue = deque()
	queue.append(w)
	result = gettime(w)
	print(result+d[w-1])