from datetime import datetime

from utilidades.conexion import (
    obtener_cliente_supabase
)


def guardar_reporte(
    patente,
    rut,
    kilometraje,
    combustible,
    neumaticos,
    luces,
    observaciones,
    foto_url=None
):

    supabase = obtener_cliente_supabase()

    datos = {
        "patente": patente,
        "rut_conductor": rut,
        "fecha_reporte": datetime.now().isoformat(),
        "kilometraje_salida": kilometraje,
        "nivel_combustible": combustible,
        "presion_neumaticos": neumaticos,
        "luces_operativas": luces,
        "observaciones": observaciones,
        "foto_evidencia_url": foto_url
    }

    respuesta = (
        supabase
        .table("reportes_estado")
        .insert(datos)
        .execute()
    )

    if (
        neumaticos is False
        or
        luces is False
    ):

        (
            supabase
            .table("vehiculos")
            .update(
                {
                    "estado_operativo":
                    "Requiere Mantención"
                }
            )
            .eq(
                "patente",
                patente
            )
            .execute()
        )

    return respuesta


def obtener_reportes():

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("reportes_estado")
        .select("*")
        .execute()
    )

    return respuesta.data


def obtener_reportes_por_patente(
    patente
):

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("reportes_estado")
        .select("*")
        .eq(
            "patente",
            patente
        )
        .execute()
    )

    return respuesta.data

