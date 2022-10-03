class CuentaBancaria:
    def __init__(self, nombre, tasa_int=0.02, balance=0):
        self.nombre= nombre
        self.tasa_int = tasa_int
        self.balance = balance

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if  self.balance > 0:
            self.balance -= monto
            return self
        else:
            self.balance -= 5
        print(f"Fondos insuficientes: cobrando una tarifa de $ 5 USD")
        return self

    def mostrar_info_cta(self):
        print(f"Usuario: {self.nombre}, Balance: $ {self.balance}" " USD") 

    def generar_interes(self):
        if  self.balance > 0:
            self.balance += self.balance * self.tasa_int
            return self
        else:
            return self
        
        
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = CuentaBancaria(nombre,tasa_int=0.02, balance=0) 
        
    def deposito(self, monto):
        self.cuenta.deposito(monto)
        self.cuenta.balance += monto
        print(f"{self.cuenta.nombre} hizo un deposito de: {monto} y su balance ahora es de: {self.cuenta.balance}")
        
    def retiro(self, monto):
        self.cuenta.retiro(monto)
        self.cuenta.balance -= monto
        print(f"{self.cuenta.nombre} hizo un retiro de: {monto} y su balance ahora es de: {self.cuenta.balance}")

    def generar_interes(self):
        self.cuenta.balance += self.cuenta.balance * self.cuenta.tasa_int
        
    def mostrar_info_cta(self):
        print(f"Usuario: {self.cuenta.nombre}, Balance: $ {self.cuenta.balance}" " USD") 

usuario1 = Usuario("Cristian Andres Yela", "cyela@hotmail.com")
usuario2 = Usuario("Rodrigo Diaz de Vivar", "rdvivar@gmail.com")
usuario3 = Usuario("Pedro Pablo Jaramillo", "ppjaramillo@outlook.com")

cuenta1 = CuentaBancaria("Cristian Andres Yela")
cuenta2 = CuentaBancaria("Rodrigo Diaz de Vivar")
cuenta3 = CuentaBancaria("Pedro Pablo Jaramillo")

cuenta1.deposito(450).deposito(250).deposito(330).retiro(295).generar_interes().mostrar_info_cta()
cuenta2.deposito(550).deposito(200).retiro(300).retiro(90).retiro(70).retiro(55).generar_interes().mostrar_info_cta()
cuenta3.deposito(350).deposito(650).retiro(150).retiro(80).generar_interes().mostrar_info_cta()
