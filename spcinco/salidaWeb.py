class SalidaHTML():
    def __init__(self):
        pass

    def procesar(cliente,dicc, nom):
        f=open(str(cliente.dni) + nom + '.html', 'w', encoding='utf-8')
        
        datos= f"""
        <html>
        <head>
            <title>ITBANK</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        </head>
        <body style="background-color:antiquewhite">
            <h1 class="p4 bg-primary text-white border-radius rounded-bottom">ITBANK</h1>
            <div class="fs-2 text fw-bold"> {cliente.apellido +" "+cliente.nombre}<div>
            <div class="fs-4"><b >Numero Cliente: </b>{str(dicc[0]['cuentaNumero'])}</div>
            <div class="fs-4"><b >DNI: </b>{cliente.dni}</div>
            <div class="fs-4"><b >Direccion: </b>{cliente.direccion.calle} {cliente.direccion.numero}, {cliente.direccion.ciudad} </div>
            <table class="table table-bordered border-info ">
                <tr class="bg-primary text fw-bold text-white"><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>"""
        for i in dicc:
            if i["estado"]== "ACEPTADA":

                datos+=f"""
                            <tr class="table-success"><td>{str(i['fecha'])}</td><td>{str(i['tipo']).replace("_", " ")}</td><td class="fw-bold">{str(i['estado'])}</td><td>${str(i['monto'])}</td><td>{str(i['razon'])}</td></tr>
                    """
            else:
                datos+=f"""
                           <tr class="table-danger"><td>{str(i['fecha'])}</td><td>{str(i['tipo']).replace("_", " ")}</td><td class="fw-bold">{str(i['estado'])}</td><td>${str(i['monto'])}</td><td>{str(i['razon'])}</td></tr> 
                    """
        datos+="""
            </table>
        </body>
        </html>"""

        
        f.write(datos)
        f.close()
