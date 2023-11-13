class CuentaBancaria:
    cuentas = []
    
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("Fondos insuficientes: Se está cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return f"{self.balance}"

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {
            "cheques": CuentaBancaria(0.02, 1000),
            "ahorros": CuentaBancaria(0.05, 3000)
        }

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}, Saldo de Cheques: {self.cuenta['cheques'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.nombre}, Saldo de Ahorros: {self.cuenta['ahorros'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self, monto, usuario):
        self.cuenta['cheques'].retiro(monto)
        usuario.cuenta['cheques'].deposito(monto)
        self.mostrar_saldo_usuario()
        usuario.mostrar_saldo_usuario()
        return self


guido = Usuario("Guido")

guido.cuenta['cheques'].deposito(100)
guido.mostrar_saldo_usuario()

