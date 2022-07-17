#import cliente
import clases.clienteclases as clienteclases

class Cuenta():
    def __init__(self,cliente,data,saldoEnCuenta):
        self.saldo_encuenta=saldoEnCuenta
        if cliente=="CLASSIC":
            self.tipo_de_cliente=clienteclases.ClienteClassic(data,self.saldo_encuenta)
            self.limite_extraccion_diario=10000
            self.limite_tranferencia_recibida=150000
            self.costo_transferencias=0.01
            self.saldo_descubierto_disponible=0
        elif cliente=="GOLD":
            self.tipo_de_cliente=clienteclases.ClienteGold(data,self.saldo_encuenta)
            self.limite_extraccion_diario=20000
            self.limite_tranferencia_recibida=500000
            self.costo_transferencias=0.005
            self.saldo_descubierto_disponible=10000
        elif cliente=="BLACK":
            self.tipo_de_cliente=clienteclases.ClienteBlack(data,self.saldo_encuenta)
            self.limite_extraccion_diario=100000
            self.costo_transferencias=0
            self.saldo_descubierto_disponible=10000