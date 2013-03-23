'''
	>>> zape = Carta(4, 'paus')
	>>> zape
	Carta(4, 'paus')
	>>> b = BaralhoIter()
	>>> for carta in b: #doctest: +ELLIPSIS
	...   print carta
	Carta('A', 'paus')
	Carta('2', 'paus')
	...
	Carta('K', 'ouros')
'''

class Carta(object):
	def __init__(self, valor, naipe):
		self.valor = valor
		self.naipe = naipe

	def __repr__(self):
		return 'Carta(%r, %r)' % (self.valor, self.naipe)

class BaralhoIter:
	naipes = 'paus copas espadas ouros'.split()
	valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

	def __init__(self):
		self.cartas = [Carta(v, n) for n in self.naipes
					   for v in self.valores]
	
	def __iter__(self):
		return IteradorBaralho(self)

class IteradorBaralho:
	def __init__(self, baralho):
		self.baralho = baralho
		self.indice = 0
	
	def next(self):
		try:
			res = self.baralho.cartas[self.indice]
		except IndexError:
			raise StopIteration()
		self.indice += 1
		return res

	def __iter__(self):
		return self
