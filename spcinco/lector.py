import cuenta
import json

class Lector():
    def __init__(self, archivo):
        self.archivo = archivo
        self.cargar()
        self.eventos=self.data['transacciones']
        self.cuenta = cuenta.Cuenta(self.data['tipo'],self.data,self.eventos[-1]['saldoEnCuenta'])

    def cargar(self):
        f=open(self.archivo)
        self.data=json.load(f)
        f.close()
        
            
        

#         for x in self.data ['transacciones']:
#             if x['tipo']=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
#                 if x['estado']=="ACEPTADA":
#                     print(x['tipo'],x['fecha'],x['saldoEnCuenta'],x['monto'])

        
# data = Lector('eventos-classic.json')

