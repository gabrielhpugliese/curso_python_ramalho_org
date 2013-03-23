def dobro(x):
  ''' devolve x*2 '''
  return x*2
import dis
dis.dis(dobro.__code__.co_code)


l = range(10)
def soma(x, y):
  return x + y
print reduce(soma, l)


def fabrica_inc(incremento):
  def novo_inc(x):
    return x+incremento
  return novo_inc
inc7 = fabrica_inc(7)
print inc7(10)


from functools import partial
base2 = partial(int, base=2)
print base2('1010')

