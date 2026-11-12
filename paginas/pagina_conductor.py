import streamlit as st

from utilidades.reportes_estado import (
    guardar_reporte
)


def mostrar_pagina_conductor():

    st.header("🚙 Check-In Operativo")

    st.write(
        "Registro de condición operativa del vehículo."
    )

    with st.form(
        "formulario_conductor"
    ):

        patente = st.text_input(
            "Patente"
        )

        rut = st.text_input(
            "RUT conductor"
        )

        kilometraje = st.number_input(
            "Kilometraje actual",
            min_value=0
        )

        combustible = st.slider(
            "Nivel combustible (%)",
            0,
            100,
            50
        )

        neumaticos = st.checkbox(
            "Neumáticos operativos",
            value=True
        )

        luces = st.checkbox(
            "Luces operativas",
            value=True
        )

        observaciones = st.text_area(
            "Observaciones"
        )

        foto = st.file_uploader(
            "Fotografía evidencia",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

        boton_guardar = (
            st.form_submit_button(
                "Guardar reporte"
            )
        )

    if boton_guardar:

        try:

            guardar_reporte(
                patente=patente.upper(),
                rut=rut,
                kilometraje=kilometraje,
                combustible=combustible,
                neumaticos=neumaticos,
                luces=luces,
                observaciones=observaciones,
                foto_url=None
            )

            st.success(
                "✅ Reporte registrado correctamente."
            )

            if (
                not neumaticos
                or
                not luces
            ):

                st.warning(
                    "⚠ El vehículo debería quedar marcado como 'Requiere Mantención'."
                )

        except Exception as error:

            st.error(
                f"Error: {error}"
            )
