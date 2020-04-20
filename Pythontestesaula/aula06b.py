# para fazer um numero ,mesmo inteiro se tornar real. No caso o numero 7
n = float(input('Digite um valor: '))
print(n)

# para fazer um numero ,se manter, inteiro. No caso o numero 7
n = int(input('Digite um valor: '))
print(n)

# para fazer um , inteiro, ser uma string. Isso ocorre sem o (str) também. No caso o numero 7
n = str(input('Digite um valor: '))
print(n)

# para usar um número inteiro em uma situação "boleana" de True/ False. No caso o numero 7
n = bool(input('Digite um valor:'))
print(n)
# no caso o Bolean, como o valor foi digitado então é verdade. Caso não seria mentira (false)
###################################################################################
# Usando o (n.isnumeric), ele diz se é possivel , converter algo para numerico.
n = input('Digite algo: ')
print(n.isnumeric())

# Usando o (n.isalpha), ele diz se é possivel , converter algo para letra.
n = input('Digite algo: ')
print(n.isalpha())

# Usando o (n.isalnum), ele diz se é algo alfanumérico.
n = input('Digite algo: ')
print(n.isalnum())

# Usando o (n.isupper), ele diz se  algo esta em maiusculo.
n = input('Digite algo: ')
print(n.isupper())

