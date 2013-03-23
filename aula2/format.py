fmt = '{moeda_orig} 1.00 equivale a {moeda_conv} {valor_conv:.2f}'
vals = ('USD', 'BRL', 1.8099)
dvals = dict(zip(('moeda_orig', 'moeda_conv', 'valor_conv'), vals))
print fmt.format(**dvals)

class Coisa():
    def __init__(self):
        self.cor = 'azul'
        self.peso = 1000

c = Coisa()
print '{coisa.cor}, {coisa.peso}'.format(coisa=c)
