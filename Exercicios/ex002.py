nome = input('Qual o seu nome? ') #comando (input) funciona, para receber dados digitados
print("É um prazer te conhecer," + nome + '!') # uso do (+) para concatenar strings

# outra forma de fazer, forma dada pelo Professor na correção. Usando o [.format()]

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

