from utilidades.conexion import (
    obtener_cliente_supabase
)


def validar_ingreso(
    patente,
    rut_conductor
):

    supabase = obtener_cliente_supabase()

    autorizacion = (
        supabase
        .table("autorizaciones")
        .select("*")
        .eq(
            "patente",
            patente
        )
        .eq(
            "rut_conductor",
            rut_conductor
        )
        .eq(
            "vigente",
            True
        )
        .execute()
    )

    if not autorizacion.data:

        return {
            "estado": "denegado"
        }

    vehiculo = (
        supabase
        .table("vehiculos")
        .select("*")
        .eq(
            "patente",
            patente
        )
        .execute()
    )

    if not vehiculo.data:

        return {
            "estado": "denegado"
        }

    conductor = (
        supabase
        .table("conductores")
        .select("*")
        .eq(
            "rut",
            rut_conductor
        )
        .execute()
    )

    if not conductor.data:

        return {
            "estado": "denegado"
        }

    return {
        "estado": "autorizado",
        "vehiculo": vehiculo.data[0],
        "conductor": conductor.data[0]
    }
