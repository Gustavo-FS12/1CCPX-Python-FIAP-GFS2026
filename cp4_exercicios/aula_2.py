t = ('a', 'b', 'c')
print(t)
print(t[0])

#Erro --> TypeError: 'tuple' object does not support item assignment
#t[0] = 'a'

t1 = 'A',
print(t1)

t2 = t1 + t[1:]
print(t2)

#ATRIBUÇÃO DE DUPLAS
a = 5
b = 10

a, b = b, a
print(a, b)

email = 'sinforoso@gmail.com'
username, dominio = email.split('@')
print(username)
print(dominio)