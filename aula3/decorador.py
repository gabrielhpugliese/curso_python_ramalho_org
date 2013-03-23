def loga_args(f):
  def minha_f(*args, **kwargs):
    print (args, kwargs)
    return f(*args, **kwargs)
  return minha_f

@loga_args
def dobro(x):
  return x*2
print dobro(10)
