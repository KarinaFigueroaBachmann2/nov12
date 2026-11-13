import streamlit as st

from paginas.pagina_login import (
    mostrar_pagina_login
)

from paginas.pagina_guardia import (
    mostrar_pagina_guardia
)

from paginas.pagina_conductor import (
    mostrar_pagina_conductor
)

from paginas.pagina_administrador import (
    mostrar_pagina_administrador
)


st.set_page_config(
    page_title="Sistema Control Vehicular Militar",
    page_icon="🚙",
    layout="wide"
)


st.title(
    "Sistema de Control Vehicular Militar"
)

st.divider()

menu = st.sidebar.selectbox(
    "Seleccionar módulo",
    [
        "Login",
        "Guardia",
        "Conductor",
        "Administrador"
    ]
)

if menu == "Login":

    mostrar_pagina_login()

elif menu == "Guardia":

    mostrar_pagina_guardia()

elif menu == "Conductor":

    mostrar_pagina_conductor()

elif menu == "Administrador":

    mostrar_pagina_administrador()
