"""Todo el codigo está en la pagina Python.org, en PyPI(aqui hay paquetes de python)"""
#pip install qrcode

import qrcode

def generar_codigo_qr(datos, nombre_archivo):
    qr = qrcode.QRCode(
        version =1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    qr.add_data(datos)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', back_color = "white")
    img.save(nombre_archivo+".png")
    
datos_para_qr = "https://luna07-zh.github.io/Curriculum-Luna-Calle-Briceno/"
nombre_archivo = "codigoqr_github"

generar_codigo_qr(datos_para_qr, nombre_archivo)

