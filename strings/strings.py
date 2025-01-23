""" lenguajes = 'Python Ruby Java Rust'

listado_lenguajes =lenguajes.split()

print(listado_lenguajes) """


""" lenguajes = ['Python', 'Ruby', 'Java', 'Rust']

string_lenguajes = ' '.join(lenguajes)

print(string_lenguajes)
print(type(string_lenguajes)) """


# concatenar

nombre = 'Juan'
apellido = 'Mendez'

# nombre_completo = nombre + ' ' + apellido

# nombre_completo = 'Mr. %s %s.' % (nombre, apellido)

# nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)

nombre_completo = f'Mr. {nombre} {apellido} {"Pérez"}.'


print(nombre_completo)
