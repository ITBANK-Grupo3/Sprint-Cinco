class Cuenta():
    def __init__(self,monto,limiteExtr,limiteTransf,costTransf,saldoDesc):
        self.limite_extraccion_diario=limiteExtr
        self.limite_tranferencia_recibida=limiteTransf
        self.monto=monto
        self.costo_transferencias=costTransf
        self.saldo_descubierto_disponible=saldoDesc

class CuentaClassic(Cuenta):
    def __init__(self, monto, limiteExtr=10000, limiteTransf=150000, costTransf=0.01, saldoDesc=0):
        super().__init__(limiteExtr, limiteTransf, monto, costTransf, saldoDesc)
        self.monto=monto

class CuentaGold(Cuenta):
    def __init__(self, monto, limiteExtr=20000, limiteTransf=500000, costTransf=0.005, saldoDesc=10000):
        super().__init__(monto, limiteExtr, limiteTransf, costTransf, saldoDesc)
        self.monto=monto

class CuentaBlack(Cuenta):
    def __init__(self, monto, limiteExtr=100000, limiteTransf=0, costTransf=0, saldoDesc=10000):
        super().__init__(monto, limiteExtr, limiteTransf, costTransf, saldoDesc)
        self.monto=monto