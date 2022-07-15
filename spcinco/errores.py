import clases.razones as rz

class FiltradoDeErrores(object):
  def __init__(self, eventos, tipoCliente):
    self.errores = [error for error in eventos if error["estado"] == "RECHAZADA"]
    for error in self.errores:
      if error["tipo"] == "ALTA_CHEQUERA":
        print(razon := rz.RazonAltaChequera(error, tipoCliente))
      
      elif error["tipo"] == "ALTA_TARJETA_CREDITO":
        print(razon := rz.RazonAltaTarjetaDeCredito(error, tipoCliente))

      elif error["tipo"] == "COMPRA_DOLAR":
        print(razon := rz.RazonCompraDolar(error, tipoCliente))

      elif error["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
        print(razon := rz.RazonRetiroEfectivo(error, tipoCliente))

      elif error["tipo"] == "TRANSFERENCIA_ENVIADA":
        print(razon := rz.RazonTransferenciaEnviada(error, tipoCliente))

      elif error["tipo"] == "TRANSFERENCIA_RECIBIDA":
        print(razon := rz.RazonTransferenciaRecibida(error, tipoCliente))
