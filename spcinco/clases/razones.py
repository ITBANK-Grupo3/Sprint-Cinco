class Razon(object):
  def __init__(self, evento, tipoCliente):
    self.estado = evento["estado"]
    self.fecha = evento["fecha"]
    self.numero = evento["numero"]
    self.tipoCliente = tipoCliente

  def __str__(self):
    return f"Solicitud nro {self.numero} | estado: {self.estado} | {self.fecha}"

  def resolver(self):
    pass

class RazonAltaChequera(Razon):
  def __str__(self):
    return f"alta la Chequera"

class RazonAltaTarjetaDeCredito(Razon):
  def __str__(self):
    return f"alta la tarjeta"

class RazonCompraDolar(Razon):
  def __str__(self):
    return f"compra dolar"

class RazonRetiroEfectivo(Razon):
  def __str__(self):
    return f"retiro efectivo"

class RazonTransferenciaEnviada(Razon):
  def __str__(self):
    return f"transferencia enviada"

class RazonTransferenciaRecibida(Razon):
  def __str__(self):
    return f"transferencia recibida"

