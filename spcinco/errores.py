from re import I
import clases.razones as rz

class FiltradoDeErrores(object):
  def __init__(self, eventos, tipoCliente):
    self.errores = [error for error in eventos if error["estado"] == "RECHAZADA"]
    self.eventosProcesados = []
    for evento in eventos:
      if evento["estado"] == "RECHAZADA":
        if evento["tipo"] == "ALTA_CHEQUERA":
          razon = str(rz.RazonAltaChequera(evento, tipoCliente))

        elif evento["tipo"] == "ALTA_TARJETA_CREDITO":
          razon = str(rz.RazonAltaTarjetaDeCredito(evento, tipoCliente))

        elif evento["tipo"] == "COMPRA_DOLAR":
          razon = str(rz.RazonCompraDolar(evento, tipoCliente))

        elif evento["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
          razon = str(rz.RazonRetiroEfectivo(evento, tipoCliente))

        elif evento["tipo"] == "TRANSFERENCIA_ENVIADA":
          razon = str(rz.RazonTransferenciaEnviada(evento, tipoCliente))

        elif evento["tipo"] == "TRANSFERENCIA_RECIBIDA":
          razon = str(rz.RazonTransferenciaRecibida(evento, tipoCliente))
      else:
        razon = "Solicitud realizada con éxito"
      self.eventosProcesados.append({"cuentaNumero": evento["cuentaNumero"],"SolicitudNro":evento["numero"], "estado":evento["estado"],"razon": razon, "fecha": evento["fecha"]})
