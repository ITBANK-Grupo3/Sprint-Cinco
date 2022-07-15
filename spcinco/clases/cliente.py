from clases import direccion
class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.direccion= direccion.Direccion(data)
        print('Se creo cliente: '+self.dni)
        print(self.direccion.ciudad)
        
    def baja(self):
        self.tipo='baja'

class ClienteGold(Cliente):
    def puede_comprar_dolar(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_crear_chequera(self):
        return True
    def __init__(self, data, tarjetaDebito=1):
        print('Se creo gold')  
        super().__init__(data)
        self.tarjetaDebito = tarjetaDebito
    
    
         

class ClienteClassic(Cliente):
    def puede_comprar_dolar(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_crear_chequera(self):
        return False
    def __init__(self, data, tarjetaDebito=1):
        print('Se creo classic')
        super().__init__(data) 
        self.tarjetaDebito=tarjetaDebito
        
    

class ClienteBlack(Cliente):
    def puede_comprar_dolar(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_crear_chequera(self):
        return True
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)
        
    



    