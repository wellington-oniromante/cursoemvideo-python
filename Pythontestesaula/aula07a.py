n1=int(input('Um valor: '))
n2= int(input('Outro Valor: '))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2
print('A soma é {}, o produto é {} ea divisão é {}'.format(s, m, d))
print('A divisão é {} e potência {}'.format(di, e))
# essa é a versão com quebra de linha nos Prints

n1=int(input('Um valor: '))
n2= int(input('Outro Valor: '))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2
print('A soma é {}, o produto é {} ea divisão é {}'.format(s, m, d), end=' ')
print('A divisão é {} e potência {}'.format(di, e))
# essa é a versão sem quebra de linha nos Prints, usanso o ,end=' '

n1=int(input('Um valor: '))
n2= int(input('Outro Valor: '))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2
print('A soma é {},\no produto é {}\nea divisão é {}'.format(s, m, d), end=' ')
print('A divisão é {} e potência {}'.format(di, e))
# essa é a versão com quebra de linha nos Prints, usando o \n para gerar as quebras

n1=int(input('Um valor: '))
n2= int(input('Outro Valor: '))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2
print('A soma é {},\no produto é {}\nea divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão é {} e potência {}'.format(di, e))
# essa é a versão com quebra de linha nos Prints, usando o {:.3f} para que tenha apenas 3 casa decimais
