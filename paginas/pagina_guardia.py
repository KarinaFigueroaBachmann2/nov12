import streamlit as st

from utilidades.autorizaciones import (
    validar_ingreso
)

from utilidades.ocr_patente import (
    leer_patente
)


def mostrar_pagina_guardia():

    st.header("🛂 Control de Acceso Vehicular")

    st.write(
        "Validación de conductor y vehículo autorizado."
    )

    foto_patente = st.camera_input(
        "Fotografiar patente"
    )

    patente_detectada = ""

    if foto_patente:

        st.image(
            foto_patente,
            caption="Patente capturada"
        )

        try:

            patente_detectada = leer_patente(
                foto_patente
            )

            st.success(
                f"Patente detectada: {patente_detectada}"
            )

        except Exception as error:

            st.warning(
                f"No fue posible leer la patente: {error}"
            )

    patente = st.text_input(
        "Patente",
        value=patente_detectada
    )

    rut = st.text_input(
        "RUT conductor"
    )

    if st.button("Validar ingreso"):

        if not patente or not rut:

            st.warning(
                "Debe ingresar patente y RUT"
            )

            return

        try:

            resultado = validar_ingreso(
                patente.upper(),
                rut
            )

            if resultado["estado"] == "denegado":

                st.error(
                    "❌ INGRESO DENEGADO"
                )

            else:

                vehiculo = resultado[
                    "vehiculo"
                ]

                st.success(
                    "✅ VEHÍCULO AUTORIZADO"
                )

                estado = vehiculo[
                    "estado_operativo"
                ]

                if estado == "Operativo":

                    st.success(
                        "✅ Estado operativo"
                    )

                elif estado == "Requiere Mantención":

                    st.warning(
                        "⚠ Requiere mantención"
                    )

                else:

                    st.error(
                        "🚨 Estado crítico"
                    )

                st.subheader(
                    "Información vehículo"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Patente:** {vehiculo['patente']}"
                    )

                    st.write(
                        f"**Tipo:** {vehiculo['tipo_vehiculo']}"
                    )

                    st.write(
                        f"**Marca:** {vehiculo['marca_modelo']}"
                    )

                with col2:

                    st.write(
                        f"**Año:** {vehiculo['anio']}"
                    )

                    st.write(
                        f"**Kilometraje:** {vehiculo['kilometraje_actual']}"
                    )

                    st.write(
                        f"**Estado:** {vehiculo['estado_operativo']}"
                    )

        except Exception as error:

            st.error(
                f"Error: {error}"
            )
