import streamlit as st

from utilidades.autorizaciones import (
    validar_ingreso
)


def mostrar_pagina_guardia():

    st.header("🛂 Guardia de Garita")

    st.write(
        "Validación de acceso vehicular."
    )

    patente = st.text_input(
        "Patente"
    )

    rut = st.text_input(
        "RUT conductor"
    )

    if st.button("Validar ingreso"):

        if not patente or not rut:

            st.warning(
                "Debe ingresar patente y RUT."
            )

            return

        resultado = validar_ingreso(
            patente.upper(),
            rut
        )

        if resultado["estado"] == "denegado":

            st.error(
                "❌ INGRESO DENEGADO"
            )

            return

        vehiculo = resultado["vehiculo"]

        estado = vehiculo[
            "estado_operativo"
        ]

        if estado == "Operativo":

            st.success(
                "✅ INGRESO AUTORIZADO"
            )

        elif estado == "Requiere Mantención":

            st.warning(
                "⚠ VEHÍCULO REQUIERE MANTENCIÓN"
            )

        else:

            st.error(
                "🚨 VEHÍCULO CRÍTICO"
            )

        st.subheader(
            "Datos del vehículo"
        )

        st.write(
            f"Patente: {vehiculo['patente']}"
        )

        st.write(
            f"Tipo: {vehiculo['tipo_vehiculo']}"
        )

        st.write(
            f"Modelo: {vehiculo['marca_modelo']}"
        )

        st.write(
            f"Kilometraje: {vehiculo['kilometraje_actual']}"
        )

        st.write(
            f"Estado: {vehiculo['estado_operativo']}"
        )
