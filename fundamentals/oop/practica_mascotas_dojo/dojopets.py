class Mascota:
    def __init__(self, nombre , tipo, trucos, ruido):
        self.nombre = nombre
        self.tipo = tipo
        self.trucos = trucos
        self.salud = 100
        self.energia = 50
        self.ruido = ruido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        self.energia -= 10
        return self

    def ruido(self):
        print(self.ruido)



class Ninja:
    def __init__(self, nombre, apellido, golosinas, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.golosinas = golosinas
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        if len(self.comida_mascota) > 0:
            comida = self.comida_mascota.pop()
            print(f" Alimentando a  {self.mascota.nombre} , {comida}!")
            self.mascota.comer()
        else:
            print("Oh no!!! Necesita mas alimento!")
        return self

    def aseo(self):
        self.mascota.ruido()
        print(self.mascota.ruido)
        

mi_golosina = ['Cuido',"Scooby galletas"]
mi_comida_mascota = ['concentrado','carne']

conchita = Mascota("Donia Conchita","Pony",['levantar la pata','rebusnar'],"Arre Arre")

Cristian = Ninja("Cristian","Yela", mi_golosina, mi_comida_mascota, conchita)

Cristian.alimentar()

