from math import log2
import sys

"""Utilizando o algoritimo de brute force do Mocelin e plotando e imprimindo os dados no console
é possível observar que ao embaralhar as cartas elas retornam a condição ordenada
seguindo uma lógica sugestiva:

Vejamos primeiro para n = 8. Realizando o embaralhamento temos:

[5, 1, 6, 2, 7, 3, 8, 4]
[7, 5, 3, 1, 8, 6, 4, 2]
[8, 7, 6, 5, 4, 3, 2, 1]
[4, 8, 3, 7, 2, 6, 1, 5]
[2, 4, 6, 8, 1, 3, 5, 7] (último passe antes de retornar a condição original)

Para n = 14 temos:

[8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7]
[4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11]
[2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13] (último passe antes de retornar a cond. orig)

Interessante... Para n=14 o array foi reordenado mais rápido.

Fazendo mais alguns testes com dimensões variadas foi possível observar o seguinte padrão:

Considere x o maior número no array para o qual log2 retorna um inteiro. Usando os exemplo acima, vemos
que nos dois casos este número é o 8. A partir do exato momento em que este número passa a ocupar
a posição 0, a cartas são ordenadas em mais log2(8) passes. Se já tivermos aplicado 3 ordenações,
teríamos então um total de 3 + 3 ordenações.  Por outro lado, quando este número x passa
a ocupar a posição -1 (último elemento do array), as cartas são ordenadas em 2* (y + log2x). Por exemplo,
se tivermos aplicado 2 ordenações até o 8 chegar na posição -1, precisaremos de um total de 2 * (2 + 3) = 10
ordenações. Faça os testes com diversos arrays utilizando o brute force e confirme...

Com isso em mente adotou-se a seguinte estratégia:

1) dado um array cujo último elemento é n, obtém-se o maior inteiro x que está contido no array e para o qual
log2(x) retorna um inteiro. Por exemplo, se n=100, o maior numero inteiro no array seria 64.

2) Este número x ocupa uma dada posição no array e queremos ter o controle de que posição o mesmo vai passar a
ocupar ao longo dos embaralhamentos. 

3) Em cada embaralhamento, representado pela função passe, o número x muda de posição. A função passe retorna
exatamente esta posição.

4) Checa-se se x está na posição 0 ou na posição -1 e caso não esteja, incrementa o contador.

Realizando alguns testes no terminal obteve-se para um array cujo n=50.000:

A abordagem de BF precisa fazer slice duas vezes na lista (time complexity O(n/2) * 2)
para cada chamada da função. Em cada chamada é criada uma lista nova que é preenchida
item a item (complexidade O(n) para preencher). Além disso, dentro do laço while
o interpretador precisa comparar duas listas,  que é feito elemento por elemento e deve
ter complexidade de pelo menos O(n)) 

(a)Brute Force:

time python3 Mocelin\ 2.py 50000
Embaralhamento do Crupier: 1428

real    0m10.254s
user    0m9.778s
sys     0m0.461s

A abordagem #2 elimina o manuseio das listas (economiza memória) e o time complexity
em percorrê-la. É possível comprovar ainda (fica a cargo do nobre leitor) que o número máximo
de comparações será o maior entre os dois números: n - log2(n) ou (n/2) - log2(n)


(b) Abordagem de dimensionalidade reduzida
time python3 Mocelin.py 50000
Embaralhamentos do Crupier: 1428

real    0m0.048s
user    0m0.031s
sys     0m0.013s

Realizando uns testes para n=1000

time python3 Mocelin.py 1000
Embaralhamentos do Crupier: 60

real    0m0.044s
user    0m0.027s
sys     0m0.013s

Ou seja, para n da ordem de 1 - 10E6 a duração parece ser constante.  """


def passe(pos_ini, dim_array):

    # Função que retorna a posição de um determinado elemento do array
    # após ser sido embaralhado.

    if pos_ini >= (dim_array // 2):
        new_pos = 2 * pos_ini - dim_array
    else:
        new_pos = 2 * pos_ini + 1

    return new_pos


# Maior número que irá compor o array
j = int(sys.argv[1])

baralho_inicial = [i for i in range(1, j + 1)]

max_number = int(log2(baralho_inicial[-1]))
x = pow(2, max_number)
index_of_n = x - baralho_inicial[0]
dimensao_array = len(baralho_inicial)

# stopping_condition = max(1 + max_number, baralho_inicial[-1] / 2 - max_number)

counter = 0
while counter <= (dimensao_array - 1):
    index_of_n = passe(index_of_n, dimensao_array)
    counter += 1

    if index_of_n == 0:
        total = counter + max_number
        break
    elif index_of_n == (dimensao_array - 1):
        total = (counter + max_number) * 2
        break


try:
    print(f"Embaralhamentos do Crupier: {total}")
except Exception:
    print(f"Embaralhamentos do Crupier: {counter}")
