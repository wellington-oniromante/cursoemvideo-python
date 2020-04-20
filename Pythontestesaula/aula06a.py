n1 = input('Digite um valor: ')
print(type(n1))  # O comando Type usado desta forma para determinar o tipo no caso string.

# O comando Type usado desta forma para determinar o tipo no agora, com o comando (int).
# mudando o tipo da variável para inteiro, ou seja, número.
n1 = int(input('Digite o valor: '))
print(type(n1))

# Versão correta do modo antigo
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma vale', s)

# Versão nova, e correta, usando  {} mais comando [.format()]
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma vale {}'.format(s))
print('A soma entre {} mais {} é igual a {}'.format(n1, n2, s))
