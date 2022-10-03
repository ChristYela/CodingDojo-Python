class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
        

    def hacer_deposito(self, monto):
        self.monto += monto
        return self

    def hacer_retiro(self,monto):
        self.monto -= monto
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario:  {self.nombre},  Balance:  $ { self.monto}"  " USD")
        return self

    def transferir_dinero(self,monto,usuario):
        self.monto -= monto
        usuario.monto += monto
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self


cristian = Usuario("Cristian")
manuel = Usuario("Manuel")
ruben = Usuario("Ruben")

cristian.hacer_deposito(1000).hacer_deposito(2000).hacer_deposito(500).hacer_retiro(450).mostrar_balance_usuario()

manuel.hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(500).hacer_retiro(300).mostrar_balance_usuario()

ruben.hacer_deposito(3500).hacer_retiro(100).hacer_retiro(500).hacer_retiro(300).mostrar_balance_usuario()

cristian.transferir_dinero(400, ruben)