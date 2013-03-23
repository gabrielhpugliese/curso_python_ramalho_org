def rotacionar(pessoas):
	pessoas = list(pessoas) # Funciona com iteraveis e iteradores
	while True:
		for pessoa in pessoas:
			yield pessoa

def rotacionar2(pessoas):
	pessoas = list(pessoas)
	proxima = 0
	while True:
		nome = yield pessoas[proxima]
		if nome is not None:
			pessoas.append(nome)
		proxima = (proxima + 1) % len(pessoas)
