num1 = 42 # declaración de variable, número inicializado
num2 = 2.3 # declaración de variable, decimal/float inicializado
boolean = True # declaración de variable, booleano inicializado
string = 'Hello World' # declaración de variable, string inicializado

# declaración de variable, lista inicializado
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# declaración de variable, diccionario inicializado
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# declaración de variable, tupla inicializado
fruit = ('blueberry', 'strawberry', 'banana')
# imprime a la consola, verificación de tipo
print(type(fruit))

# imprime a la consola, Valor de acceso a la lista
print(pizza_toppings[1])

#Agrega valor a la lista
pizza_toppings.append('Mushrooms')

# imprime a la consola, valor de acceso al diccionario
print(person['name'])

# cambia valor al diccionario
person['name'] = 'George'
# cambia valor al diccionario
person['eye_color'] = 'blue'

# imprime a la consola, accesa a los datos de la tupla
print(fruit[2])

# Condicional if, evalua, imprime a la consola, Condicional else, imprime a la consola
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Condicional if - elif - else, imprime a la consola
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# Bucle For comienza en 0 y sube hasta 5
for x in range(5):
    print(x)
# Bucle For comienza en 2 y sube hasta 5
for x in range(2,5):
    print(x)
# Bucle For  comienza en 2, sube hasta 10, se incrementa en 3
for x in range(2,10,3):
    print(x)

#While Loop, declaración de variable
x = 0
while(x < 5):
    # imprime a la consola
    print(x)
    # incrementando x
    x += 1

# eliminar de la  lista, el valor final
pizza_toppings.pop()
# eliminar lista, valor en el inicio
pizza_toppings.pop(1)

# imprimir en la consola de diccionario
print(person)
# borra el valor en el diccionario
person.pop('eye_color')
# imprimir en la consola de diccionario
print(person)

# bucle for, recorrido de una lista
for topping in pizza_toppings:
    #Condicional if
    if topping == 'Pepperoni':
        # Continua
        continue
    # imprime a la consola
    print('After 1st if statement')
    # Condicional if
    if topping == 'Olives':
        # se detiene el bucle
        break

# declaración de función
def print_hello_ten_times():
    # bucle for, empieza en 0 aumenta hasta 10
    for num in range(10):
        # imprime en la consola
        print('Hello')

# llama a la función
print_hello_ten_times()

# declaración de la función con parámetro de x
def print_hello_x_times(x):
    # bucle For  hasta un nçumero dado x
    for num in range(x):
        # imprime a la consola
        print('Hello')

# argumento de llamada de función de 4
print_hello_x_times(4)

# declaración de función con parámetro predeterminado
def print_hello_x_or_ten_times(x = 10):
    # bucle For hasta  x
    for num in range(x):
        # imprime a la consola
        print('Hello')

# llamado de función va hasta  10
print_hello_x_or_ten_times()
# llamado de función va hasta 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)