class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuentas = {
        "comprueba": CuentaBancaria(tasa_int=0.02, balance=0),
        "ahorros": CuentaBancaria(tasa_int=0.02, balance=0),
        "cta_interes": CuentaBancaria(tasa_int=0.02, balance=0),
        "interes": CuentaBancaria(tasa_int=0.02, balance=0), 
    }

    def hacer_deposito(self, monto, tipo):
        self.cuentas[tipo].balance += monto
        return self

    def hacer_retiro(self, monto, tipo):
        self.cuentas[tipo].balance -= monto
        return self

    def transferir_dinero(self, tipo, otro_usuario, otro_tipo_usuario, monto):
        self.cuentas[tipo].balance -= monto
        otro_usuario.cuentas[otro_tipo_usuario].balance += monto
        return self

    def mostrar_saldo_usuario(self, tipo):
        print(f"User: {self.nombre}, balance: $ {self.cuentas[tipo].balance}" " USD")


class CuentaBancaria:
    def __init__(self,tasa_int=0.02, balance=0):
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
        print(f" Balance: $ { self.balance}" "USD")

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_int
            return self
        else:
            return self


usuario1 = Usuario("Cristian Yela", "cyela@hotmail.com")
usuario2 = Usuario("Rodrigo Diaz de Vivar", "rdvivar@gmail.com")
usuario3 = Usuario("Pedro Pablo Jaramillo", "ppjaramillo@outlook.com")

usuario1.hacer_deposito(1000,"ahorros").hacer_deposito(1000,"comprueba").hacer_deposito(1000,"comprueba").hacer_retiro(100,"comprueba").transferir_dinero("comprueba",usuario3,"comprueba",100).mostrar_saldo_usuario("ahorros")
usuario1.mostrar_saldo_usuario("comprueba")
usuario2.hacer_deposito(1000,"ahorros").hacer_deposito(1000,"comprueba").hacer_retiro(200, "ahorros").transferir_dinero("comprueba",usuario1,"comprueba",100).mostrar_saldo_usuario("ahorros")
usuario2.mostrar_saldo_usuario("comprueba")
usuario3.hacer_deposito(500, "ahorros").hacer_deposito(700, "comprueba").hacer_retiro(100,"comprueba").hacer_retiro(100, "comprueba").hacer_retiro(150, "comprueba").transferir_dinero("comprueba",usuario2,"comprueba",100).mostrar_saldo_usuario("ahorros")
usuario3.mostrar_saldo_usuario("comprueba") 