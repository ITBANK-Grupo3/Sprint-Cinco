import salidaWeb 

dicc=[
    {"cuentaNumero":34,
    "SolicitudNro":666,
    "estado":"RECHAZADO",
    "razon":"FONDOS NO DISPONIBLES", 
    "fecha": "18/07/2022"}
]

SALIDA = salidaWeb.SalidaHTML.procesar("prueba", dicc)