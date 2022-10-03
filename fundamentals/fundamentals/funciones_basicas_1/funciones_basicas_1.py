#1
def numero_de_grupos_alimetarios():
    return 5
print(numero_de_grupos_alimetarios()) 
# >>> 5
print("-------------")

#2
def numero_de_ramas_militares():
    return 5 
#print(numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo() + numero_de_ramas_militares())
# >>> undefined. 
# se agrega comentario en print, para saltar el error
print("-------------")

#3
def numero_de_libros_en_espera():
    return 5
    return 10
print(numero_de_libros_en_espera())
#>>>5
print("-------------")

#4
def numero_de_dedos():
    return 5
    print(10)
print(numero_de_dedos())
# >>> 5
print("-------------")

#5
def numero_de_lagos_grandes():
    print(5)
x = numero_de_lagos_grandes()
print(x)
# >>> 5 , None
print("-------------")

#6
def add(b,c):
    print(b+c)
#print(add(1,2) + add(2,3))
# se agrega comentario en print, para saltar el error
# >>> 3, 5,Error can't add NoneTypes
print("-------------")

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# >>> "25"
print("-------------")

#8
def numero_de_oceanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(numero_de_oceanos_o_dedos_o_continentes())
# >>> 100, 10
print("-------------")
#9
def numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo(2,3))
# >>> 7
print(numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo(5,3))
# >>> 14
print(numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo(2,3) +numero_de_dias_en_una_semana_silicon_o_lados_del_triangulo(5,3))
# >>> 21
print("-------------")
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# >>> 8
print("-------------")
#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# >>> 500,500, 300, 500
print("-------------")
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# >>>> 500, 500, 300, 500
print("-------------")
#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# >>> 500, 500, 300, 300
print("-------------")
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# >>> 1, 3, 2
print("-------------")
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# >>> 1, 3, 5 , 10
print("-------------")