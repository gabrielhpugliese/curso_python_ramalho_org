''' http://turing.com.br/material/ppqsp/lista_ex_1.html 
    Exercicio 2'''

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

homens_ate_quatro = [homem for homem in homens if len(homem) <= 4]
print '2.1:'
print homens_ate_quatro

tuplas_de_homens = [(homem[0], homem) for homem in homens]
print '2.2:'
print tuplas_de_homens

dict_de_homens = {tupla[0]: tupla[1] for tupla in tuplas_de_homens}
print '2.3:'
print dict_de_homens

zip_pessoas = zip(mulheres, homens)
print '2.4:'
print dict(zip_pessoas)

import itertools
todos = mulheres + homens
comb = list(itertools.combinations(todos, 2))
danca = [dupla for dupla in comb if dupla[0] in mulheres and dupla[1] in homens]
print '2.5:'
print danca

danca_alt = [(m, h) for m in mulheres for h in homens]
print '2.5 alternativo:'
print danca_alt

danca_menor_que_quatro = [dupla for dupla in comb if dupla[0] in mulheres 
                                                 and dupla[1] in homens
                                                 and len(dupla[0]) <= 4
                                                 and len(dupla[1]) <= 4]
print '2.6:'
print danca_menor_que_quatro
