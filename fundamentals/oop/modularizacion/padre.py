local_val = "Mula Conchita"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hello"


print(square(5))
usuario = Usuario("Cristian Yela")
print(usuario.name)
print(usuario.di_hola())

print(__name__)

if __name__ == "__main__":
    print("el archivo se esta ejecutando directamente")
else:
    print("El archivo se esta ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)
