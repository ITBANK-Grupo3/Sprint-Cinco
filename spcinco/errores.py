import clases.razones as rz

class FiltradoDeErrores(object):
  def __init__(self, eventos):
    self.errores = [error for error in eventos if error["estado"] == "RECHAZADA"]
    print(self.errores)
    for error in self.errores:
      if error["tipo"] == "ALTA_CHEQUERA":
        print(razon := rz.RazonAltaChequera(error))
      
      elif error["tipo"] == "ALTA_TARJETA_CREDITO":
        print(razon := rz.RazonAltaTarjetaDeCredito(error))
