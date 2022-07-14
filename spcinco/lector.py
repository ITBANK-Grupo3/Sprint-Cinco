import json

class Lector():
    def __init__(self, archivo):
        self.archivo = archivo
        self.cargar()

    def cargar(self):
        f=open(self.archivo)
        self.data=json.load(f)
        f.close()

        for x in self.data ['transacciones']:
            print(x['estado'])

data = Lector('eventos-classic.json')