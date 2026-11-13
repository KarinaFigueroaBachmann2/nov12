import pandas as pd
from supabase import create_client

SUPABASE_URL = "https://apkqaalyrgzblzdvdrmj.supabase.co
"
SUPABASE_KEY = "sb_secret_92z0vL4zFo6LizHWdeq02g_Rbf5D1-4"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

tablas = ["conductores", "vehiculos", "autorizaciones", "reportes_estado"]

for tabla in tablas:
    respuesta = supabase.table(tabla).select("*").execute()
    datos = respuesta.data

    if datos:
        df = pd.DataFrame(datos)
        df.to_csv(f"{tabla}.csv", index=False, encoding="utf-8-sig")
        df.to_excel(f"{tabla}.xlsx", index=False)
        print(f"Tabla {tabla} descargada correctamente.")

    else:
        print(f"La tabla {tabla} esta vacia.")
