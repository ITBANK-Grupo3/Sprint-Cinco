class Razon(object):
  def __init__(self, evento):
    self.estado = evento["estado"]
    self.fecha = evento["fecha"]
    self.numero = evento["numero"]

  def __str__(self):
    return f"Solicitud nro {self.numero} | estado: {self.estado} | {self.fecha}"

  def resolver(self):
    pass

class RazonAltaChequera(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f"Surgió un error al dar de alta la Chequera"

class RazonAltaTarjetaDeCredito(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f"Surgió un error al dar de alta la tarjeta"

class RazonCompraDolar(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f""

class RazonRetiroEfectivo(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f""

class RazonTransferenciaEnviada(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f""

class RazonTransferenciaRecibida(Razon):
  def __init__(self, evento):
    super().__init__(evento)
  def __str__(self):
    return f""

