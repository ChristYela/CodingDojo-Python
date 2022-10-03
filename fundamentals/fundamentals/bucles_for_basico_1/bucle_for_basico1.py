#1 Básico: imprime todos los números enteros del 0 al 150.
for number1 in range(0, 151, 1): #comienzo en 0, detenerse en 151, cantidad a avanzar de 1 en 1
    print(number1)
    
print("-------------")

#2 Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for number2 in range(5, 1001, 5):
    if number2 % 5 == 0: #multiplo de 5
        print(number2)

print("-------------")
#3 Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
# Si es divisible por 5, imprime "Coding” en su lugar. 
# Si es divisible por 10, imprime "Coding Dojo".
for number3 in range(0, 101, 1): #comienzo en 0, detenerse en 101, cantidad a avanzar de 1 en 1
    if (number3 % 10 == 0):
        print("Coding Dojo")                         
    elif (number3 % 5 == 0):
        print("Coding")        
    else:
        print(number3)    
    
print("-------------")

#4 Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
total = 0
num = int(500000) # num=500000
numero_impar = []

for i in range(0, num + 1):
    if i % 2 != 0:
        numero_impar.append(i)
        total += i          
print("la suma de todos los enteros impares desde 0 hasta {} es: {}".format(num,total))

print("-------------")


#5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
def countdown(number5):
    lista = []
    for i in range(number5, -1, -4): #comienzo, detenerse, cantidad a avanzar
        lista.append(i)
    return lista

print(countdown(2018))

print("-------------")

#6 Contador flexible: establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum=2
highNum=9
mult=3
for i in range(lowNum, highNum + 1, 1): #comienzo, detenerse, cantidad a avanzar
    
    if i % mult == 0:
        print(i)
        