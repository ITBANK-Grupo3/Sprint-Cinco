import lector
import errores

data = lector.Lector('../eventos-classic.json')

eventos = data.eventos
cliente = data.cliente
erroresData = errores.FiltradoDeErrores(eventos, cliente.tipo)

eventosProcesados = erroresData.eventosProcesados
