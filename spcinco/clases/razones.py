# Evento para pruebas
evento  = {
"estado": "RECHAZADA",
"tipo": "TRANSFERENCIA_RECIBIDA",
"cuentaNumero": 190,
"cupoDiarioRestante": 3000,
"monto": 200000,
"fecha": "25/06/2022 16:00:55",
"numero": 10,
"saldoEnCuenta": 100000,
"totalTarjetasDeCreditoActualmente": 0,
"totalChequerasActualmente": 0
}


class Razon(object):
  def __init__(self, evento):
    self.estado = evento["estado"]
    self.fecha = evento["fecha"]

  def __str__(self):
    return f"El evento realizado el {self.fecha} se encuentra {self.estado}"

  def resolver(self):
    if self.estado == "RECHAZADA":
      print("Evento rechazado")

class RazonAltaChequera(Razon):
  pass

class RazonAltaTarjetaDeCredito(Razon):
  pass

class RazonCompraDolar(Razon):
  pass

class RazonRetiroEfectivo(Razon):
  pass

class RazonTransferenciaEnviada(Razon):
  pass

class RazonTransferenciaRecibida(Razon):
  pass

holi = RazonAltaChequera(evento)

holi.resolver()

print(holi)