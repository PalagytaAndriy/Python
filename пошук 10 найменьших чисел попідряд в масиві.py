import random

pos = 0
def foo(ls, n, p):
	global j
	s = 0
	i = n
	while i < n + 5:
		i += 1
		s += ls[i]
	print(f"n: {n} n \ts: {s}")
	if 10 - n == 5:
		p = n
		return s
	else:
		s1 = foo(ls, n + 1, p)
		if s <= s1:
			j = n
			p = n
			return s
		else:
			return s1


ls = [random.randint(-10, 10) for i in range(0, 11)]
print(ls, '\n')
p = 0
j = 0

print(foo(ls, 0, pos))

i = 0
i = j

while i < j + 5:
	print(ls[i],end=' ')
	i += 1


