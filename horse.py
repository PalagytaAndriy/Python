def horse(x0, y0, done, size=5):
	# создаем шахматную доску в виде 2го списка
	h = [[0 for j in range(size)] for i in range(size)]
	# начальная координата(1го хода)
	h[x0][y0] = 1

	# Возможные ходы
	dx = [2, 1, -1, -2, -2, -1, 1, 2]
	dy = [1, 2, 2, 1, -1, -2, -2, -1]

	def check_done(u, v, i):
		h[u][v] = i
		done = move(u, v, i)
		if not done:
			h[u][v] = 0
		return done

	def move(x, y, i):

		# eos - показывает все ли варианты возможных 8ми ходов мы рассмотрели
		# done - показывает удачна ли данная ветка решения
		# k - порядковый номер рассмотренной попытки из 8 допустимых
		env = {'done': False, 'eos': False, 'u': x, 'v': y, 'k': -1}

		def next():
			x = env['u']
			y = env['v']
			while env['k'] < 8:
				env['k'] += 1
				if env['k'] < 8:
					env['u'] = x + dx[env['k']]
					env['v'] = y + dy[env['k']]
				if (0 <= env['u'] < size) and (0 <= env['v'] < size) and h[env['u']][
					env['v']] == 0:
					break
			env['eos'] = (env['k'] == 8)

		if i < size ** 2:  # если доска не заполнена
			next()
			while not env['eos'] and not check_done(env['u'], env['v'], i + 1):
				next()
			done = not env['eos']
		else:
			done = True
		return done

	move(x0, y0, 1)
	print(h)


horse(0, 0, True, 6)
