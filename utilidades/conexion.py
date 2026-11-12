import streamlit as st
from supabase import create_client


def obtener_cliente_supabase():
    """
    Retorna cliente Supabase.
    """

    url = st.secrets["supabase"]["SUPABASE_URL"]
    key = st.secrets["supabase"]["SUPABASE_KEY"]

    return create_client(
        url,
        key
    )

