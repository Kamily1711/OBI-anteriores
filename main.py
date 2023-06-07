#1- Hotel-OBI:
d = int(input())
a = int(input())
n = int(input())
if n == 1:
    print(d*31)
elif n >= 16:
    print((d+(14*a))*(31-n+1))
else:
    print((d+(n-1)*a)*(31-n+1))


#2- Maior Valor - OBI:
n = int(input())
m = int(input())
s = int(input())
tem = 0
for i in range(m, n-1, -1):
    tam = str(i)
    num = []
    for j in tam:
        num.append(int(j))
    if sum(num) == s:
        print(i)
        tem = 1
        exit()
if tem == 0:
    print('-1')


#3-Quadrado mágico - OBI:
n = int(input())
tabela = []
numero = None
for i in range(n):
    linha = []
    new_linha = []
    linha = input().split()
    for elemento in linha:
        new_linha.append(int(elemento))
    tabela.append(new_linha)
linha = None
for i in range(n):
    if 0 not in tabela[i]:
        soma = sum(tabela[i])
    for j in range(n):
        if tabela[i][j] == 0:
            linha = i+1
            coluna = j+1
for i in range(n):
    if 0 in tabela[i]:
        numero = soma - sum(tabela[i])
print(numero)
print(linha)
print(coluna)


#4- Chuva - OBI:
n = int(input())
s = int(input())
vetor = [int(i) for i in input().split()]
prefix_sum = []
prefix_sum.append(vetor[0])
cont = 0
for x in range(1, len(vetor)):
    prefix_sum.append(prefix_sum[x-1]+vetor[x])
prefix_sum.sort(reverse=True)
for num1 in prefix_sum:
    if num1 == s:
        cont += 1
    for num2 in prefix_sum:
        if num1-num2 == s:
            cont += 1
print(cont)





































"""n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    palavra1 = []
    palavra2 = []
    for let in a:
        palavra1.append(let)
    for let in b:
        palavra2.append(let)
    tam = len(palavra1)-len(palavra2)
    encaixa = 0
    for i in range(len(palavra1)-1, tam-1, -1):
        for j in range(len(palavra2)):
            print(f'{palavra1[i]} {palavra2[j]}')
"""
"""n = int(input())
for _ in range(n):
    linha = input()
    new_linha = []
    for caractere in linha:
        if 90>=ord(caractere)>=65 or 122>=ord(caractere)>=97:
            new_linha.append(chr(ord(caractere)+3))
        else:
            new_linha.append(caractere)
    new_linha.reverse()
    qtd = len(new_linha)
    for i in range(qtd//2,qtd):
        new_linha[i] = chr(ord(new_linha[i])-1)
    print(''.join(new_linha))
"""


















"""
resolução obi
d = int(input())
a = int(input())
n = int(input())
if n > 15:
    n = 15
diaria = d + (n-1)*a
print((31 - n + 1)*diaria)

continuar a minha...
d = int(input())
a = int(input())
n = int(input())
if n>15:
    n=15
print(d+(n-1)*a)
print((31-n+1))
print((d+(n-1)*a)*(31-n+1))

"""



"""
1- Hotel-OBI:
d = int(input())
a = int(input())
n = int(input())
if n == 1:
    print(d*31)
elif n >= 16:
    print((d+(14*a))*(31-n+1))
else:
    print((d+(n-1)*a)*(31-n+1))

2- Maior Valor - OBI:
n = int(input())
m = int(input())
s = int(input())
tem = 0
for i in range(m, n-1,-1):
    tam = str(i)
    num = []
    for j in tam:
        num.append(int(j))
    if sum(num) == s:
        print(i)
        tem = 1
        exit()
if tem == 0:
    print('-1')

3-Quadrado mágico - OBI: 
n = int(input())
tabela = []
numero = None
for i in range(n):
    linha = []
    new_linha = []
    linha = input().split()
    for elemento in linha:
        new_linha.append(int(elemento))
    tabela.append(new_linha)
linha = None
for i in range(n):
    if 0 not in tabela[i]:
        soma = sum(tabela[i])
    for j in range(n):
        if tabela[i][j] == 0:
            linha = i+1
            coluna = j+1
for i in range(n):
    if 0 in tabela[i]:
        numero = soma - sum(tabela[i])
print(numero)
print(linha)
print(coluna)

4- Chuva - OBI:
n = int(input())
s = int(input())
vetor = [int(i) for i in input().split()]
prefix_sum = []
prefix_sum.append(vetor[0])
cont = 0
for x in range(1, len(vetor)):
    prefix_sum.append(prefix_sum[x-1]+vetor[x])
prefix_sum.sort(reverse=True)
for num1 in prefix_sum:
    if num1 == s:
        cont += 1
    for num2 in prefix_sum:
        if num1-num2 == s:
            cont += 1
print(cont)
"""




































"""n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    palavra1 = []
    palavra2 = []
    for let in a:
        palavra1.append(let)
    for let in b:
        palavra2.append(let)
    tam = len(palavra1)-len(palavra2)
    encaixa = 0
    for i in range(len(palavra1)-1, tam-1, -1):
        for j in range(len(palavra2)):
            print(f'{palavra1[i]} {palavra2[j]}')
"""
"""n = int(input())
for _ in range(n):
    linha = input()
    new_linha = []
    for caractere in linha:
        if 90>=ord(caractere)>=65 or 122>=ord(caractere)>=97:
            new_linha.append(chr(ord(caractere)+3))
        else:
            new_linha.append(caractere)
    new_linha.reverse()
    qtd = len(new_linha)
    for i in range(qtd//2,qtd):
        new_linha[i] = chr(ord(new_linha[i])-1)
    print(''.join(new_linha))
"""