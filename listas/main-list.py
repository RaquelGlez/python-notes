# Listas

""" lista = ['string', 10, 15.6, True]

print(lista) """

""" 
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

primer_curso = lista_cursos[0]

segundo_curso = lista_cursos[1]

ultimo_curso = lista_cursos[4]


print(primer_curso)
print(segundo_curso)
print(ultimo_curso)

primer_curso = lista_cursos[-5]

segundo_curso = lista_cursos[-4]

ultimo_curso = lista_cursos[-1]

print(primer_curso)
print(segundo_curso)
print(ultimo_curso)


print(lista_cursos[100])
 """

""" # Actualizar
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

lista_cursos[4] = 'Rust'

print(lista_cursos) """


# Sublistas
# [start:end]
# [start:end:skip]

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

sub_lista = lista_cursos[0:3]

print(lista_cursos)
"""print(sub_lista)

sub_lista = lista_cursos[2:30]
print(sub_lista) """

""" sub_lista = lista_cursos[2:]
print(sub_lista)

sub_lista = lista_cursos[:4]
print(sub_lista) """

""" 
sub_lista = lista_cursos[1:5:2]
print(sub_lista) """

""" sub_lista = lista_cursos[:]
print(sub_lista) """

""" sub_lista = lista_cursos[::2]
print(sub_lista) """


sub_lista = lista_cursos[::-1]
print(sub_lista)
