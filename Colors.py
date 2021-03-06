# ======================================================================================================================
#                                        Colors conversion system
# ======================================================================================================================
#                                  Decimal to Zero-one and Hexadecimal
# ======================================================================================================================


def decimal(r=0, g=0, b=0, a=1, rhz=3):
	if rhz < 1 or rhz > 3:
		rhz = 3
	if a < 0 or a > 1:
		a = 1
	
	
	if r > 255:
		r = 255
	elif r < 0:
		r = 0
		
	if g > 255:
		g = 255
	elif g < 0:
		g = 0
		
	if b > 255:
		b = 255
	elif b < 0:
		b = 0
# ======================================================================================================================
#                                                 0 - 1
# ======================================================================================================================
	red = r
	green = g
	blue = b
	
	red = r / 256
	green = g / 256
	blue = b / 256
		
	zero_one = (red, green, blue, a)
	if rhz == 1:
		return zero_one
# ======================================================================================================================
#                                              Hexadecimal
# ======================================================================================================================
	rgb = (r, g, b)
	n = 1
	for color in rgb:
		first = int(color // 16)
		second = int(color % 16)
			
		if first == 10:
			first = 'A'
		elif first == 11:
			first = 'B'
		elif first == 12:
			first = 'C'
		elif first == 13:
			first = 'D'
		elif first == 14:
			first = 'E'
		elif first == 15:
			first = 'F'
		
		if second == 10:
			second = 'A'
		elif second == 11:
			second = 'B'
		elif second == 12:
			second = 'C'
		elif second == 13:
			second = 'D'
		elif second == 14:
			second = 'E'
		elif second == 15:
			second = 'F'
		
		if n == 1:		
			red = str(first) + str(second)
		if n == 2:
			green = str(first) + str(second)
		if n == 3:
			blue = str(first) + str(second)
		
		n += 1
	
	hexadecimal = '#' + red + green + blue
	if rhz == 2:
		return hexadecimal
		
	if rhz == 3:
		print(hexadecimal)
		print(zero_one)


# ======================================================================================================================
#                                Hexadecimal to Decimal and Zero-one
# ======================================================================================================================


def hexadecimal(h='#000000', a=1, rhz=3):
	if rhz < 1 or rhz > 3:
		rhz = 3
	if a < 0 or a > 1:
		a = 1
		
	h = h.upper()
	
	for i in h[:]:
		if i not in '#0123456789ABCDEF':
			i = 'F'
# ======================================================================================================================
#                                                   Decimal
# ======================================================================================================================
	if len(h) == 7 and h[0] == '#' and h.count('#') == 1:
		r = h[1:3]
		g = h[3:5]
		b = h[5:]
		
		def inth(n):
			try:
				n = int(n)
				
			except:
				if n == 'A':
					n = 10
				elif n == 'B':
					n = 11
				elif n == 'C':
					n = 12
				elif n == 'D':
					n = 13
				elif n == 'E':
					n = 14
				elif n == 'F':
					n = 15
				else:
					n = 15
			finally:
				return n
		
		
		
		red = ((16 ** 0) * inth(r[1])) + ((16 ** 1) * inth(r[0]))
		green = ((16 ** 0) * inth(g[1])) + ((16 ** 1) * inth(g[0]))
		blue = ((16 ** 0) * inth(b[1])) + ((16 ** 1) * inth(b[0]))
		decimal = (red, green, blue, a)
	
	if rhz == 1:
		return decimal
# ======================================================================================================================
#                                                  0 - 1
# ======================================================================================================================
	rzo = red / 255
	gzo = green / 255
	bzo = blue / 255
	
	zero_one = (rzo, gzo, bzo, a)
	
	if rhz == 2:
		return zero_one
	if rhz == 3:
		print(decimal)
		print(zero_one)


# ======================================================================================================================
#                                   Zero-one to Hexadecimal and Decimal
# ======================================================================================================================


def zero_one(r=0, g=0, b=0, a=1, rhz=3):
	if rhz < 0 or rhz > 3:
		rhz = 3
	if a < 0 or a > 1:
		a = 1
		
	if r < 0:
		r = 0
	elif r > 1:
		r = 1
		
	if g < 0:
		g = 0
	elif g > 1:
		g = 1
		
	if b < 0:
		b = 0
	elif b > 1:
		b = 1
# ======================================================================================================================
#                                               Decimal
# ======================================================================================================================
	red = int(r * 255)
	green = int(g * 255)
	blue = int(b * 255)
	
	decimal = (red, green, blue, a)
	
	if rhz == 1:
		return decimal	
# ======================================================================================================================
#                                              Hexadecimal
# ======================================================================================================================
	rgb = (red, green, blue)
	
	n = 1
	for color in rgb:
		first = int(color // 16)
		second = int(color % 16)
			
		if first == 10:
			first = 'A'
		elif first == 11:
			first = 'B'
		elif first == 12:
			first = 'C'
		elif first == 13:
			first = 'D'
		elif first == 14:
			first = 'E'
		elif first == 15:
			first = 'F'
		
		if second == 10:
			second = 'A'
		elif second == 11:
			second = 'B'
		elif second == 12:
			second = 'C'
		elif second == 13:
			second = 'D'
		elif second == 14:
			second = 'E'
		elif second == 15:
			second = 'F'
		
		if n == 1:		
			red = str(first) + str(second)
		if n == 2:
			green = str(first) + str(second)
		if n == 3:
			blue = str(first) + str(second)
		
		n += 1
	
	hexadecimal = '#' + red + green + blue
	if rhz == 2:
		return hexadecimal
		
	if rhz == 3:
		print(decimal)
		print(hexadecimal)
