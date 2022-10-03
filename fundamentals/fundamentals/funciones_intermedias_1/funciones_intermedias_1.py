#Nota: Evita nombrar las variables y parámetros con palabras claves de clase
# como int, str, list y dict.

# 1 Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
print("-------------")
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

print("-------------")
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print("-------------")
estudiantes[0]['last_name'] = "Bryant"
print(estudiantes)

print("-------------")
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
# En el directorio_deportes, cambia "Messi" por "Andrés".
print("-------------")
directorio_deportes['futbol'][0] = 'Andres'
print(directorio_deportes)
print("-------------")


z = [ {'x': 10, 'y': 20} ]
# Cambia el valor 20 en z a 30
print("-------------")
z[0]['y'] = 30
print(z)
print("-------------")


# 2 Iterar a través de una lista de diccionarios

# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
# Por ejemplo, dada la siguiente lista:
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#  first_name - Michael, last_name - Jordan
#  first_name - John, last_name - Rosales
#  first_name - Mark, last_name - Guillen
#  first_name - KB, last_name - Tonel
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print("-------------")
def iterateDictionary(estudiantes): 
    for s in estudiantes:
        print("first_name - " + s['first_name'] + ", " + "last_name - " +s['last_name']  )
        
impEst= (iterateDictionary(estudiantes))
print("-------------")
        


# 3 Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios
# y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario.
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print("-------------")
def iterateDictionary2(estudiantes): 
    for n in estudiantes:
        print(n['first_name'])
        
impEst= (iterateDictionary2(estudiantes))
print("-------------")

#Y en iterateDictionary2('last_name', estudiantes) debería generar:
# Jordan
# Rosales
# Guillen
# Tonel

print("-------------")
def iterateDictionary2(estudiantes): 
    for a in estudiantes:
        print(a['last_name'])
        
impEst= (iterateDictionary2(estudiantes))
print("-------------")


# 4 Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas,
# imprima el nombre de cada clave junto con el tamaño de su lista,
# y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
# salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
#8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
print("-------------")
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(diccionario):
    for key,value in diccionario.items():
        print("-------------")
        print(f"{len(value)} {key.upper()}")
        print("-------------")
        for i in range(0, len(value)):
            print(value[i])
            

printInfo(dojo)
print("-------------")
