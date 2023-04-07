pos = 0
def foo(ls, n, p):
	s = 0
	i = n
	while i < n + 10:
		i += 1
		s += ls[i]
	print(f"n: {n} n \ts: {s}")
	if 100 - n == 10:
		p = n
		return s
	else:
		s1 = foo(ls, n + 1, p)
		if s <= s1:
			p = n
			return s
		else:
			return s1
import random
ls = [i for i in range(101)]
#random.shuffle(ls)
print(foo(ls, 0, pos))