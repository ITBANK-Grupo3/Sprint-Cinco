from clases import cuenta
from clases import cliente
import json

from clases.cuenta import CuentaClassic

class Lector():
    def __init__(self, archivo):
        self.archivo = archivo
        self.cargar()
        self.eventos=self.data['transacciones']
        if self.data['tipo']=="BLACK":
            self.cliente=cliente.ClienteBlack(self.data)
            # self.cuenta = cuenta.CuentaBlack()
        elif self.data['tipo']=="GOLD":
            self.cliente = cliente.ClienteGold(self.data)
            # self.cuenta = cuenta.CuentaGold()
        else:
            self.cliente = cliente.ClienteClassic(self.data)
            # self.cuenta = CuentaClassic()
            
        

    def cargar(self):
        f=open(self.archivo)
        self.data=json.load(f)
        f.close()
        
            
        

#         for x in self.data ['transacciones']:
#             if x['tipo']=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
#                 if x['estado']=="ACEPTADA":
#                     print(x['tipo'],x['fecha'],x['saldoEnCuenta'],x['monto'])

        
# data = Lector('eventos-classic.json')

