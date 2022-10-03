class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def hacer_deposito(self, monto):
        self.monto += monto

    def hacer_retiro(self,monto):
        self.monto -= monto

    def mostrar_balance_usuario(self):
        print(f"Usuario:  {self.nombre},  Balance: $ { self.monto}"  " USD")

    def transferir_dinero(self,monto,usuario):
        self.monto -= monto
        usuario.monto += monto
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()


cristian = Usuario("Cristian")
manuel = Usuario("Manuel")
ruben = Usuario("Ruben")

cristian.hacer_deposito(1000)
cristian.hacer_deposito(2000)
cristian.hacer_deposito(500)
cristian.hacer_retiro(450)
cristian.mostrar_balance_usuario()

manuel.hacer_deposito(1000)
manuel.hacer_deposito(1000)
manuel.hacer_retiro(500)
manuel.hacer_retiro(300)
manuel.mostrar_balance_usuario()

ruben.hacer_deposito(3500)
ruben.hacer_retiro(100)
ruben.hacer_retiro(500)
ruben.hacer_retiro(300)
ruben.mostrar_balance_usuario()

cristian.transferir_dinero(400, ruben)