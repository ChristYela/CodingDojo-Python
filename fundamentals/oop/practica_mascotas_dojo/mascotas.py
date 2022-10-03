class Ninja:
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota, salud):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota
        self.salud = 100
        self.energia = 100
        

    def caminar(self):
        self.salud += 5
        self.energia -= 25
        return self

    def alimentar(self):
        self.salud -= 5
        return self

    def asear(self):
        self.salud -= 5
        return self

    def displayHealth(self):
        print("Ninja: " + str(self.nombre ) + " " + str(self.apellido) + ", Mascota: " + str(self.mascota) + ", Salud: " + str(self.salud) + ", Energia: " + str(self.energia))


class Mascota(Ninja):
    def __init__(self, nombre, salud, energia, sonido):
        super().__init__(nombre, salud)
        self.salud = salud
        self.energia = energia
        self.sonido = sonido

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
    
    def sonido(self):
        print(self.sonido)

    def display_health_mascota(self):
        super().displayHealth()
        print("Soy una super mascota")
        return self  



ninja_1 = Ninja("Cristian", "Yela", "Artemis", "dar un paseo", "porcion favorita", 100)
ninja_2 = Ninja("Andres", "Garcia", "Canela", "apapachos", "cuido preferido", 100)

ninja_1.alimentar().caminar().asear().displayHealth()
ninja_2.alimentar().caminar().asear().displayHealth()
