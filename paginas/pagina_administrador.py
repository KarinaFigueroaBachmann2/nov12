import streamlit as st

from utilidades.indicadores import (
    obtener_indicadores
)


def mostrar_pagina_administrador():

    st.header(
        "📊 Puesto de Mando"
    )

    st.write(
        "Panel de monitoreo operacional."
    )

    try:

        datos = obtener_indicadores()

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        with col1:

            st.metric(
                "Operativos",
                datos["operativos"]
            )

        with col2:

            st.metric(
                "Mantención",
                datos["mantencion"]
            )

        with col3:

            st.metric(
                "Críticos",
                datos["criticos"]
            )

        with col4:

            st.metric(
                "Disponibilidad %",
                round(
                    datos["disponibilidad"],
                    2
                )
            )

        st.divider()

        st.subheader(
            "Estado actual de la flota"
        )

        st.dataframe(
            datos["vehiculos"],
            use_container_width=True
        )

    except Exception as error:

        st.error(
            f"Error: {error}"
        )
