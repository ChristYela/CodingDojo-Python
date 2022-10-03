class CuentaBancaria:
    def __init__(self, nombre, tasa_int=0.01, balance=0):
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
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(nombre, tasa_int=0.01, balance=0)
        
usuario1 = Usuario("Cristian Andres Yela")
usuario2 = Usuario("Rodrigo Diaz de Vivar")

cuenta1 = CuentaBancaria("Cristian Andres Yela")
cuenta2 = CuentaBancaria("Rodrigo Diaz de Vivar")
cuenta1.deposito(450).deposito(250).deposito(330).retiro(295).generar_interes().mostrar_info_cta()
cuenta2.deposito(550).deposito(200).retiro(300).retiro(90).retiro(70).retiro(55).generar_interes().mostrar_info_cta()



