# lambda
dobro = lambda x: x * 2
print(dobro(7))

soma = lambda x,y: x + y
print(soma(8,7))

# filter
lista = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2 == 0, lista)))

# map
print(list(map(lambda x: x*2, lista)))