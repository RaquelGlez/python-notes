""" tupla = ()

print(tupla)
print(type(tupla)) """

#tupla = ('string', 10, 15.4, True, [1,2,3])

""" tupla = ('string', 10, 15.4, True, [1,2,3],(4,5,6))

print(tupla) """


""" cursos = ['Python', 'Django', 'Flask']

niveles = ('Basico', 'Intermedio', 'Avanzado')

cursos_tupla = tuple(cursos)

print(cursos_tupla)
print(type(cursos_tupla))

niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista)) """



""" numeros = (1,2,3,4, 5, 6)
uno, dos, tres, cuatro, *resto_valores = numeros

print(1)
print(2)
print(3)
print(4)
print(resto_valores) """


""" numeros = (1,2,3,4, 5, 6,7,8,9,10)
#uno, dos, tres, cuatro, *resto_valores, nueve, diez = numeros
uno, _, tres, cuatro, *resto_valores, nueve, diez = numeros

print(uno)
#print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)
print(resto_valores) """




# zip

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

resultado = zip(lista, tupla)

print(resultado)

resultado = tuple(resultado)

print(resultado)
