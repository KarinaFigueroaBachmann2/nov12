import easyocr


def leer_patente(imagen):

    lector = easyocr.Reader(
        ["en"]
    )

    resultados = lector.readtext(
        imagen
    )

    texto = ""

    for resultado in resultados:

        texto += resultado[1]

    texto = texto.upper()

    texto = texto.replace(
        " ",
        ""
    )

    return texto
