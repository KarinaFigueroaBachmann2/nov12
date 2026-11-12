from utilidades.conexion import (
    obtener_cliente_supabase
)


def obtener_indicadores():

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("vehiculos")
        .select("*")
        .execute()
    )

    vehiculos = respuesta.data

    total = len(vehiculos)

    operativos = len(
        [
            v
            for v in vehiculos
            if v["estado_operativo"]
            == "Operativo"
        ]
    )

    mantencion = len(
        [
            v
            for v in vehiculos
            if v["estado_operativo"]
            == "Requiere Mantención"
        ]
    )

    criticos = len(
        [
            v
            for v in vehiculos
            if v["estado_operativo"]
            == "Crítico"
        ]
    )

    if total > 0:

        disponibilidad = (
            operativos / total
        ) * 100

    else:

        disponibilidad = 0

    return {
        "vehiculos": vehiculos,
        "operativos": operativos,
        "mantencion": mantencion,
        "criticos": criticos,
        "disponibilidad": disponibilidad
    }
