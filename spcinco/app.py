import lector
import errores
import salidaWeb

'''#Procesamiento Cliente Classic
dataClassic = lector.Lector('../eventos-classic.json')

eventosClassic = dataClassic.eventos
clienteClassic = dataClassic.cliente
erroresDataClassic = errores.FiltradoDeErrores(eventosClassic, clienteClassic.tipo)

eventosProcesadosClassic = erroresDataClassic.eventosProcesados
salidaWeb.SalidaHTML.procesar("clienteClassic",eventosProcesadosClassic)

#Procesamiento Cliente Gold
dataGold = lector.Lector('../eventos-gold.json')

eventosGold = dataGold.eventos
clienteGold = dataGold.cliente
erroresDataGold = errores.FiltradoDeErrores(eventosGold, clienteGold.tipo)

eventosProcesadosGold = erroresDataGold.eventosProcesados
salidaWeb.SalidaHTML.procesar("clienteGold", eventosProcesadosGold)

#Procesamiento Cliente Black
dataBlack = lector.Lector('../eventos-black.json')

eventosBlack = dataBlack.eventos
clienteBlack = dataBlack.cliente
erroresDataBlack = errores.FiltradoDeErrores(eventosBlack, clienteBlack.tipo)

eventosProcesadosBlack = erroresDataBlack.eventosProcesados
salidaWeb.SalidaHTML.procesar("clienteBlack", eventosProcesadosBlack)

# Datos en pantalla
print("Eventos Classic-----------")
print(eventosProcesadosClassic)
print()
print("Eventos Gold--------------")
print(eventosProcesadosGold)
print()
print("Eventos Black-------------")
print(eventosProcesadosBlack)'''
