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

