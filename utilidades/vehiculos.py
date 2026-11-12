from utilidades.conexion import (
    obtener_cliente_supabase
)


def obtener_vehiculo(
    patente
):

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("vehiculos")
        .select("*")
        .eq(
            "patente",
            patente
        )
        .execute()
    )

    if respuesta.data:

        return respuesta.data[0]

    return None


def obtener_vehiculos():

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("vehiculos")
        .select("*")
        .execute()
    )

    return respuesta.data


def actualizar_estado_operativo(
    patente,
    nuevo_estado
):

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("vehiculos")
        .update(
            {
                "estado_operativo":
                nuevo_estado
            }
        )
        .eq(
            "patente",
            patente
        )
        .execute()
    )

    return respuesta


def actualizar_kilometraje(
    patente,
    kilometraje
):

    supabase = obtener_cliente_supabase()

    respuesta = (
        supabase
        .table("vehiculos")
        .update(
            {
                "kilometraje_actual":
                kilometraje
            }
        )
        .eq(
            "patente",
            patente
        )
        .execute()
    )

    return respuesta
