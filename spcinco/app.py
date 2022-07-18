import lector
import errores
import salidaWeb

jsonBlack = "../eventos-black.json"
jsonClassic = "../eventos-classic.json"
jsonGold = "../eventos-gold.json"

#Procesamiento Cliente Classic
cuentaClassic = lector.Lector(jsonClassic)

eventosClassic = cuentaClassic.eventos
clienteClassic = cuentaClassic.cuenta.tipo_de_cliente
erroresDataClassic = errores.FiltradoDeErrores(eventosClassic, clienteClassic.tipo)

eventosProcesadosClassic = erroresDataClassic.eventosProcesados
salidaWeb.SalidaHTML.procesar(clienteClassic,eventosProcesadosClassic, "Classic")

# Procesamiento Cliente Gold
cuentaGold = lector.Lector('../eventos-gold.json')

eventosGold = cuentaGold.eventos
clienteGold = cuentaGold.cuenta.tipo_de_cliente
erroresDataGold = errores.FiltradoDeErrores(eventosGold, clienteGold.tipo)

eventosProcesadosGold = erroresDataGold.eventosProcesados
salidaWeb.SalidaHTML.procesar(clienteGold, eventosProcesadosGold, "Gold")

#Procesamiento Cliente Black
cuentaBlack = lector.Lector('../eventos-black.json')

eventosBlack = cuentaBlack.eventos
clienteBlack = cuentaBlack.cuenta.tipo_de_cliente
erroresDataBlack = errores.FiltradoDeErrores(eventosBlack, clienteBlack.tipo)

eventosProcesadosBlack = erroresDataBlack.eventosProcesados
salidaWeb.SalidaHTML.procesar(clienteBlack, eventosProcesadosBlack, "Black")
