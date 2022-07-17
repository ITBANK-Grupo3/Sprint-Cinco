class SalidaHTML():
    def __init__(self):
        pass

    def procesar(nom,dicc):
        f=open(nom+'.html', 'w')
        
        datos= "<html>" + "<h1 style='background-color: blue'> Cuenta Numero"+ str(dicc[0]['cuentaNumero']) +"</h1>" + "</html>"
        
        f.write(datos)
        f.close()
