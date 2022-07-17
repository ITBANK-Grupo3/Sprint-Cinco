class Razon(object):
  def __init__(self, evento, tipoCliente):
    self.monto = evento["monto"]
    self.cupoRestante = evento["cupoDiarioRestante"]
    self.saldoCuenta = evento["saldoEnCuenta"]
    self.totalTarjetasCredito = evento["totalTarjetasDeCreditoActualmente"]
    self.totalChequeras = evento["totalChequerasActualmente"]
    self.tipoCliente = tipoCliente

class RazonAltaChequera(Razon):
  def __str__(self):
    if self.tipoCliente == "CLASSIC":
      return "El usuario perteneciente a Classic no tiene acceso a la creación de chequeras."
    elif self.tipoCliente == "BLACK":
      if self.totalChequeras > 1:
        return "El usuario perteneciente a Black solo puede acceder a dos chequera."
    elif self.tipoCliente == "GOLD":
      if self.totalChequeras > 0:
        return "El usuario perteneciente a Gold solo puede acceder a una chequera."

class RazonAltaTarjetaDeCredito(Razon):
  def __str__(self):
    if self.tipoCliente == "CLASSIC":
      return "El usuario perteneciente a Classic no tiene acceso a la creación de tarjetas de crédito."
    elif self.tipoCliente == "BLACK":
      if self.totalTarjetasCredito > 4:
        return "El usuario perteneciente a Black solo puede acceder hasta cinco tarjetas de crédito."
    elif self.tipoCliente == "GOLD":
      if self.totalTarjetasCredito > 0:
        return "El usuario perteneciente a Gold solo puede acceder a una tarjeta de crédito."

class RazonCompraDolar(Razon):
  def __str__(self):
    if self.tipoCliente == "CLASSIC":
      return "El usuario perteneciente a Classic no tiene acceso a la compra y venta de dólares."
    elif self.tipoCliente == "BLACK" or self.tipoCliente == "GOLD":
      if self.saldoCuenta < self.monto:
        return "La cuenta no posee los fondos suficientes para la cantidad de dolares solicitados."

class RazonRetiroEfectivo(Razon):
  def __str__(self):
    if self.saldoCuenta < self.monto:
        return "No posee fondos suficientes para la extracción."
    elif self.tipoCliente == "CLASSIC":
      if self.monto > self.cupoRestante:
        return "El monto de la extracción supera al cupo diario restante. Recordá que el cupo es de $10.000 al día."
    elif self.tipoCliente == "BLACK":
      if self.monto > self.cupoRestante:
        return "El monto de la extracción supera al cupo diario restante. Recordá que el cupo es de $100.000 al día."
    elif self.tipoCliente == "GOLD":
      if self.monto > self.cupoRestante:
        return "El monto de la extracción supera al cupo diario restante. Recordá que el cupo es de $20.000 al día."

class RazonTransferenciaEnviada(Razon):
  def __str__(self):
    if self.tipoCliente == "CLASSIC":
      if self.saldoCuenta < (self.monto * 1.01):
        return f"No posee fondos suficientes para la transferencia. Faltarían ${(self.monto * 1.01) - self.saldoCuenta} para poder realizar la operación."
    elif self.tipoCliente == "BLACK":
      if self.saldoCuenta < self.monto:
        return f"No posee fondos suficientes para la transferencia. Faltarían ${self.monto - self.saldoCuenta} para poder realizar la operación."
    elif self.tipoCliente == "GOLD":
      if self.saldoCuenta < (self.monto * 1.005):
        return f"No posee fondos suficientes para la transferencia. Faltarían ${(self.monto * 1.005) - self.saldoCuenta} para poder realizar la operación."


class RazonTransferenciaRecibida(Razon):
  def __str__(self):
    if self.tipoCliente == "CLASSIC":
      if self.monto > 150000:
        return "No puede recibir transferencias mayores a $150.000 sin previo aviso."
    elif self.tipoCliente == "BLACK":
      pass
    elif self.tipoCliente == "GOLD":
      if self.monto > 500000:
        return "No puede recibir transferencias mayores a $500.000 sin previo aviso."

