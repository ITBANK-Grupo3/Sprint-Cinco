import lector
import errores

#Procesamiento Cliente Classic
data = lector.Lector('../eventos-classic.json')

eventos = data.eventos
cliente = data.cliente
erroresData = errores.FiltradoDeErrores(eventos, cliente.tipo)

eventosProcesados = erroresData.eventosProcesados

#Procesamiento Cliente Black
dataDos = lector.Lector('../eventos-black.json')

eventosDos = dataDos.eventos
clienteDos = dataDos.cliente
erroresDataDos = errores.FiltradoDeErrores(eventosDos, clienteDos.tipo)

eventosProcesadosDos = erroresDataDos.eventosProcesados
