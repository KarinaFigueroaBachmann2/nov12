import streamlit as st


def mostrar_pagina_login():

    st.header("🔐 Inicio de Sesión")

    nombre_usuario = st.text_input(
        "Nombre de usuario"
    )

    perfil = st.selectbox(
        "Perfil",
        [
            "Guardia",
            "Conductor",
            "Administrador"
        ]
    )

    if st.button(
        "Ingresar"
    ):

        st.session_state[
            "sesion_iniciada"
        ] = True

        st.session_state[
            "usuario"
        ] = nombre_usuario

        st.session_state[
            "perfil"
        ] = perfil

        st.success(
            f"Bienvenido {nombre_usuario}"
        )
